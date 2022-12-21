import math
import sys
from multiprocessing import Process


class Sensor:
    def __init__(self, nodes):
        self.x = eval(nodes[0])[0]
        self.y = eval(nodes[0])[1]
        self.beaconx = eval(nodes[1])[0]
        self.beacony = eval(nodes[1])[1]
        self.manhattan = abs(self.x - self.beaconx) + \
            abs(self.y - self.beacony)

    def minX(self):
        return self.x - self.manhattan

    def maxX(self):
        return self.x + self.manhattan

    def shorterThanManhattan(self, x, y):
        return abs(self.x - x) + abs(self.y - y) <= self.manhattan

    def longerThanManhattan(self, x, y):
        return not self.shorterThanManhattan(x, y)

    def isBeacon(self, x, y):
        return self.beaconx == x and self.beacony == y

    def getSlice(self, y):
        dy = abs(y - self.y)
        if (dy > self.manhattan):
            return None

        dx = self.manhattan - dy
        return range(self.x - dx, self.x+dx)


def GetInputList(path):
    data = []
    with open(path) as file:

        for line in file:
            array = line.replace("\n", "").replace("Sensor at ", "").replace(
                " closest beacon is at ", "").replace('x=', '').replace('y=', '').split(':')
            data.append(array)
        return data


def Part1(y, sensors):
    minX = sys.maxsize
    maxX = 0
    for s in sensors:
        minX = min(s.minX(), minX)
        maxX = max(s.maxX(), maxX)

    count = 0
    for x in range(minX-1, maxX+1):
        for s in sensors:
            if (not s.isBeacon(x, y) and s.shorterThanManhattan(x, y)):
                count += 1
                break
    print(count)


def Part2(minX, maxX, minY, maxY, sensors):
    keepSearching = True
    cnt = 0
    for y in range(minY, maxY + 1):
        if not keepSearching:
            print('Done')
            break
        for x in range(minX, maxX + 1):
            cnt += 1
            if cnt % 100000 == 0:
                print('At x:%d * y:%d' % (x, y))
            if not keepSearching:
                break
            beconFound = False
            for s in sensors:
                if s.isBeacon(x, y):
                    beconFound = True
                    break
            if (beconFound):
                continue

            found = False
            for s in sensors:
                if (not s.isBeacon(x, y) and s.shorterThanManhattan(x, y)):
                    found = True
                    break

            if not found:
                unique = (x, y)
                keepSearching = False
                return unique, unique[0]*4000000 + unique[1]


# def FindGap(ranges, limit):
#     ordered = [r for r in ranges if set(r).intersection(limit)]
#     ordered.sort(key=min )

#     m = min(limit) - 1
#     for r in ordered:
#         if (m + 1 < min(r)):
#             return m + 1
#         m = max(m, max(r))

#     if m < max(limit):
#         return m + 1
#     else:
#         return None

# def Part2_2(xyLimit, sensors):
#     for y in range(xyLimit+1):
#         print('At ', y)
#         covered = [s.getSlice(y) for s in sensors if (s.getSlice(y) != None)]
#         gap = FindGap(covered, range(xyLimit+1))
#         if(isinstance(gap, int)):
#             print( (gap+1) * 4000000 + y)
#             break
#     pass

##############################################################################################################

input = GetInputList('day15/input.txt')
sensors = []
for item in input:
    sensor = Sensor(item)
    sensors.append(sensor)

# y = 2_000_000 #change here
# Part1(y, sensors)

minX = minY = sys.maxsize
maxX = maxY = 0
for s in sensors:
    minX = min(minX, s.x)
    maxX = max(maxX, s.x)
    minY = min(minY, s.y)
    maxY = max(maxY, s.y)
#print(minX, maxX, minY, maxY)
# xyLimit = 4_000_000 #change here
unique, frequency = Part2(minX, maxX, minY, maxY, sensors)
print(unique)
print(frequency)
