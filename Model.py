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
# Plot and Animation Creation.
import matplotlib
# Use function to state which backend matplotlib is to use.
matplotlib.use("TkAgg")
import matplotlib.pyplot 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.animation import FuncAnimation 
# Processing time.
import time 
# Imports Agent Class.
import AgentFramework
# Read in CSV.
import csv
# Read in web data.
import requests
import bs4



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



#CREATING ANIMATION AND GUI 
#--------------------------
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#ax.set_autoscale_on(False)



# CREATE AGENTS
# --------------
# Empty array for adding agents.
agents = []

for i in range(num_of_agents):
    # Append a new instance of the Agent class to the agents array.
    agents.append(AgentFramework.Agent(environment))

# Move agents and interact with environment. 
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        # Calls move function - moves agent position based on random number.
        agents[i].move()
        # Calls eat function - agent interacts with environment and changes store. 
        agents[i].eat()

# Empty array for adding all created agents. Enables agent to know location of other agents.
all_agents = []        
# Loop over all the agents.
for i in range(num_of_agents):
    # Set the all_agents value to the full agents array on this instance of agent.
    agents[i].set_all_agents(agents)
    all_agents.append
print(all_agents)



# PLOT AGENTS ON SCATTER GRAPH
# ----------------------------
# Set x axis - 0 (left) - 100 (right).
matplotlib.pyplot.xlim(0, 100)
# Set y axis - 0 (bottom) - 100 (top).
matplotlib.pyplot.ylim(0, 100) 
# Display takes in environment. 
matplotlib.pyplot.imshow(environment)
# Loop over the agents.
for i in range(len(agents)):
    # Plot the agent data as a scatter.
    matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
    # Pause animates scatter plot to show one agent every second.
    matplotlib.pyplot.pause(1) 
# Display scatter plot.
matplotlib.pyplot.imshow 



# AGENTS INTERACT WITH NEIGHBOURHOOD
#-----------------------------------
# Create the Neighbourhood
neighbourhood = 50
# Loop through agents for num_of_iterations.
for j in range(num_of_iterations):
    for i in range(len(agents)):
        # Call share_with_neighbours function which alters agent's store value based on proximity. 
        agents[i].share_with_neighbours(neighbourhood)

#FUNCTION USES ALL_AGENTS SO SHOULD IT BE
# all_agents[i].share_with_neighbours(neighbourhood)


#TRY THESE THEN REMOVE IF CANNOT GET WORKING...
# Calculate distance between agents 
"""for i in range(0, num_of_agents, 1):
    for j in range(i + 1, num_of_agents, 1): #excludes 0 from calculations
        distance = agents[i].distance_between(agent)
print(distance)  """  

#calculate distance between agents.
#mindis = AgentFramework_New.distance_between() #minimum distance 
#for i in range(0, num_of_agents, 1):
    #for j in range(i + 1, num_of_agents, 1): #excludes 0 from calculations
        #print(i, j)
        #distance = distance_between()
#mindis = min(mindis, AgentFramework_New.distance)
#print(mindis)
#END...



#CREATING ANIMATION AND GUI CONTINUED
#------------------------------------
"""def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw() """

# Builds the main window
root = tkinter.Tk()
    #Do I need? - is that why two are created test with each. 
    # Sets window
    #window = tkinter.Tk()
# Creates button and assigns to variable title.
title = tkinter.Button(text="Agent Based Model", fg="black", bg="white", width=18, height=2)
# Use the pack method to add title to window. 
title.pack()
# Create figure.
figure = Figure(figsize=(7, 7), dpi=100)
# Subplot within figure. 
plot = figure.add_subplot(1, 1, 1) 
#create an instance of FigureCanvasTkAgg - an interface between the Figure and Tkinter Canvas.
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(figure, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 
root.mainloop()



#END
#---
# Calculate and print processing time.
end = time.process_time()
print("time = " + str(end - start))


