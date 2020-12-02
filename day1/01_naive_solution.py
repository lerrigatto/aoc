# AOC day1 - 2 number naive solution
import time

def find_two_numbers(input_list, sum):

    for n1 in input_list:
        for n2 in input_list:
            if n1+n2 == sum:
                return n1*n2

input_list = [
            1721,
            979,
            366,
            299,
            675,
            1456]

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
