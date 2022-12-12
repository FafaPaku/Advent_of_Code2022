import math


def GetInputList(path):
    data = []
    with open(path) as file:

        for line in file:
            array = line.replace("\n", "")
            data.append(array)
        return data


def GetStartingItems(input):
    m = input[1::7]
    final = []
    for starting in m:
        temp = starting.replace('  Starting items: ', '').split(', ')
        itemp = [int(x) for x in temp]
        final.append(itemp)
    return final


def GetOperations(input):
    m = input[2::7]
    final = []
    for starting in m:
        temp = starting.replace('  Operation: new = old ', '').split(' ')
        final.append(temp)
    return final


def GetDivisibles(input):
    m = input[3::7]
    final = []
    for starting in m:
        temp = int(starting.replace('  Test: divisible by ', ''))
        final.append(temp)
    return final


def GetTruths(input):
    final = []
    m = input[4::7]
    for starting in m:
        temp = int(starting.replace('    If true: throw to monkey ', ''))
        final.append(temp)
    return final


def GetFalses(input):
    final = []
    m = input[5::7]
    for starting in m:
        temp = int(starting.replace('    If false: throw to monkey ', ''))
        final.append(temp)
    return final

def GetOperationInt(operation, item):
    if operation[1] == 'old':
        return item
    else:
        return int(operation[1])


def CalculateWorry(operation, item):
    v = 0
    if operation[1] == 'old':
        v = item
    else:
        v = int(operation[1])
    if (operation[0] == '*'):
        return item * v
    if (operation[0] == '/'):
        return item / v
    if (operation[0] == '+'):
        return item + v
    return item - v


def PerformRounds(rounds, input, isBored):
    monkeys = GetStartingItems(input)
    operations = GetOperations(input)
    divisibleby = GetDivisibles(input)
    truths = GetTruths(input)
    falses = GetFalses(input)
    inspected = [0]*len(monkeys)
    myLCM = math.lcm(*divisibleby)
    for _ in range(rounds):
        for m in range(len(monkeys)):
            for item in monkeys[m]:
                worry = CalculateWorry(operations[m], item)
                if (isBored):
                    worry = math.floor(worry/3)
                else:
                    worry = worry % myLCM
                if (worry % divisibleby[m] == 0):
                    monkeys[truths[m]].append(worry)
                else:
                    monkeys[falses[m]].append(worry)
                inspected[m] += 1
            monkeys[m] = []  # clear

    return inspected


input = GetInputList('day11/input.txt')
rounds = 20
inspected = PerformRounds(rounds, input, True)
print(inspected)
inspected.sort(reverse=True)
print(inspected[0]*inspected[1])

rounds = 10000
inspected = PerformRounds(rounds, input, False)
print(inspected)
inspected.sort(reverse=True)
print(inspected[0]*inspected[1])
