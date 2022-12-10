def CreateStackTest():
    depths = [[] for i in range(3)]
    depths[0] = ['Z', 'N']
    depths[1] = ['M', 'C', 'D']
    depths[2] = ['P']
    return depths


def CreateStack():
    depths = [[] for i in range(9)]
    depths[0] = ['R', 'G', 'H', 'Q', 'S', 'B', 'T', 'N']
    depths[1] = ['H', 'S', 'F', 'D', 'P', 'Z', 'J']
    depths[2] = ['Z', 'H', 'V']
    depths[3] = ['M', 'Z', 'J', 'F', 'G', 'H']
    depths[4] = ['T', 'Z', 'C', 'D', 'L', 'M', 'S', 'R']
    depths[5] = ['M', 'T', 'W', 'V', 'H', 'Z', 'J']
    depths[6] = ['T', 'F', 'P', 'L', 'Z']
    depths[7] = ['Q', 'V', 'W', 'S']
    depths[8] = ['W', 'H', 'L', 'M', 'T', 'D', 'N', 'C']
    return depths


def moveCrates(stack, num, p1, p2):
    i = 1
    while i <= num:
        crate = stack[p1-1].pop()
        stack[p2-1].append(crate)
        i += 1


def moveCrates2(stack, num, p1, p2):
    i = 1
    temp = []
    while i <= num:
        crate = stack[p1-1].pop()
        temp.append(crate)
        i += 1
    i = 1
    while i <= num:
        crate = temp.pop()
        stack[p2-1].append(crate)
        i += 1

def GetInputList(path):
    data = []
    with open(path) as file:

        for line in file:
            data.append(list(filter(None, line.replace("\n", "").replace(
                "move", "").replace("from", "").replace("to", "").split(" "))))
        return data


data = GetInputList("day5/input.txt")
stack = CreateStack()
stack2 = CreateStack()
for d in data:
    num = int(d[0])
    p1 = int(d[1])
    p2 = int(d[2])
    moveCrates(stack, num, p1, p2)
    moveCrates2(stack2, num, p1, p2)

output = ""
for l in stack:
    l.reverse()
    output += l[0]

print(output)

output = ""
for l in stack2:
    l.reverse()
    output += l[0]

print(output)
