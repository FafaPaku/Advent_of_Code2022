TestString = "bvwbjplbgvbhsrlpgdmjqwftvncz"

def GetInputList(path):
    with open(path) as f:
        return f.read()

def GetMarker(s, r):
    i = 1
    while i < len(s)-(r-1):
        current = s[i:i+r]
        if(len(set(current)) == len(current)):
            return i+r
        i+=1
    return -1

message = GetInputList("day6/input.txt")
packetLength = 4
messageLength = 14

print(GetMarker(message, packetLength))
print(GetMarker(message, messageLength))
# 1920
# 2334
