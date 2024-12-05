import os, re

print("\n========== INPUT FILE ==========")

input = []
for line in open('input.txt'):
    input.append(line.replace("\n",""))
print("Input: " + str(input) + "\n")

print("\n========== Part 1 ==========")

sum = 0
for line in input:
    for e in re.findall("mul\([0-9]+,[0-9]+\)",line):
        nums = e[4:-1].split(",")
        if len(nums[0]) < 4 or len(nums[1]) < 4:
            sum += int(nums[0]) * int(nums[1])

print(sum)
