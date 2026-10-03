level = 0
count = 0
with open("level.txt") as file: #opens levels text file
    string = file.read()
    print(string)
    broken = [*string]
    print(broken)
    for char in broken:
        count += 1
        if char == "(": #if "(" increase count
            level += 1
        else: #else its ")" and count decreases
            level -= 1
        if level == -1: #breaks when count is -1
            break

print(count)
print(level)
