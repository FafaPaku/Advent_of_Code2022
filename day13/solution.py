import functools

def GetInputList(path):
    data = []
    with open(path) as file:

        for line in file:
            array = line.replace("\n", "")
            data.append(array)
        return data


def CompareHelp(left, right):
    if (left == right):
        return 0
    if (left < right):
        return -1
    return 1


def ComparePackets(left, right):
    result = 0
    for i in range(min(len(left), len(right))):                             
        match isinstance(left[i], list), isinstance(right[i], list):        
            case True, True: result = ComparePackets(left[i], right[i])     #If both values are lists
            case True, False: result = ComparePackets(left[i], [right[i]])  #If exactly one value is an integer, convert the integer to a list
            case False, True: result = ComparePackets([left[i]], right[i])  #If exactly one value is an integer, convert the integer to a list
            case _: result = CompareHelp(left[i], right[i])                 #If both values are integers, the lower integer should come first

        if result: #If equivalent, 0, skip... we want to coninue
            return result

    return CompareHelp(len(left), len(right))                               #If the left list runs out of items first we are good


def GetSumRightOrder(input):
    sum = 0
    idx = 1
    for i in range(len(input)):
        if (i % 3 == 0):
            left = eval(input[i])
            right = eval(input[i+1])
            print('Index', idx)
            print('Compare %s vs %s' % (input[i], input[i+1]))
            result = ComparePackets(left, right)
            if (result == -1):
                sum += idx
            idx += 1
            print('Result: ', result)

    print('Sum of right order:', sum)


input = GetInputList('day13/input.txt')
GetSumRightOrder(input)

input2 = []
for item in input:
    if item != '':
        input2.append(eval(item))

input2.append([[2]])
input2.append([[6]])

#https://www.geeksforgeeks.org/how-does-the-functools-cmp_to_key-function-works-in-python/
result = sorted(input2, key=functools.cmp_to_key(ComparePackets))
second = result.index([[2]]) + 1
sixth = result.index([[6]]) +1

print('Part2: ',second * sixth )
