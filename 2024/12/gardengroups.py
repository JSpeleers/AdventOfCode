from collections import deque

from util.decorators import aoc_timed_solution
from util.util import MOVES


def explore_area(grid, rows, cols, start_r, start_c):
    seen = set()
    queue = deque([(start_r, start_c)])
    area, perimeter = 0, 0
    boundary = {}

    while queue:
        r, c = queue.popleft()
        if (r, c) in seen:
            continue

        seen.add((r, c))
        area += 1

        for dr, dc, _ in MOVES:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == grid[r][c]:
                queue.append((nr, nc))
            else:
                perimeter += 1
                if (dr, dc) not in boundary:
                    boundary[(dr, dc)] = set()
                boundary[(dr, dc)].add((r, c))

    return area, perimeter, boundary


def calculate_sides(boundary):
    sides = 0
    for direction, positions in boundary.items():
        visited_boundary = set()

        for start_pos in positions:
            if start_pos in visited_boundary:
                continue

            sides += 1
            queue = deque([start_pos])

            while queue:
                r, c = queue.popleft()
                if (r, c) in visited_boundary:
                    continue

                visited_boundary.add((r, c))
                for dr, dc, _ in MOVES:
                    nr, nc = r + dr, c + dc
                    if (nr, nc) in positions:
                        queue.append((nr, nc))

    return sides


@aoc_timed_solution(2024, 12, 1)
def run_part1(filename):
    with open(filename) as f:
        grid = f.read().strip().split('\n')
    rows, cols = len(grid), len(grid[0])
    seen = set()
    sol = 0
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in seen:
                area, perimeter, _ = explore_area(grid, rows, cols, r, c)
                sol += area * perimeter
    return sol


@aoc_timed_solution(2024, 12, 2)
def run_part2(filename):
    with open(filename) as f:
        grid = f.read().strip().split('\n')
    rows, cols = len(grid), len(grid[0])
    seen = set()
    sol = 0
    for r in range(rows):
        for c in range(cols):
            if (r, c) in seen:
                continue

            area, perimeter, boundary = explore_area(grid, rows, cols, r, c)
            sides = calculate_sides(boundary)

            sol += area * sides
    return sol


if __name__ == '__main__':
    run_part1("example_1.txt")
    run_part1("input.txt")
    run_part2("example_1.txt")
    run_part2("input.txt")
