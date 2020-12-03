# AOC day 3 - Traverse a matrix
import time

input_file = []
with open("puzzle_input.txt") as f:
    input_file = f.read().splitlines()

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

def traverse(right, down, input_file):
    x = 0
    tree_count = 0

    line_len = len(input_file[0])

    for y in range(0, len(input_file), down):
        if input_file[y][x] == "#":
            tree_count = tree_count + 1
        x = (x + right) % line_len
    print(tree_count)
    return tree_count

init_time = time.time_ns()
tree_count = 1
for x, y in slopes:
    tree_count *= traverse(x, y, input_file)
finish_time = time.time_ns()

print(tree_count)
print(f"computed in {finish_time-init_time}ns")

