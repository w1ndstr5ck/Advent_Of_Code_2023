
file1 = open("Input1_1.txt", "r")
lines = file1.readlines()

total = 0
for line in lines:
    for char in line:
        if char.isdigit():
            start = char
            break
        else:
            continue
    for char in reversed(line):
        if char.isdigit():
            last = char
            break
        else:
            continue
    combined = start + last
    total += int(combined)

print(total)