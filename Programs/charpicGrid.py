# Write your code here :-)
grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]

for x in range(len(grid[0])):
    for y in range(len(grid)):
        print(grid[y][x], end='')
        """
        if y == len(grid)-1:
            print(sep='')
        y+=1
    x+=1
    """
    print(' ')



#####

lst = [0,1,2,3,4,5,6,7,8,9]

print(lst[0::3])

print([x for i,x in enumerate(lst) if i%3 == 0])

def newlst():
    for i,x in enumerate(lst):
            if i%3: continue
            yield x

print(list(newlst()))
