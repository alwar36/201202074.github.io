# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 11:37:41 2022

@author: Alex Warren
"""
#import modules at the top of code

import random # Generate random numbers
import matplotlib # Module to create plots
import tkinter 
import tkinter.ttk 
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot 
# FuncAnimation creates animations using functions.
#from matplotlib.animation import FuncAnimation #To create animations
import time # Time module to observe runtime. 
import AgentFramework_New # File containing Agent class and functions.
import csv # Module to read CSVs.
import requests
import bs4



# SETUP
# ------
# Calculate time takes code to execute.
# https://docs.python.org/3/library/time.html#time.process_time
start = time.process_time()
# Ensure that 'random' package generates the same number sequence every time this file is run.
# https://docs.python.org/3/library/random.html
random.seed(1)
# Total number of agents to create.
num_of_agents = 10
# Number of times to iterate.
num_of_iterations = 100



# CREATE ENVIRONMENT
# ------------------
# Start environment as empty array (will be populated by values from CSV data).
# The numbers are the grass values.
environment = []
# Open CSV file.
f = open('in.txt', newline='')
# reader is array from CSV data.
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
f.close() # Close f to return file back to operating system

#print(rowlist) #test 
#print(environment) #test



#CREATING ANIMATION AND GUI WITH TITLE FRAME
#-----------------------------
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#ax.set_autoscale_on(False)

# CREATE AGENTS
# --------------
# Empty array for adding agents.
agents = []

for i in range(num_of_agents):
    # Append a new instance of the Agent class to the agents array.
    agents.append(AgentFramework_New.Agent(environment))

#Loop to move agents and agents to interact with environment. 
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        #calls move function - moves agent position based on random number.
        agents[i].move()
        #calls eat function - agent interacts with environment and changes store. 
        agents[i].eat()

all_agents = []        
# Loop over all the agents.
for i in range(num_of_agents):
    # Set the all_agents value to the full agents array on this instance of agent.
    agents[i].set_all_agents(agents)
    all_agents.append
print(all_agents)



# PLOT AGENTS ON SCATTER GRAPH
# ----------------------------
# https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.xlim.html
matplotlib.pyplot.xlim(0, 100) # 0 (left) - 100 (right)
matplotlib.pyplot.ylim(0, 100) # 0 (bottom) - 100 (top)
# Display data as an image
matplotlib.pyplot.imshow(environment)
# Loop over the agents.
for i in range(len(agents)):
    # Plot the agent data as a scatter.
    matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
    #scatter plots animates showing point every 2 seconds
    matplotlib.pyplot.pause(1) 
#matplotlib.pyplot.imshow 




# AGENTS INTERACT WITH NEIGHBOURHOOD
#-----------------------------------
# Create the Neighbourhood
neighbourhood = 50

for j in range(num_of_iterations):
    for i in range(len(agents)):
        agents[i].share_with_neighbours(neighbourhood)
    
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

"""for i in range(10): #len(agents)
    #excludes 0 from calculations
    for j in range(i + 1, 10, 1): 
        # Run calculation on this instance using another instance."""




#CREATE GUI
#----------
"""def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw() 

# Builds the main window
root = tkinter.Tk()
# Sets window title
window = tkinter.Tk()
#creates frame 
#creates button called ABM and assigns to variable title. This only creates label does not add it to window.
title = tkinter.Button(text="Agent Based Model", fg="black", bg="white", width=18, height=2)
#foreground (fg), background (bg) colours to MediumSlateBlue #7B68EE and Lavender #E6E6FA
#width and height values measured in text units
#https://en.wikipedia.org/wiki/Web_colors#Hex_triplet 
#to add title to window use the pack method. 
title.pack()
#add title label into a frame
figure = Figure(figsize=(7, 7), dpi=100)
plot = figure.add_subplot(1, 1, 1) # subplot to take up the entire figure
#create an instance of FigureCanvasTkAgg
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(figure, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 


#to begin application
root.mainloop()
"""


#calculates time taken to run.
end = time.process_time()
print("time = " + str(end - start))


