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


def move_shark(i,j,sharks,fish,sharkmove,fishmove,size,time):
    
    #find nearby cells
    
    nearby = nearby_cells(i,j,size) #remember that this matrix is already shuffled so no need to worry about randomzing directions adn stuff later!
    
    #see if there are any fish nearby
    
    for count in range(0,8):
        
        if fish[ nearby[count,0] , nearby[count,1] ] > -1 :
            
            
            sharks[nearby[count,0] , nearby[count,1]] = 0 #shark eats fish and starve resets to zero
            fish[nearby[count,0] , nearby[count,1]] = -1 #fish gets eaten, awww
            sharks[i,j] = -1
            sharkmove[nearby[count,0] , nearby[count,1]] = time + 1


    #if no fish, move into empty spot
    
    if sharks[i,j] > -1: #if the shark has not moved to eat fish
        
        for count in range(0,8):
            
            if sharks[ nearby[count,0] , nearby[count,1] ] < -1:
                
                sharks[nearby[count,0] , nearby[count,1]] = sharks[i,j] + 1 #move shark and increase its age
                
                sharks[i,j] = -1

                sharkmove[nearby[count,0] , nearby[count,1]] = time + 1

                
                
    
    

    
    return sharks,fish,sharkmove


#--------------------------------------
#simulation parametres
#--------------------------------------

seed() #define seed

size = 10 #size of domain
timesteps = 10000 #runtime fo the program

#sharks holds locations and ages of all sharks
#fish holds locations and ages of all fish

sharks = np.zeros((size,size)) - 1 #-1 means no fish, anything higher is the age of the fish
fish = np.zeros((size,size)) - 1



#sharkmove keeps track of whether you have already moved a shark
#fishmove keeps track of whether you have already moved a fish 

sharkmove = zeros((size,size))
fishmove = zeros((size,size))

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


#--------------------------------------
#run simulation
#--------------------------------------

for time in range(0,timesteps):
    
    for i in range(0,size):
        for j in range(0,size):
            
            #shark behavior
            
            if sharks[i,j]>-1:
                
                
                #function to see if shark dies (if it's dying, may as well die before it mover or procreates)
                
                
                
                #function to see if shark is ready to reproduce
                
                
                
                #function to move shark/eat fish
                
                if sharkmove[i,j] == time: #make sure shark has not already moved
    
                    sharks,fish,sharkmove = move_shark(i,j,sharks,fish,sharkmove,fishmove,size,time)
                
                
            if fish[i,j]>-1:
                
                
                #function to see if fish dies (if it's dying, may as well die before it mover or procreates)
                
                
                #function to see if fish is ready to reproduce
                
                
                #function to move fish
                
                a=2 #dummy script; delet later on
                
#sharks seem to be doing their job as expected        