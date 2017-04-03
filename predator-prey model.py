from pylab import *
import math 
import random

def move(i,j,fish,shark): #find a neighbourhood for the fish or shark to move
    neighbour = 0
    x=[0.0]*4
    y=[0.0]*4
    if i==0:
        i1=size-1
    else:
        i1=x-1
    if (fish[i1,j]==0)and(shark[i1,j]==0):
        x[neighbour]=i1
        y[neighbour]=j
        neighbour = neighbour+1
    if i==size-1:
        i2=0
    else:
        i2=i+1
    if (fish[i2,j]==0)and(shark[i2,j]==0):
        x[neighbour]=i2
        y[neighbour]=j
        neighbour = neighbour+1
    if j==0:
        j1=size-1
    else:
        j1=j-1
    if (fish[i,j2]==0)and(shark[i,j2]==0):
        x[neighbour]=i
        y[neighbour]=j1
        neighbour = neighbour+1  
    if j==size-1:
        j2=0
    else:
        j2=j+1
    if (fish[i,j2]==0)and(shark[i,j2]==0):
        x[neighbour]=i
        y[neighbour]=j2
        neighbour = neighbour+1
    a=random.randint(0,neighbour)
    a=a-1
    return(x[a],y[a])
    
#----------------------------------
#               MAIN
#----------------------------------    

nsteps=100
shark_number=[0.0]*nsteps
fish_number=[0.0]*nsteps
size=100
#read the parameter of systems
shark_number[0]= input('inital number of shark:')
fish_number[0]= input('intial number of fish:')
procreate= input('time steps for fish and shark to procreate:')
starvation= input('time steps for shark to die of starvation:')

#define and initialize the grid
fish = zeros((size,size))
shark = zeros((size,size))
for i in range(size):
    for j in range(size):
        fish[i,j]=-1
        shark[i,j]=-1
        
fishmove = zeros((size,size))
sharkmove = zeros((size,size))
sharkstarve = zeros((size,size))


fishnumber = 0
while fishnumber<fish_number[0]:
    x=int(100*random.random())
    y=int(100*random.random())
    if fish[x,y]==-1:
        fish[x,y]=0
        fishnumber=fishnumber+1

sharknumber = 0
while sharknumber<shark_number[0]:
    x=int(100*random.random())
    y=int(100*random.random())
    if (shark[x,y]==-1)and(fish[x,y]==-1):
        shark[x,y]=0
        sharknumber=sharknumber+1

#prcess by each timestep
for t in range (timesteps):
    for i in range(size):
        for j in range(size):
            if (fish[i,j]>-1)and (fishmove[i,j]==t):  
                x,y = move(i,j,fish,shark) #find a neighbourhood for the fish to move
                fish[x,y]=fish[i,j]+1
                fishmove[x,y]=t+1
                fish[i,j]=-1
                fishmove[i,j]=0
                if fish[x,y]==procration:
                    fish[i,j]=0
                    fishmove[i,j]=t+1
                    fish[x,y]=0
                    fish_number[t+1]=fish_number[t]+1
                    
            if (shark[i,j]>-1)and (sharkmove[i,j]==t):
                x,y,food=prey(i,j,fish)
                if food==1:
                    shark[x,y]=shark[i,j]+1
                    sharkmove[x,y]=t+1
                    sharkstarve[x,y]=0
                    shark[i,j]=-1
                    sharkmove[i,j]=0
                    fish[x,y]=-1
                    fishmove[x,y]=0
                    fish_number[t+1]=fish_number[t]-1               
                    else:
                        x,y = move(i,j,fish,shark)
                        shark[x,y]=shark[i,j]+1
                        sharkmove[x,y]=t+1
                        sharkstarve[x,y]=sharkstarve[i,j]+1
                        shark[i,j]=-1
                        
                if sharkstarve[x,y]==starvation:
                    shark[x,y]=-1
                    shark_number[t+1]=shark[number]-1
                    else if shark[x,y]=procreator:
                        shark[i,j]=0
                        sharkmove[i,j]=t+1
                        sharkstarve[i,j]=0
                        
                    