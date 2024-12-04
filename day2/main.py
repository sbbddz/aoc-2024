file = open("input.txt", "r")
input = file.read().split("\n")
input.pop()

def is_safe(a):
    safe = True

    for i in range(0, len(a)-1):
        diff = abs(a[i] - a[i+1])
        if diff >= 1 and diff <= 3:
            continue
        else:
            safe = False
            break

    diffs = []
    for i in range(0, len(a)-1):
        diff = a[i] - a[i+1]
        diffs.append(diff > 0)

    if len(set(diffs)) > 1:
        safe = False

    if safe:
        return True
    else:
        return False

safe_count = 0
for value in input:
    a = list(map(int, value.split(" ")))
    if is_safe(a):
        safe_count = safe_count + 1
    else:
        for i in range(0, len(a)):
            b = a.copy()
            b.pop(i)
            if is_safe(b):
                safe_count = safe_count +1
                print("safe by removing: " + str(a[i]) + " " + str(a))
                break

print("==============")
print(safe_count)
print("==============")
