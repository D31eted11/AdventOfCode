level = 0
count = 0
with open("level.txt") as file:
    string = file.read()
    broken = [*string]
    for char in broken:
        count += 1
        if char == "(":
            level += 1
        else:
            level -= 1
        if level == -1:
            break

print(count)
print(level)
