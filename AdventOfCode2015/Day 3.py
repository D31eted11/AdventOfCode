def part1():
    row = 0
    collum = 0
    count = 0
    debug = 0
    with open("Day3Input.txt") as f:
        content = f.read()
        split = [*content]
        print(len(split))
        for char in content:
            if char == ">":
                collum += 1
            elif char == "v":
                row += 1
        grid = [[0 for i in range(collum)] for j in range(row)]
        startRow = int(row/2)
        startCollum = int(collum/2)
        for char in content:
            if char == ">":
                startCollum += 1
                grid[startRow][startCollum] =  1
            elif char == "v":
                startRow += 1
                grid[startRow][startCollum] =  1
            elif char == "<":
                startCollum -= 1
                grid[startRow][startCollum] = 1
            elif char == "^":
                startRow -= 1
                grid[startRow][startCollum] = 1

        number = sum(row.count(1) for row in grid) + 1
        print(number)



part1()