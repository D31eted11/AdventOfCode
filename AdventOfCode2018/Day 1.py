def part1():
    count = 0
    with open("Day1Input.txt", "r") as f:
        for line in f:
            operator = line[0]
            number = int(line[1:])
            if operator == '+':
                count += number
            else:
                count -= number
        print(count)

part1()