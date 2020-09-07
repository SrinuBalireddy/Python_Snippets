# Conway'a Game of life

import random,copy,time
width  = 60
height = 20

#creating a list of list for the cells
nextcells=[]
for x in range(width):
    column=[] #create a new column
    for y in range(height):
        if random.randint(0,1)==0:
            column.append('#') #Add a living cell
        else:
            column.append(' ') #Add a dead cell
    nextcells.append(column) #nextcells is a list of column lists

print(nextcells)

"""
while True: #Main program loop
    print('\n\n\n\n\n') #Seperate each step with new line
    currentcells = copy.deepcopy(nextcells)
    #Print currentcells on screen
    for y in range(height):
        for x in range(width):
            print(currentcells[x][y],end='') #print the # or space
        print() #print a new line at the end of the row

 """
