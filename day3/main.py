import math
import re

file = open("input.txt", "r")
input = file.read().split("\n")
input = "".join(input)

# part1
parsed = list(re.findall("mul\\(\\d+,\\d+\\)", input))

sum = 0
for i in parsed:
    res = list(map(int, re.findall("\\d+", i)))
    sum += math.prod(res)

print(sum)

# part2
parsed = list(re.findall("mul\\(\\d+,\\d+\\)|do\\(\\)|don't\\(\\)", input))

sum = 0
enabled = True
for i in parsed:
    if "don't" in i:
        enabled = False
    elif "do" in i:
        enabled = True
    else:
        if enabled:
            res = list(map(int, re.findall("\\d+", i)))
            sum += math.prod(res)

print(sum)
