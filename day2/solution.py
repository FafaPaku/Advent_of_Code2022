def GetInputList(path):
    data = []
    with open(path) as file:

        for line in file:
            data.append(line.replace("\n",""))
        return data

def outcome(a,b):
    bonus = 0
    game = 0
    if b == "A": 
        bonus = 1
    if b == "B": 
        bonus = 2
    if b == "C": 
        bonus = 3
    if a == b:
        game = 3
    elif (a+b == "CA") or (a+b == "BC") or (a+b == "AB"):
        game = 6
    return game+bonus

def outcome2(a,b): # A-Rock B-Paper C -Scissors
    c = a
    if b == "X": #lose
        if a == "A":
            c = "C"
        if a == "B":
            c = "A" 
        if a == "C":
            c = "B"           
        return outcome(a,c)
    if b == "Y": #draw
        return outcome(a,a)
    if b == "Z": #win
        if a == "A":
            c = "B"
        if a == "B":
            c = "C" 
        if a == "C":
            c = "A"          
        return outcome(a,c)
    

cnt = 0
cnt2 = 0
# reading file
data = GetInputList("day2/input.txt")

for g in data:
    e = g.split(" ")[0]
    m = g.split(" ")[1].replace("X","A").replace("Y","B").replace("Z","C")
    m2 = g.split(" ")[1]
    cnt += outcome(e,m)
    cnt2 += outcome2(e,m2)

print(cnt)
print(cnt2)
#14297
#10498