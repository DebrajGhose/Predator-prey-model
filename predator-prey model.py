from pylab import *
import math 
import random

def prey(i,j,fish):#find whether there is a fish in the neighbour of the shark
    neighbour = 0
    x=[0.0]*4
    y=[0.0]*4
    if i==0:
        i1=size-1
    else:
        i1=i-1
    if (fish[i1,j]>-1):
        x[neighbour]=i1
        y[neighbour]=j
        neighbour = neighbour+1
    if i==size-1:
        i2=0
    else:
        i2=i+1
    if (fish[i2,j]>-1):
        x[neighbour]=i2
        y[neighbour]=j
        neighbour = neighbour+1   
    if j==0:
        j1=size-1
    else:
        j1=j-1
    if (fish[i,j1]>-1):
        x[neighbour]=i
        y[neighbour]=j1
        neighbour = neighbour+1
    if j==size-1:
        j2=0
    else:
        j2=j+1
    if (fish[i,j2]>-1):
        x[neighbour]=i
        y[neighbour]=j2
        neighbour = neighbour+1
    if neighbour>0:
        a=random.randint(0,neighbour-1)
    else:
        a=1          
    return(x[a],y[a],neighbour)
    
def move(i,j,fish,shark): #find a neighbourhood for the fish or shark to move
    neighbour = 0
    x=[0.0]*4
    y=[0.0]*4
    if i==0:
        i1=size-1
    else:
        i1=i-1
    if (fish[i1,j]==-1)and(shark[i1,j]==-1):
        x[neighbour]=i1
        y[neighbour]=j
        neighbour = neighbour+1
        
    if i==size-1:
        i2=0
    else:
        i2=i+1
    if (fish[i2,j]==-1)and(shark[i2,j]==-1):
        x[neighbour]=i2
        y[neighbour]=j
        neighbour = neighbour+1
        
    if j==0:
        j1=size-1
    else:
        j1=j-1
    if (fish[i,j1]==-1)and(shark[i,j1]==-1):
        x[neighbour]=i
        y[neighbour]=j1
        neighbour = neighbour+1
          
    if j==size-1:
        j2=0
    else:
        j2=j+1
    if (fish[i,j2]==-1)and(shark[i,j2]==-1):
        x[neighbour]=i
        y[neighbour]=j2
        neighbour = neighbour+1
        
    if neighbour>0:
        a=random.randint(0,neighbour-1)
        return(x[a],y[a])
    else:
        return(i,j)
    
#----------------------------------
#               MAIN
#----------------------------------    

timesteps=100
shark_number=[0.0]*(timesteps+1)
fish_number=[0.0]*(timesteps+1)
fish_number1=[0.0]*(timesteps+1)
size=100
#read the parameter of systems
#shark_number[0]= input('inital number of shark:')
#fish_number[0]= input('intial number of fish:')
#procreate= input('time steps for fish and shark to procreate:')
#starvation= input('time steps for shark to die of starvation:')

shark_number[0]=50
fish_number[0]=200
procreate=20
starvation=10

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
while fishnumber<fish_number[0]: #geneate a random distribuation of fish
    x=int(size*random.random())
    y=int(size*random.random())
    if fish[x,y]==-1:
        fish[x,y]=0
        fishnumber=fishnumber+1

sharknumber = 0
while sharknumber<shark_number[0]: #generate a random distrbuation of shark
    x=int(size*random.random())
    y=int(size*random.random())
    if (shark[x,y]==-1)and(fish[x,y]==-1):
        shark[x,y]=0
        sharknumber=sharknumber+1

#prcess by each timestep
for t in range (timesteps):
    shark_number[t+1]=shark_number[t]
    fish_number[t+1]=fish_number[t]
    #fish_number1[t+1]=0
    for i in range(size):
        for j in range(size):
            
            if (fish[i,j]>-1)and (fishmove[i,j]==t):  
                #fish_number1[t+1]=fish_number[t+1]+1
                x,y = move(i,j,fish,shark) #find a neighbourhood for the fish to move    
                fish[x,y]=fish[i,j]+1
                fishmove[x,y]=t+1 
                if (x<>i)or(y<>j): #check if the fish move or be blocked at the original position
                    fish[i,j]=-1
                    fishmove[i,j]=0
                    if fish[x,y]>procreate: #check if the fish reach the age to procreate a new fish
                        fish[i,j]=0
                        fishmove[i,j]=t+1
                        fish[x,y]=0
                        fish_number[t+1]=fish_number[t+1]+1
                    
            if (shark[i,j]>-1)and (sharkmove[i,j]==t):
                x,y,food=prey(i,j,fish)
                if food>0:
                    shark[x,y]=shark[i,j]+1
                    sharkmove[x,y]=t+1
                    sharkstarve[x,y]=0
                    shark[i,j]=-1
                    fish[x,y]=-1
                    fishmove[x,y]=0
                    fish_number[t+1]=fish_number[t+1]-1               
                else:
                    x,y = move(i,j,fish,shark)
                    shark[x,y]=shark[i,j]+1
                    sharkmove[x,y]=t+1
                    sharkstarve[x,y]=sharkstarve[i,j]+1
                    if (x<>i)or(y<>j):        #to check if shark moves or be blocked in the same place
                        shark[i,j]=-1  
                          
                if sharkstarve[x,y]==starvation: #check whether shark will die of starvation
                    shark[x,y]=-1
                    shark_number[t+1]=shark_number[t+1]-1
                if (shark[x,y]>procreate)and((x<>i)or(y<>j)):
                    shark[i,j]=0
                    sharkmove[i,j]=t+1
                    sharkstarve[i,j]=0
                    shark[x,y]=0
                    shark_number[t+1]=shark_number[t+1]+1  

#generate the figure  
plt.plot(fish_number,label='fish number')
plt.plot(shark_number,label='shark number')
plt.xlabel('evolution time')
plt.ylabel('number of animal')
plt.show()
plt.savefigure('predator-prey Model.jepg')