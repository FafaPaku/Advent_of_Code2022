def GetInputList(path):
    data = []
    with open(path) as file:

        for line in file:
            data.append(line.replace("\n",""))
        return data

# print(ord('a')- 96)
# print(ord('z')- 96) 
# print(ord('A') - 64+26)
# print(ord('Z')- 64+26) 
def priority(x):
    if x.islower() :
        return ord(x)- 96
    else:
        return ord(x) - 64+26

# Yield successive n-sized
# chunks from l.
def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

# reading file
data = GetInputList("day3/input.txt")

#part 1
Sum = 0
for r in data:
    firstpart = r[:len(r)//2]
    secondpart  = r[len(r)//2:]
    
    a=list(set(firstpart)&set(secondpart))
    Sum += (sum(list(map(priority, a))))
print(Sum)

#part2
Sum2 = 0
n = 3
x = list(divide_chunks(data, n))
for i in x:
    a=list(set(i[0])&set(i[1])&set(i[2]))
    Sum2 += (sum(list(map(priority, a))))
print(Sum2)
#8018
#2518