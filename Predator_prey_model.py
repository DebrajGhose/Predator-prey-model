# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 01:32:44 2017
"""




from pylab import *
import random
import matplotlib.animation as manimation

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
        sharkstarve[i,j] = sharkstarve[a,b] #baby shark still needs food. Without this condition, shark population can continue to thrive after fish are dead
        sharkmove[i,j]=time #baby shark does not move
        totalsharks[time] = totalsharks[time]+1

 
############################
############################

def is_shark_starving():
    
    global size, timesteps, sharks, fish, sharkmove, fishmove, time, i, j, totalsharks ,totalfish, sharkspawn, fishspawn , sharkstarve, sharkfamished
    
    if sharkstarve[i,j] >= sharkfamished:
        
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
        
        doneeating = 0 #shark has not yet eaten
        donemoving = 0 #shark has spawned
        
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
            
            doneeating = 1 #indicate that the shark has finished feeding
            
        


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

                spawn_shark(nearby[count,0] , nearby[count,1]) #see if shark is mature to spawn
                
                donemoving = 1

                break

            

                
            
    #if shark has still  not been able to move at all in this time step, simply increase its age
    
    
    if doneeating == 0 and donemoving == 0: #if shark has not moved at all
        
        sharks[i,j] = sharks[i,j] + 1
        sharkstarve[i,j] = sharkstarve[i,j] + 1 #shark gets a little hungrier

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

# a function to make a matrix that represents the location of the fish and the sharks, to be used to make a movie frame of their locations

def eco_frame():
    
    global sharks, fish, size
    
    gridnew = zeros((size,size))
    for a in range(0,size):
        for b in range(0,size):
            
            if sharks[a,b] > -1:
                
                gridnew[a,b] = 200 #set some value for the shark color

            if fish[a,b] > -1:
                
                gridnew[a,b] = 100 #set some value to color fish
                
    return gridnew
	   






#--------------------------------------
#simulation parameters
#--------------------------------------

seed() #define seed


#using global variables for most things because 1) definitions remian same across functions 2) easy readability

global size, timesteps, sharks, fish, sharkmove, fishmove, time, i, j, totalsharks ,totalfish, sharkspawn, fishspawn , sharkstarve, sharkfamished


size = 35 #size of domain
timesteps = 150 #runtime fo the program

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
fishspawn = 1 #age at which fish spawns
sharkfamished = 2 #if shark does not get food within this time, it dies

totalsharks = [0.0]*timesteps #keep track of number of sharks and fish
totalfish = [0.0]*timesteps

totalsharks[0] = 70 #initial number of sharks
totalfish[0] = 400 #initial number of fish

#place sharks

sharkleft = totalsharks[0]

while sharkleft > 0:
    
    a = int(round(rand()*(size-1))) ; b = int(round(rand()*(size-1))); #indices where you place fish  
    
    if (sharks[a,b] == -1):
        sharks[a,b] = 0
        sharkleft = sharkleft-1

fishleft = totalfish[0] #keeping track of how many fish I have left to place
       
#place fish
    
while fishleft > 0:
    
    a = int(round(rand()*(size-1))) ; b = int(round(rand()*(size-1))); #indices where you place fish      
    
    if (sharks[a,b] == -1) and (fish[a,b]==-1):
        fish[a,b] = 0
        fishleft = fishleft-1 #count down till all fish are placed on the grid
        
#generate matrix that keeps track of when shark has last eaten

sharkstarve = np.copy(sharks)



#--------------------------------------
#run simulation
#--------------------------------------

#set up animation parameters

FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib',comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)
fig = plt.figure()

with writer.saving(fig, "Sharkmovie.mp4", timesteps):

    for time in range(1,timesteps):
        #keep track of time
        print time
    
    	#start with number fo sharks and fish from previous timestep
    
        totalsharks[time] = totalsharks[time-1]
        totalfish[time] = totalfish[time-1]
    
    
    
        for i in range(0,size):
        	
            for j in range(0,size):
                
                #shark behavior
                if (sharks[i,j]>-1) and (sharkmove[i,j] < time ):
                    
                    sharks[i,j] = sharks[i,j]+1 #make shark older
                    
                    #function to see if shark dies (if it's dying, may as well die before it mover or procreates)
                    
                    is_shark_starving()
                    
                    #function to move shark/eat fish and reproduce
                    
                    move_and_spawn_shark()
                    
                    
                if fish[i,j]>-1:
                    
                    #make fish older
                    
                    fish[i,j] = fish[i,j] + 1
                    
                    #function to move fish and make them spawn
                    
                    move_and_spawn_fish()
                    
        print 'gridding'
        ecosystem = eco_frame()
        print('Generating frame')
        imshow( ecosystem, interpolation='none', cmap = 'viridis' ) 
        clim(0,200)
        writer.grab_frame()
            


plt.figure(2)                
plot(totalsharks,label='Predators')
plot(totalfish,label='Prey')
xlabel('Time steps')
ylabel('Number of animals')

legend()

plt.figure(3)
plot(totalsharks,totalfish)
xlabel('Number of Sharks')
ylabel('Number of Fish')
savefig('Predator_prey_phase_output.pdf')

