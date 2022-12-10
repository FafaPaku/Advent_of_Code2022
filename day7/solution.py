def GetInputList(path):
    data = []
    with open(path) as file:

        for line in file:
            data.append(line.replace("\n",""))
        return data

def GetTreeAtPath(tree, path):
    return tree if not path else GetTreeAtPath(tree[path[0]], path[1:])

def GetTree(input):
    path = [] #tacker
    tree = {}
    for line in input:
        split = line.split()
        currentTree = GetTreeAtPath(tree, path)
        
        if split[0].isdigit():
            currentTree[split[1]] = int(split[0])
        elif split[1] == "cd":
            if (directory := split[2]) == "..":
                path.pop()
            else:
                currentTree[directory] = {}
                path.append(directory)
    return tree        

def GetDirSize(tree, sizes):
    directorySize = 0
    for key, value in tree.items():
        if isinstance(value, int):
            fileSize = value
            directorySize += fileSize
        else:
            subdirectorySize, subSizes = GetDirSize(tree[key], sizes)
            directorySize += subdirectorySize
    sizes.append(directorySize)
    return directorySize, sizes


def part1(input):
    tree = GetTree(input)
    totalSize, sizes = GetDirSize(tree, [])
    return sum([size for size in sizes if size < 100000])


def part2(input):
    tree = GetTree(input)
    totalSize, sizes = GetDirSize(tree, [])
    return min([size for size in sizes if size > 30000000 - (70000000 - max(sizes))])

#input = GetInputList("day7/inputTest.txt")
input = GetInputList("day7/input.txt")   
print(part1(input))
print(part2(input))