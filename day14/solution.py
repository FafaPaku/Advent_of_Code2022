def GetInputList(path):
    data = []
    with open(path) as file:

        for line in file:
            array = line.replace("\n", "")
            data.append(array)
        return data


def CreateOccupied(input):
    occupied = []
    for line in input:
        p = [eval(i) for i in line.split(' -> ')]
        occupied.extend(p)
        for i in range(len(p)-1):
            # same row
            between = [(p[i][0], y) for y in range(
                min(p[i][1], p[i+1][1])+1, max(p[i][1], p[i+1][1])) if p[i][0] == p[i+1][0]]
            occupied.extend(between)
            # same column
            between = [(x, p[i][1]) for x in range(
                min(p[i][0], p[i+1][0])+1, max(p[i][0], p[i+1][0])) if p[i][1] == p[i+1][1]]
            occupied.extend(between)
    return occupied


def PourSand(input, infiniteFloor):
    occupied = CreateOccupied(input)

    counter = 0
    if not infiniteFloor:
        maxY = max((y for (x, y) in occupied))
    else:
        maxY = max((y for (x, y) in occupied))+2
        minX = min((x for (x, y) in occupied))
        maxX = max((x for (x, y) in occupied))
        for i in range(minX-1000, maxX+100):
            occupied.append((i, maxY))

    x, y = 500, 0
    while True:
        if (x, y) in occupied:  # new pour
            x, y = 500, 0
        if not infiniteFloor and y > maxY:  # in the void
            break
        if (x, y + 1) not in occupied and y < maxY + 1:  # go deeper
            y += 1
        elif (x - 1, y + 1) not in occupied and y < maxY + 1:  # shift lower left
            x -= 1
            y += 1
        elif (x + 1, y + 1) not in occupied and y < maxY + 1:  # shift lower right
            x += 1
            y += 1
        else:  # we stopped
            counter += 1
            occupied.append((x, y))

        if infiniteFloor and (x, y) == (500, 0):  # filled up
            break
    print('At Rest: ', counter)


input = GetInputList('day14/input.txt')
PourSand(input, False)
PourSand(input, True)
