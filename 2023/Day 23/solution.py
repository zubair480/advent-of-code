import sys
from typing import List, Tuple
from collections import defaultdict
from datetime import datetime

Coord = Tuple[int, int]

def parse_input(input_str: str) -> List[List[str]]:
    return [list(line) for line in input_str.strip().split('\n')]

def dfs(pos: Coord, trails: List[List[str]], visited: set) -> int:
    x, y = pos
    if y == len(trails[0]) - 1:
        return 0
    else:
        possible = []
        if trails[x][y] == '.':
            possible = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        elif trails[x][y] == '>':
            possible = [(0, 1)]
        elif trails[x][y] == '<':
            possible = [(0, -1)]
        elif trails[x][y] == '^':
            possible = [(-1, 0)]
        elif trails[x][y] == 'v':
            possible = [(1, 0)]

        count = 0
        for dx, dy in possible:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= len(trails) or ny >= len(trails[0]):
                continue
            if trails[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                count = max(count, 1 + dfs((nx, ny), trails, visited))
                visited.remove((nx, ny))

        return count

def part1(trails: List[List[str]]) -> int:
    start = datetime.now()

    # Set a higher recursion limit
    sys.setrecursionlimit(10**6)

    result = max(dfs((0, y), trails, set()) for y in range(len(trails[0])))

    print(f"Part 1: {result}")
    print(f"> Time elapsed is: {datetime.now() - start}")
    return result

if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        input_str = file.read()

    trails = parse_input(input_str)
    part1(trails)
    
