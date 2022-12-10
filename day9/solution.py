def GetInputList(path):
    data = []
    with open(path) as file:

        for line in file:
            array = line.replace("\n", "")
            data.append(array)
        return data

def MoveCloser(h,k):
    if abs(h[0]-k[0])<=1 and abs(h[1]-k[1])<=1:
        return k
    for i in [0,1]:
        if h[i]-k[i]>0: # to the right or down
            k[i]+=1
        elif h[i]-k[i]<0: # to the left or up
            k[i]-=1
    return k

input = GetInputList('day9/input.txt')
tracker=[]
#knots=2
knots=10

rope=[[0,0] for i in range(knots)]

for steps in input:
    direction = steps.split(' ')[0]
    step = int(steps.split(' ')[1])
    for i in range(step):
        h=rope[0]
        if direction=="R":
            h[1]+=1 
        elif direction=="L":
            h[1]-=1 
        elif direction=="U":
            h[0]-=1 
        elif direction=="D":
            h[0]+=1 
        for idx in range(1,knots):
            rope[idx]=MoveCloser(rope[idx-1],rope[idx])    
        tracker.append(','.join([str(x) for x in rope[-1]]))

print(len(set(tracker)))
