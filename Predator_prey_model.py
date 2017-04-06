# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 01:32:44 2017
"""




from pylab import *
import random

#-----------------------------
#Functions go here
#-----------------------------

################################
#################################

def spawn_shark(a,b):
    #shark will only spawn if it has already moved
    global size, timesteps, sharks, fish, sharkmove, fishmove, time, i, j, totalsharks ,totalfish, sharkspawn, fishspawn , sharkstarve, sharkfamished
    
    #see if shark is mature enough to spawn
    if sharks[a,b] > sharkspawn:
        #reset shark ages if it spawns
        sharks[a,b]=0
        sharks[i,j]=0 #create new shark
        sharkmove[i,j]=time #baby shark does not move
        sharkstarve[i,j]=0 #baby shark starts afresh
        totalsharks[time] = totalsharks[time]+1

 
############################
############################

def is_shark_starving():
    
    global size, timesteps, sharks, fish, sharkmove, fishmove, time, i, j, totalsharks ,totalfish, sharkspawn, fishspawn , sharkstarve, sharkfamished
    
    if sharkstarve[i,j] > sharkfamished:
        
        sharks[i,j] = -1
        sharkstarve[i,j] = -1
        sharkmove[i,j] = -1
        totalsharks[time] = totalsharks[time]-1


    


##########################
##########################

def nearby_cells(): #generates a matrix of nearby cells with Moore's neighborhood
    global i,j, size
    #create an array containing Moore neighbors

    nearby = array([ [(i-1)%size,j] , [(i-1)%size,(j+1)%size] , [(i)%size,(j+1)%size] , [(i+1)%size,(j+1)%size] , [(i+1)%size,(j)%size] , [(i+1)%size,(j-1)%size] , [(i)%size,(j-1)%size] , [(i-1)%size,(j-1)%size]        ])

    #shuffle nearby cells!
    
    np.random.shuffle(nearby)
    
    return nearby


    
#############################
#############################    
    
    
    
def move_and_spawn_shark():
    
    #global variables
    
    
    global size, timesteps, sharks, fish, sharkmove, fishmove, time, i, j, totalsharks ,totalfish, sharkspawn, fishspawn , sharkstarve, sharkfamished

  
    #find nearby cells
    
    nearby = nearby_cells() #remember that this matrix is already shuffled so no need to worry about randomzing directions  later!
    
    #see if there are any fish nearby
    
    for count in range(0,8): 
        #cycle through nearby cells (these cells have been shuffled, so the choice is random)
        
        if fish[ nearby[count,0] , nearby[count,1] ] > -1 :
            
            #see if shark has reached reproductive age
            
            sharks[nearby[count,0] , nearby[count,1]] = sharks[i,j] #shark eats fish and moves
            sharks[i,j] = -1 #no shark in this spot anymore
            
            sharkstarve[nearby[count,0] , nearby[count,1]] = 0 #shark is full!
            sharkstarve[i,j] = -1 #there is no shark here


            fish[nearby[count,0] , nearby[count,1]] = -1 #fish gets eaten, awww
            totalfish[time] = totalfish[time] - 1 #lower total fish when fish get eaten

            sharkmove[nearby[count,0] , nearby[count,1]] = time

            spawn_shark(nearby[count,0] , nearby[count,1])
            
            doneteating = 1
            
        else:
            
            doneeating = 0
            


            break


    #if no fish, move into empty spot
    
    if doneeating==0: #if the shark has not moved to eat fish
        
        for count in range(0,8):
            
            if sharks[ nearby[count,0] , nearby[count,1] ] == -1: #look for empty spot
                
                sharks[nearby[count,0] , nearby[count,1]] = sharks[i,j] #move shark
                sharks[i,j] = -1                    
                
                sharkstarve[nearby[count,0] , nearby[count,1]] = sharkstarve[i,j] + 1 #shark gets a little hungrier
                sharkstarve[i,j] = -1 #there is no shark here

                

                sharkmove[nearby[count,0] , nearby[count,1]] = time

                spawn_shark(nearby[count,0] , nearby[count,1])

                break

            

                
            
    #if shark has still  not been able to move at all in this time step, simply increase its age
    
    if sharks[i,j] > -1:
        
        sharks[i,j] = sharks[i,j] + 1

########################################
########################################

def move_and_spawn_fish():
    
    #global variables
    
    
    global size, timesteps, sharks, fish, sharkmove, fishmove, time, i, j, totalsharks ,totalfish, sharkspawn, fishspawn , sharkstarve, sharkfamished

  
    #find nearby cells
    
    nearby = nearby_cells() #remember that this matrix is already shuffled so no need to worry about randomzing directions  later!
    

    
    for count in range(0,8):
        
        if (sharks[ nearby[count,0] , nearby[count,1] ] == -1) and (fish[ nearby[count,0] , nearby[count,1] ] == -1): #look for empty spot
            
            fish[nearby[count,0] , nearby[count,1]] = fish[i,j] #move fish
            fish[i,j] = -1                    
           
            fishmove[nearby[count,0] , nearby[count,1]] = time

            spawn_fish(nearby[count,0] , nearby[count,1])

            break


########################################
########################################

def spawn_fish(a,b):
    #shark will only spawn if it has already moved
    global size, timesteps, sharks, fish, sharkmove, fishmove, time, i, j, totalsharks ,totalfish, sharkspawn, fishspawn , sharkstarve, sharkfamished
    
    #see if fish is mature enough to spawn
    if fish[a,b] > fishspawn:
        #reset fish ages if it spawns
        fish[a,b]=0
        fish[i,j]=0 #create new shark
        fishmove[i,j]=time #baby shark does not move
        
        totalfish[time] = totalfish[time]+1 #add fish

 
############################
############################      






#--------------------------------------
#simulation parameters
#--------------------------------------

seed(1) #define seed


#using global variables for most things because 1) definitions remian same across functions 2) easy readability

global size, timesteps, sharks, fish, sharkmove, fishmove, time, i, j, totalsharks ,totalfish, sharkspawn, fishspawn , sharkstarve, sharkfamished


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
sharkfamished = 6 #if shark does not get food within this time, it dies

#----------------------------------------------------------------------
#generate sharks and fish on matrix without overlapping shark and fish
#----------------------------------------------------------------------

genshark = 0/size**2 #determines approximate number of sharks generated
genfish = 10.0/size**2 #determines approxiamte number of fish generated

decount = 0

for i in range(0,size): #iterated through all cells in the matrix
    
    for j in range(0,size):
        
        #toss coin to insert shark
        if rand() < genshark: 
            
            sharks[i,j] = 0
        
         #if you don't insert shark, toss coin to insert fish
        elif rand() < genfish:
            
            fish[i,j] = 0    


totalsharks = [0.0]*timesteps
totalfish = [0.0]*timesteps

#generate matrix that keeps track of when shark has last eaten

sharkstarve = np.copy(sharks)


totalsharks[0] = sum(sharks) + size**2
totalfish[0] = sum(fish) + size**2 #calculates total sharks/fish at initial timepoint, this hack works because the matrix has only -1s and 0s. Don't use this method for later timesteps

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
            
            if (sharks[i,j]>-1) and (sharkmove[i,j] < time ):
                
                #make shark older
                
                sharks[i,j] = sharks[i,j]+1
                
                #function to see if shark dies (if it's dying, may as well die before it mover or procreates)
                
                is_shark_starving()
                
                #function to move shark/eat fish and reproduce
                
                
                move_and_spawn_shark()
                
                
            if fish[i,j]>-1:
                
                #make fish older
                
                fish[i,j] = fish[i,j] + 1
                
                #function to move fish and make them spawn
                
                move_and_spawn_fish()
                
plot(totalsharks)
plot(totalfish)
