import os

print("\n========== INPUT FILE ==========")

input = []

for line in open('input.txt'):
    input.append([int(item) for item in line.split(" ")])

print("Input: " + str(input) + "\n")

# ========== Common =========="

def checkDiff(diff, isAsc):
    return (diff < 0 and isAsc or diff > 0 and not isAsc) and abs(diff) in range(1,4)

def isSafe(report):
    # Confirm the direction.
    isAsc = True
    if report[0] > report[1]:
        isAsc = False
    # Iterate through to find level diffs
    for i in range(1, len(report)):
        diff = report[i-1] - report[i]
        if checkDiff(diff, isAsc):
            continue
        return i-1
        break
    return -1

def isSafe2(report):
    tolerated = False
    # Confirm the direction.
    isAsc = True
    if report[0] > report[1]:
        isAsc = False
    # Iterate through to find level diffs
    for i in range(1, len(report)):
        diff = report[i-1] - report[i]
        if checkDiff(diff, isAsc) or diff == 0:
            continue
        elif not tolerated and i < len(report)-1 and checkDiff(report[i-1] - report[i+1], isAsc):
            tolerated = True
            i+=1
            continue
        return i-1
        break
    return -1

print("\n========== Part 1 ==========")

safe = 0
for report in input:
    if isSafe(report) == -1:
        safe +=1

print(safe)

print("\n========== Part 2 ==========")

safe = 0

for report in input:
    if isSafe2(report) == -1:
        safe +=1

print(safe)
