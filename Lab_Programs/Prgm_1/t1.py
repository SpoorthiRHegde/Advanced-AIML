#importing necessary libraries
import random
import time
# Intialize the height and width of the table
W,H=5,5
    
#Intialize the obstacles ,tasks,agent
obstacles={(1,1),(2,4),(3,4)}
tasks={(0,2),(2,1),(3,0)}
agent=(0,0)
i=0
#fuction to check if its valid move
def valid(x,y):
    #Validate if the move is within grid and not obstacles
    return 0<=x<W and 0<=y<H and (x,y) not in obstacles
   
#function to display
def show():
    for y in range(H):
        #Intialize the row
        row=""
        #Check the each possible instance in that loaction
        for x in range(W):
            #If the current loaction is the agent the display A
            if (x,y)==agent: row+="A "
            #If the current loaction is the task the display T
            elif (x,y) in tasks: row+="T "
            #If the current loaction is the Obstacles the display O
            elif (x,y) in obstacles: row+="X "
            #If the location is empty print .
            else: row+=". "
        #print the current row
        print(row)
    #Go to new line
    print()
    time.sleep(1)

#Perform 50 steps    
for step in range(50):
    #display the current status of the board
    show()
    #Validate if the agent has picked up tha task at that point
    if agent in tasks:
        print(f"Picked task at {agent}\n")
        #Removing the task from the loaction once picked up
        tasks.remove(agent)
        if not tasks:break
    else:
        x,y = agent
        #Find the next possible moves for the agent
        moves = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        #Shuffle the next possible moves randomly
        random.shuffle(moves)
        #validate each move 
        for m in moves:
            #If next move valid then move to that loaction
            if valid(*m): agent = m; break