
file1 = open("Input1_1.txt", "r")
lines = file1.readlines()

total = 0

for line in lines:
    line = line.replace("one", "o1e")
    line = line.replace("two", "t2o")
    line = line.replace("three", "t3ee")
    line = line.replace("four", "f4ur")
    line = line.replace("five", "f5ve")
    line = line.replace("six", "s6x")
    line = line.replace("seven", "s7ven")
    line = line.replace("eight", "e8ght")
    line = line.replace("nine", "n9ne")
    line = line.replace("one", "o1e")
    line = line.replace("two", "t2o")
    line = line.replace("three", "t3ee")
    line = line.replace("four", "f4ur")
    line = line.replace("five", "f5ve")
    line = line.replace("six", "s6x")
    line = line.replace("seven", "s7ven")
    line = line.replace("eight", "e8ght")
    line = line.replace("nine", "n9ne")
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