# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 11:37:41 2022

@author: Alex Warren
"""
#IMPORT MODULES
#--------------
# Generate random numbers.
import random 
# GUI. 
import tkinter 
import tkinter.ttk 
#import tkinter.font as fnt
# Plot and Animation Creation.
import matplotlib
# Use function to state which backend matplotlib is to use.
matplotlib.use("TkAgg")
import matplotlib.pyplot 
# To generate an animation
from matplotlib.animation import FuncAnimation 
# Processing time.
import time 
# Imports Agent Class.
import AgentFramework
# Read in CSV.
import csv



# SETUP
# ------
# Calculate time takes code to execute.
start = time.process_time()
# Ensures the 'random' package generates same number sequence every time file is run.
random.seed(1)
# Total number of agents to create.
num_of_agents = 10
# Number of times to iterate.
num_of_iterations = 100



# CREATE ENVIRONMENT
# ------------------
# Start environment as empty array (will be populated by values from CSV data).
environment = []
# Open CSV file.
f = open('in.txt', newline='')
# Reader is array from CSV data.
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) 
# Loop over CSV data to get each row.
for row in reader:
    # rowlist is the current row
    rowlist = []   
    # Loop through each value in this row.
    for value in row:
        # Add values to 'rowlist' then add the rowlist to 'environment'.
        rowlist.append(value)
    environment.append(rowlist)
# Close f to return file back to operating system    
f.close() 
#print(rowlist) #test 
#print(environment) #test



# CREATE AGENTS, INTERACTIONS AND ANIMATION
# ---------------------------
# Empty array for adding agents.
agents = []

for i in range(num_of_agents):
    # Append a new instance of the Agent class to the agents array.
    agents.append(AgentFramework.Agent(environment))

# Create carry on variable and set to True.     
carry_on = True	

# Function to create scatter plot based on agents moving across environment. 
def update(frame_number):   
    
    fig.clear()
    global carry_on
    
    # Move agents and interact with environment. 
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            # Calls move function - moves agent position based on random number.
            agents[i].move()
            # Calls eat function - agent interacts with environment and changes store. 
            agents[i].eat()
     
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")      
     
    
    for i in range(len(agents)):
        # Plot the agent data as a scatter.
        matplotlib.pyplot.xlim(0, 100)
        # Set y axis - 0 (bottom) - 100 (top).
        matplotlib.pyplot.ylim(0, 100) 
        # Display takes in environment. 
        matplotlib.pyplot.imshow(environment)
        # Display agents.
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)


# Empty array for adding all created agents. Enables agent to know location of other agents.
all_agents = []        
# Loop over all the agents.
for i in range(num_of_agents):
    # Set the all_agents value to the full agents array on this instance of agent.
    agents[i].set_all_agents(agents)
    all_agents.append
#print(all_agents)


# Create the Neighbourhood
neighbourhood = 50
# Loop through agents for num_of_iterations.
for j in range(num_of_iterations):
    for i in range(len(agents)):
        # Call share_with_neighbours function which alters agent's store value based on proximity. 
        agents[i].share_with_neighbours(neighbourhood)
#print(agents)

# Function created so that when agents stores all not empty the animation stops. 		
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 10) & (carry_on) :
        # Returns control and waits next call.
        yield a			
        a = a + 1


# Create figure and axes
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = matplotlib.pyplot.axes([0, 0, 1, 1])

# Commented out - animation which runs until num_of_iterations completed.
#animation = FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
# Animation runs until agents stores are all not empty.
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
#matplotlib.pyplot.imshow()



#CREATING GUI 
#------------
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw() 

# Creates main window called root.
root = tkinter.Tk()
# Sets root title 
root.wm_title("Agent Based Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 
# Create menu bar.
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

# Sets the GUI waiting for events
tkinter.mainloop()

#END
#---
# Calculate and print processing time.
end = time.process_time()
print("time = " + str(end - start))

