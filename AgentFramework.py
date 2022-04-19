# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 14:43:22 2022

@author: Alex Warren
"""
import random

# A single agent class.
class Agent:
    # Constructor - When the class is instantiated this runs.
    # Takes an ENVIRONMENT
    def __init__(self, environment):
        # _x is random int on each Agent.
        self._x = random.randint(0,99)
        # _y is random int on each Agent.
        self._y = random.randint(0,99)
        # Set the passed environment value on this agent.
        self.environment = environment
        # Start the store on this agent as 0.
        self.store = 0 
        # Start the agents array that will contain all the created agents.
        self.all_agents = []
        
    
    def move(self):
        """
        Function to move agents position using a random number.

        Returns
        Number altered by +/- 1. 

        """

        # If random num is less than 0.5 
        if random.random() < 0.5:
            # _x is incremented 
            self._x = (self._x + 1) % 100
        else:
            # _x is decremented 
            self._x = (self._x - 1) % 100
        if random.random() < 0.5:
            # _y is incremented 
            self._y = (self._y + 1) % 100
        else:
            # _y is decremented 
            self._y = (self._y - 1) % 100
    
    # Method for increasing store value.
    def eat(self):
        # If there's more than 10 left in the cell.
        if self.environment[self._y][self._x] > 10:
            # delete 10 from the cell.
            self.environment[self._y][self._x] -= 10
            # increase store on this agent by 10.
            self.store += 10

    # Return my X value.
    def getx(self):
        #print("getx called")
        return self._x
    
    # Set the X value (passed in).
    def setx(self, value):
        #print("setx called")
        self._x = value
    
    # Python thing that allows you to call these properties with self.x
    x = property(getx, setx,"The 'x' property.")
    
    # Return my Y value.
    def gety(self):
        #print("gety called")
        return self._y
    
    # Set the Y value (passed in).
    def sety(self, value):
        #print("sety called")
        self._y = value
    
    # Python thing that allows you to call these properties with self.y
    y = property(gety, sety, "The 'y' property.")
    

    # Set the all_agents.
    def set_all_agents(self, value):
        self.all_agents = value
     
        
    #function to calculate distance between first instance and agents.     
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
                

    # Function to get agents to interact with neighbours. 
    def share_with_neighbours(self, neighbourhood):
        # Loop through agents in self.agents
        for agent in self.all_agents:
            # Calculate distance betwwen self and current other agent.
            dist = self.distance_between(agent)
            # If distance is less than or equal to neighbourhood.
            if dist <= neighbourhood:
                # Sum first instance of agents store with other agent store.
                sum = self.store + agent.store
                # Calculate average of two agents store.
                ave = sum/2
                # Assign self.store and agent.store the averages. 
                self.store = ave
                agent.store = ave
                # Print a string with result. 
                print("Agents are " + str(dist) + " apart. With a store of" + str(ave))
     
    





"""    # Get distance between self and provided agent.
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5

"""      



    
"""use property attribute for getter and setter functionality. This means that 
     _x and _y can be called using self.x and self.y. By default Python dosen't
     alter anything with a _before and _ it, property enables this."""       
  
                
        
