from random import randint


##world = ["*********",
##         "*-------*",
##         "*-------*",
##         "*********"]
##
##for line in world:
##    print(line)


#world = [ [1,1,1,1,1,1,1,1], [1, 0, 0 , 0

def createLevel():

    width = randint(10, 40)
    height = randint(10, 25)

    level = []

    level.append("#"*width)
    
    for i in range(1, height-1):

        line = "#" + "."*(width - 2) + "#"
    
        
        level.append(line)

    level.append("#"*width)
##
##    stairX = 2
##    stairY = 4

    stairX = randint(1, width-1)
    stairY = randint(1, height-1)
    
    level[stairY] = level[stairY][:stairX] + "u" + level[stairY][stairX+1:]

    
    
    
    return level


theLevel = createLevel()

for line in theLevel:
    print(line)
