def part1():
    grid = [[0 for i in range(1000)] for j in range(1000)]
    with open("Day6Input.txt") as f:
        for row in f:
          instruction = row.split(" ")
          print(instruction)


part1()