# AOC day1 - 2 number better solution
import time

def find_two_numbers(input_list, sum):
    input_list.sort()

    nf = 0
    nl = len(input_list) - 1

    while nf<nl:
        if input_list[nf] + input_list[nl] == sum:
            return input_list[nf] * input_list[nl]
        if input_list[nf] + input_list[nl] > sum:
            nl = nl - 1
        else:
            nf = nf + 1

input_file = []

with open("input.txt") as numbers:
    for num in numbers:
        input_file.append(int(num))
sum = 2020

init_time = time.time_ns()
solution = find_two_numbers(input_file, sum)
finish_time = time.time_ns()

print(solution)
print(f"computed in {finish_time-init_time}ns")
