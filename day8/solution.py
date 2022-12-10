def GetInputList(path):
    data = []
    with open(path) as file:

        for line in file:
            array = [int(x) for x in [*(line.replace("\n", ""))]]
            data.append(array)
        return data


def GetScenicScore(tree, arr):
    score = 0
    for s in arr:
        if (s < tree):
            score += 1
        else:
            score += 1
            break
    if (score == 0):
        score = 1
    return score


def GetMaxRightOf(input, x, y):
    tree = int(input[x][y])
    a = input[x][y+1:]
    score = GetScenicScore(tree, a)
    return max(a, default=-1), score


def GetMaxLeftOf(input, x, y):
    tree = int(input[x][y])
    a = input[x][:y]
    a.reverse()
    score = GetScenicScore(tree, a)
    return max(a, default=-1), score


def GetMaxTopOf(input, x, y):
    tree = int(input[x][y])
    column = []
    i = 0
    while i < x:
        column.append(input[i][y])
        i += 1
    column.reverse()
    score = GetScenicScore(tree, column)
    return max(column, default=-1), score


def GetMaxBottomOf(input, x, y):
    tree = int(input[x][y])
    column = []
    i = x+1
    while i < len(input):
        column.append(input[i][y])
        i += 1
    score = GetScenicScore(tree, column)
    return max(column, default=-1), score


def IsItemVisible(input, x, y):
    tree = int(input[x][y])
    right, s1 = GetMaxRightOf(input, x, y)
    left, s2 = GetMaxLeftOf(input, x, y)
    bottom, s3 = GetMaxBottomOf(input, x, y)
    top, s4 = GetMaxTopOf(input, x, y)
    if (
        tree > right or
        tree > left or
        tree > bottom or
        tree > top):
        return True, (s1*s2*s3*s4)
    else:
        return False, (s1*s2*s3*s4)


def GetNumVisibleTrees(input):
    maxScenic = 0
    count = 0
    x = 0
    y = 0
    xMax = len(input)-1
    yMax = len(input[0])-1
    while x <= xMax:
        while y <= yMax:
            visible, scene = IsItemVisible(input, x, y)
            if (visible):
                count += 1
            if (scene > maxScenic):
                maxScenic = scene
            y += 1
        y = 0
        x += 1

    return count, maxScenic


input = GetInputList('day8/input.txt')
print(GetNumVisibleTrees(input))  # 1698, 672280
