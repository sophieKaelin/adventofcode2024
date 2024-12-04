import os

print("\n========== INPUT FILE ==========")

lineA, lineB = [], []

for line in open('input.txt'):
    x = line.split("   ")
    lineA.append(int(x[0]))
    lineB.append(int(x[1]))

print("Input1: " + str(lineA) + "\nInput2: " + str(lineB) + "\n")

print("\n========== Part 1 ==========")

# print("Part 1: " + str(sum(lineA)-sum(lineB)) + "\n") # Why does this not work?

lineA.sort()
lineB.sort()
total = 0
for x in range(1000):
    total += abs(lineA[x] - lineB[x])

print(total)

print("\n========== Part 2 ==========")

d = {i:lineB.count(i) for i in lineB}

total = 0
for x in lineA:
    if x not in d:
        continue
    total += x * d[x]
print(total)
