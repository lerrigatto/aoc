# AOC day 3 - Traverse a matrix
import time

input_file = []
with open("puzzle_input.txt") as f:
    input_file = f.read().splitlines()

# Traverse pattern is 3r, 1d

x = 0
tree_count = 0

# two options
#for line in input_file:
#    pos = (pos + 3) # use %
#    if line[pos] == '#'

init_time = time.time_ns()
line_len = len(input_file[0])

for y in range(0, len(input_file)):
    # print(f"{y},{x} {input_file[y][x]}")
    if input_file[y][x] == "#":
        tree_count = tree_count + 1
    x = (x + 3) % line_len

finish_time = time.time_ns()

print(tree_count)
print(f"computed in {finish_time-init_time}ns")

