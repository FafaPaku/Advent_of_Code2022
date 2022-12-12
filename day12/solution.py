from collections import defaultdict


def GetInputList(path):
    data = []
    with open(path) as file:

        for line in file:
            array = line.replace("\n", "")
            data.append(array)
        return data

def GetLetter(input, x, y):
    letter = input[y][x]
    return letter.replace('S', 'a').replace('E', 'z')

def GetCord(input, letter):
    for y in range(len(input)):
        line = input[y]
        if (x := line.find(letter)) > -1:
            return str(x)+'|'+str(y)

def GetACords(input):
    letters = []
    for y in range(len(input)):
        for x in range(len(input[0])):
            letter = GetLetter(input, x, y)
            if (letter == 'a'):
                letters.append(str(x)+'|'+str(y))
    return letters



# Python3 implementation to build a
# graph using Dictionaries
# Function to build the graph


def build_graph(input):

    edges = []

    # loop each node and add to
    graph = defaultdict(list)

    maxX = len(input[0])
    maxY = len(input)
    for y in range(maxY):
        for x in range(maxX):
            # check left
            if (x+1 < maxX):
                if (ord(GetLetter(input, x+1, y)) - ord(GetLetter(input, x, y)) <= 1):
                    graph[str(x)+'|'+str(y)].append(str(x+1)+'|'+str(y))
            # check right
            if (x-1 >= 0):
                if (ord(GetLetter(input, x-1, y)) - ord(GetLetter(input, x, y)) <= 1):
                    graph[str(x)+'|'+str(y)].append(str(x-1)+'|'+str(y))
            # check up
            if (y-1 >= 0):
                if (ord(GetLetter(input, x, y-1)) - ord(GetLetter(input, x, y)) <= 1):
                    graph[str(x)+'|'+str(y)].append(str(x)+'|'+str(y-1))
            # check down
            if (y+1 < maxY):
                if (ord(GetLetter(input, x, y+1)) - ord(GetLetter(input, x, y)) <= 1):
                    graph[str(x)+'|'+str(y)].append(str(x)+'|'+str(y+1))

    return graph

# def GetLetter(input, x, y):
#     letter = input[y][x]
#     return letter.replace('S','a').replace('E','z')

# Python implementation to find the
# shortest path in the graph using
# dictionaries

# Function to find the shortest
# path between two nodes of a graph


def BFS_SP(graph, start, goal):
    explored = []

    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]

    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return

    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    #print("Shortest path = ", *new_path)
                    #print(len(new_path)-1)
                    return len(new_path)-1
            explored.append(node)

    # Condition when the nodes
    # are not connected
    print("So sorry, but a connecting"
          "path doesn't exist :(")
    return


input = GetInputList('day12/input.txt')
graph = build_graph(input)
SCord = GetCord(input, 'S')
ECord = GetCord(input, 'E')

# print(graph)
# Function Call
min = BFS_SP(graph, SCord, ECord)
print(min)

aCords = GetACords(input)
print(aCords)
for aCord in aCords:
    current = BFS_SP(graph, aCord, ECord)
    if(isinstance(current, int)):
        if(current < min): min = current

print(min)