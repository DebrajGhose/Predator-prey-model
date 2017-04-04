# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 01:32:44 2017
"""




from pylab import *


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
    return nearby


def move_shark(i,j,sharks,fish,sharkmove,fishmove,size):
    
    #find nearby cells
    
    nearby = nearby_cells(i,j,size)
    
    print nearby
    
    #see if there are any fish nearby
    
    fishnearx = []; fishneary = [];



    #if no fish see how many empty spots there are
    
    #choose an empty spot to move into

    
    


#--------------------------------------
#simulation parametres
#--------------------------------------

seed() #define seed

size = 20 #size of domain
timesteps = 100 #runtime fo the program

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

genshark = 40.0/size**2 #determines approximate number of sharks generated
genfish = 40.0/size**2 #determines approxiamte number of fish generated

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
    
                    move_shark(i,j,sharks,fish,sharkmove,fishmove,size)
                
                
            if fish[i,j]>-1:
                
                
                #function to see if fish dies (if it's dying, may as well die before it mover or procreates)
                
                #function to see if fish is ready to reproduce
                
                #function to move fish
                
                a=2
        