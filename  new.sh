#!/bin/bash

if [ "$#" -lt 2 ] || [ "$#" -gt 3 ]; then
    echo "Usage: $0 <YEAR> <DAY> [PYTHON_FILENAME]"
    exit 1
fi

YEAR=$1
DAY=$2
PYTHON_FILE=${3:-solution.py}

DIR="$YEAR/$DAY"
mkdir -p "$DIR"
touch "$DIR/input.txt"
touch "$DIR/example_1.txt"

cat <<EOF > "$DIR/$PYTHON_FILE"
from util.decorators import aoc_timed_solution

@aoc_timed_solution($YEAR, $DAY, 1)
def run_part1(filename):
    pass

@aoc_timed_solution($YEAR, $DAY, 2)
def run_part2(filename):
    pass

if __name__ == '__main__':
    run_part1("example_1.txt")
    # run_part1("input.txt")
    # run_part2("example_1.txt")
    # run_part2("input.txt")
EOF

echo "Directory and files created for Advent of Code $YEAR Day $DAY."