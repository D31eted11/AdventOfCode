def part1():
    row = 0
    collum = 0
    with open("Day3Input.txt") as f:
        content = f.read()
        split = [*content] #break string into values
        print(len(split))
        for char in content:
            if char == ">": #counts how wide the grid needs to be
                collum += 1
            elif char == "v": #counts how long grid needs to be
                row += 1
        grid = [[0 for i in range(collum)] for j in range(row)] #creates grid with exact values
        startRow = int(row/2) #calcs midpoint of grid
        startCollum = int(collum/2)
        for char in content: #walk through text file moving in appropriate direction setting value to 1
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

        number = sum(row.count(1) for row in grid) + 1 #counts number of 1 and adds starting 1
        print(number)



part1()