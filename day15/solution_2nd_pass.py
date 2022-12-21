class Point():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def manhattan_distance(self, other):
        diff = self - other
        return sum((abs(diff.x), abs(diff.y)))


def GetSensors(input):
    sensor_beacon: dict[Point, Point] = {}
    for line in input:
        line = line.replace("\n", "").replace("Sensor at ", "").replace(
            " closest beacon is at ", "").replace('x=', '').replace('y=', '').replace(':', ',')
        sx, sy, bx, by = eval(line)
        sensor_beacon[Point(sx, sy)] = Point(bx, by)
    return sensor_beacon


class SensorGrid():
    def __init__(self, sensor_beacon: dict[Point, Point]) -> None:
        self.sensor_beacon = sensor_beacon
        self.sensor_range = {s: b.manhattan_distance(
            s) for s, b in self.sensor_beacon.items()}
        self.beacons = set(sensor_beacon.values())
        self.sensors = set(sensor_beacon.keys())

        max_distance = max(self.sensor_range.items(), key=lambda x: x[1])[1]
        self.min_x = self.min_y = self.max_x = self.max_y = 0
        for s, b in self.sensor_beacon.items():
            self.min_x = min([self.min_x, s.x, b.x])
            self.max_x = max([self.max_x, s.x, b.x])
            self.min_y = min([self.min_y, s.y, b.y])
            self.max_y = max([self.max_y, s.y, b.y])

        self.min_x -= max_distance
        self.min_y -= max_distance
        self.max_y += max_distance
        self.max_x += max_distance

    def getRangesForRow(self, row: int) -> list:
        # get sensors with vertical distance smaller or equal to manhattan
        close_sensors = {s: r for s,
                         r in self.sensor_range.items() if abs(s.y - row) <= r}

        intervals: list[list] = []  # store start and end x for each sensor
        for s, max_rng in close_sensors.items():
            vert_dist_to_row = abs(s.y - row)
            max_x_vector = (max_rng - vert_dist_to_row)
            start_x = s.x - max_x_vector
            end_x = s.x + max_x_vector
            intervals.append([start_x, end_x])

        intervals.sort()
        ranges = []
        ranges.append(intervals[0])

        for interval in intervals[1:]:
            # Check for overlapping intervals
            if ranges[-1][0] <= interval[0] <= ranges[-1][-1]:
                ranges[-1][-1] = max(ranges[-1][-1], interval[-1])
            else:
                ranges.append(interval)

        return ranges

    def getPointsOutsideScanArea(self, xyDistressLimit: int) -> Point:
        for sensor, manhattan in self.sensor_range.items():
            for dx in range(manhattan+2):  # max distress x is manhattan + 1
                # from formula distress beacon x+y = manhattan+1
                dy = (manhattan+1) - dx

                # north east west south ranges
                for sign_x, sign_y in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    x = sensor.x + (dx * sign_x)
                    y = sensor.y + (dy * sign_y)

                    # if not in boundary, try next dx and dy
                    if not (0 <= x <= xyDistressLimit
                            and 0 <= y <= xyDistressLimit):
                        continue

                    # get all disallowed intervals
                    ranges = self.getRangesForRow(y)
                    # look for a gap between any intervals
                    if len(ranges) > 1:
                        for i in range(1, len(ranges)+1):
                            if ranges[i][0] > ranges[0][1] + 1:
                                x = ranges[i][0] - 1
                                return Point(x, y)
        return None


def GetInputList(path):
    data = []
    with open(path) as file:
        for line in file:
            data.append(line)
    return data


##############################################################################################################


input = GetInputList('day15/input.txt')
sensors = GetSensors(input)
grid = SensorGrid(sensors)

# Part 1
ROW = 2000000
ranges = grid.getRangesForRow(ROW)
count = sum(r[1]-r[0]+1 for r in ranges)
beacons = sum(1 for b in grid.beacons if b.y == ROW)
print("Part1 ", count-beacons)

# Part 2
xyDistressLimit = 4000000
beacon = grid.getPointsOutsideScanArea(xyDistressLimit)
print("Part2 ", beacon.x * xyDistressLimit + beacon.y)
