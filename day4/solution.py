def GetInputList(path):
    data = []
    with open(path) as file:

        for line in file:
            data.append(line.replace("\n",""))
        return data

def FullyContains(r1,r2):
    r1min = int(r1.split('-')[0])
    r1max = int(r1.split('-')[1])
    r2min = int(r2.split('-')[0])
    r2max = int(r2.split('-')[1])
    return (r1min <= r2min and r1max >= r2max) or (r1min >= r2min and r1max <= r2max)

def OverlapAtAll(r1,r2):
    r1min = int(r1.split('-')[0])
    r1max = int(r1.split('-')[1])
    r2min = int(r2.split('-')[0])
    r2max = int(r2.split('-')[1])
    return max(r1min,r2min) <= min(r1max,r2max)
    # return (r1min <= r2max) and (r1max >= r2min)

# reading file
data = GetInputList("day4/input.txt")
Sum = 0
Sum2 = 0

for r in data:
    r1 = r.split(',')[0]
    r2 = r.split(',')[1]
    if(FullyContains(r1,r2)):
        Sum += 1
    if(OverlapAtAll(r1,r2)):
        Sum2 += 1
print(Sum)
print(Sum2)
# 562
# 924