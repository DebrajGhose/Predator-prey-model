# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 01:32:44 2017
"""




from pylab import *
import random

#-----------------------------
#Functions go here
#-----------------------------
 
def nearby_cells(i,j,size): #generates a matrix of nearby cells with Moore's neighborhood
    
    nearby = [0,0] #nearx and neary will contain indices of nearby cells
    for m in range(-1,2):
        for n in range(-1,2):
            
            if not (m == 0 and n == 0): #ignore the point i,j
            
                newrow = [ (j+m)%size , (i+n)%size] #j (column) controls x axis and i (row) controls y
                nearby = vstack([nearby, newrow])
                                
    nearby = delete(nearby, (0), axis=0)
    
    #shuffle nearby cells!
    
    random.shuffle(nearby)
    
    return nearby


def move_and_spawn_shark():
    
    #global variables
    
    
    global size, timesteps, sharks, fish, sharkmove, fishmove, time, i, j, totalsharks ,totalfish, sharkspawn, fishspawn
    
    
    if sharkmove[i,j] < time: #make sure shark has not already moved in this timestep
        
        
        #find nearby cells
        
        nearby = nearby_cells(i,j,size) #remember that this matrix is already shuffled so no need to worry about randomzing directions adn stuff later!
        
        #see if there are any fish nearby
        
        for count in range(0,8):
            
            if fish[ nearby[count,0] , nearby[count,1] ] > -1 :
                
                
                sharks[nearby[count,0] , nearby[count,1]] = sharks[i,j] + 1 #shark eats fish and ages
                sharks[i,j] = -1 #no shark in this spot anymore
                
                fish[nearby[count,0] , nearby[count,1]] = -1 #fish gets eaten, awww
                totalfish[time] = totalfish[time] - 1 #how many fish are eaten from previous timestep
    
                sharkmove[nearby[count,0] , nearby[count,1]] = time
                
                break
    
    
        #if no fish, move into empty spot
        
        if sharks[i,j] > -1: #if the shark has not moved to eat fish
            
            for count in range(0,8):
                
                if sharks[ nearby[count,0] , nearby[count,1] ] == -1: #look for empty spots
                    
                    sharks[nearby[count,0] , nearby[count,1]] = sharks[i,j] + 1 #move shark and increase its age
                    
                    sharks[i,j] = -1
    
                    sharkmove[nearby[count,0] , nearby[count,1]] = time
    
                    break
                
        #if shark has not been able to move at all in this time step, simply increase its age
        
        if sharks[i,j]>-1:
            
            sharks[i,j] = sharks[i,j] + 1
                
        #if shark has moved out of its current spot and is old enough, it is safe to reproduce            
        
        if (sharks[ nearby[count,0] , nearby[count,1] ]> sharkspawn) and (sharks[i,j] < 0):
            
            sharks[[ nearby[count,0] , nearby[count,1] ]] = 0 #reset shark ages to 0
            sharks[i,j] = 0
        
            totalsharks[time] = totalsharks[time] + 1
        
        




#--------------------------------------
#simulation parameters
#--------------------------------------

seed() #define seed


#using global variables for most things because 1) definitions remian same across functions 2) easy readability

global size, timesteps, sharks, fish, sharkmove, fishmove, time, i, j, totalsharks ,totalfish, sharkspawn, fishspawn


size = 10 #size of domain
timesteps = 100 #runtime fo the program

#sharks holds locations and ages of all sharks
#fish holds locations and ages of all fish

sharks = np.zeros((size,size)) - 1 #-1 means no fish, anything higher is the age of the fish
fish = np.zeros((size,size)) - 1

#sharkmove keeps track of whether you have already moved a shark in a given timestep
#fishmove keeps track of whether you have already moved a fish in a given timestep

sharkmove = zeros((size,size))
fishmove = zeros((size,size))

#-------------------------------------------------------------
# parameters for shark and fish
#--------------------------------------------------------------
sharkspawn = 10 #age at which shark spawns
fishspawn = 5 #age at which fish spawns

#----------------------------------------------------------------------
#generate sharks and fish on matrix without overlapping shark and fish
#----------------------------------------------------------------------

genshark = 20.0/size**2 #determines approximate number of sharks generated
genfish = 20.0/size**2 #determines approxiamte number of fish generated

for i in range(0,size): #iterated through all cells in the matrix
    
    for j in range(0,size):
        
        if rand() < genshark: #toss coin to insert shark
            sharks[i,j] = 0
        
        elif rand() < genfish: #if you don't insert shark, toss coin to insert fish
            fish[i,j] = 0    


totalsharks = [0.0]*timesteps
totalfish = [0.0]*timesteps

totalsharks[0] = sum(sharks+1)
totalfish[0] = sum(fish+1) #calculates total sharks/fish at initial timepoint, this hack works because the matrix has only -1s and 0s. Don't use this method for later timesteps

#--------------------------------------
#run simulation
#--------------------------------------

for time in range(1,timesteps):
    
    #start with number fo sharks and fish from previous timestep
    
    totalsharks[time] = totalsharks[time-1]
    totalfish[time] = totalfish[time-1]
    
    
    
    for i in range(0,size):
        for j in range(0,size):
            
            #shark behavior
            
            if sharks[i,j]>-1:
                
                
                #function to see if shark dies (if it's dying, may as well die before it mover or procreates)
                
                
                #function to move shark/eat fish and reproduce
                
                
                    move_and_spawn_shark()
                
                
            if fish[i,j]>-1:
                
                
                #function to see if fish dies (if it's dying, may as well die before it mover or procreates)
                
                
                #function to see if fish is ready to reproduce
                
                
                #function to move fish
                
                a=2 #dummy script; delet later on
                
