def GetInputList(path):
    data = []
    with open(path) as file:

        for line in file:
            array = line.replace("\n", "")
            data.append(array)
        return data

def GetSignalStrength(input, c):
    register = 1
    cycle= 1
    for item in input:
        myList = item.split(" ")
        if (len(myList) == 1 and myList[0] == 'noop'):
            cycle+=1
            if(cycle == c):
                return register * c
        elif (len(myList) == 2 and myList[0] == 'addx'):
            cycle+=1
            if(cycle == c):
                return register * c
            register += int(myList[1])
            cycle+=1
            if(cycle == c):
                return register * c
    return 1

def DrawPixel(screen, register, xPosition, yPosition):
    r = register
    if(xPosition >= r-1 and xPosition <= r+1):
        screen[xPosition][yPosition] = '#'
    else:
        screen[xPosition][yPosition] = '.'
    return screen

def GetNextPixel(xPosition,yPosition):
    xPosition = (xPosition+1)%40
    if(xPosition == 0): 
        yPosition = (yPosition+1)%6
    return xPosition,yPosition
    
def GetDrawScreen(input, screen):
    register = 1
    cycle= 1
    xPosition = 0
    yPosition = 0
    for item in input:
        myList = item.split(" ")
        if (len(myList) == 1 and myList[0] == 'noop'):
            screen = DrawPixel(screen, register, xPosition, yPosition)
            xPosition, yPosition = GetNextPixel(xPosition,yPosition)
            cycle+=1
        elif (len(myList) == 2 and myList[0] == 'addx'):
            screen = DrawPixel(screen, register, xPosition, yPosition)
            xPosition, yPosition = GetNextPixel(xPosition,yPosition)
            cycle+=1

            screen = DrawPixel(screen, register, xPosition, yPosition)
            xPosition, yPosition = GetNextPixel(xPosition,yPosition)
            register += int(myList[1])
            cycle+=1
    screen.reverse()
    return  screen


def GetTotalSignalStregth(input, myList):
    total = 0
    for item in myList:
        total += GetSignalStrength(input, item)
    return total

input = GetInputList('day10/input.txt')
cycles = [20,60,100,140,180,220]
print(GetTotalSignalStregth(input, cycles))

screen =  [[] for i in range(40)]
for i in range(40):
    for j in range(6):
        screen[i].append('')
     
word = GetDrawScreen(input, screen)
for w in word:
    print(*w)

