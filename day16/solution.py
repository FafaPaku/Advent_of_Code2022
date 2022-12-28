from dataclasses import dataclass
from pathlib import Path
import re
import functools

INPUT_DIR = Path(__file__).parent
INPUT_FILE = Path(INPUT_DIR, "input.txt")


@dataclass(frozen=True)
class Valve():
    id: str
    rate: int
    neighbors: set[str]



def main():
    with open(INPUT_FILE, mode="rt") as file:
        data = file.read().splitlines()

    valves = ParseInput(data)

    @functools.cache
    def GetMaxRelief(opened, mins_left, valve_id, isElephant=False):
        if mins_left <= 0:
            if isElephant:  # act as if you waited for count down to then add elephant's work
                return GetMaxRelief(opened, 26, "AA")
            else:
                return 0
        
        most_relief = 0
        valve = valves[valve_id]
        for neighbor in valve.neighbors:
            most_relief = max(most_relief, GetMaxRelief(frozenset(opened), mins_left-1, neighbor, isElephant))

        #if the rate is not zero, and the valve is not open and we have time
        if valve.rate > 0 and mins_left > 0 and valve_id not in opened:
            opened = set(opened)
            opened.add(valve_id)
            mins_left -= 1
            total_flow = mins_left * valve.rate
            for neighbor in valve.neighbors:
                most_relief = max(most_relief, total_flow+ GetMaxRelief(frozenset(opened), mins_left-1, neighbor, isElephant))

        return most_relief
    
    print("Part 1:", GetMaxRelief(frozenset(), 30, 'AA'))
    print("Part 2:", GetMaxRelief(frozenset(), 26, 'AA', True))


def ParseInput(data) -> dict[str, Valve]:
    pattern = re.compile(r"Valve ([A-Z]{2})\D+=(\d+);.+[valve]s? (.+)")
    valves = {}
    for line in data:
        valve, rate, neighbors = pattern.findall(line)[0]
        valves[valve]=Valve(valve, int(rate), {x.strip() for x in neighbors.split(',')})
    
    return valves


if __name__ == "__main__":
    main()
