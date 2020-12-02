# AOC day1 - 3 numbers horrible solution
import time

def find_two_numbers(input_list, sum):
    input_list.sort()

    nf = 0
    nl = len(input_list) - 1

    while nf<nl:
        nm = nf + 1
        max_sum = input_list[nf] + input_list[nl]
        #print(f"O:{input_list[nf]} {input_list[nl]} {max_sum}")
        while nm<nl:
            cur_sum = input_list[nf] + input_list[nm] + input_list[nl]
            #print(f"I:{input_list[nf]} {input_list[nm]} {input_list[nl]} {max_sum}")
            if cur_sum == sum:
                return input_list[nf] * input_list[nm] * input_list[nl]
            nm = nm + 1
            if cur_sum > max_sum:
                max_sum = cur_sum
        if max_sum >= sum:
            nl = nl - 1
        else:
            nf = nf + 1
            nl = len(input_list) - 1

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
