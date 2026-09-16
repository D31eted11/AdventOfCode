
def part1():
    count = 0
    number = 0
    with open('Day1input.txt') as f:
        lines = f.readlines()
        for l in lines:
            int1 = int(lines[number])
            for line in lines:
                total = int1 + int(line[count])
                if total == 2020:
                    print(int1)
                    print(line[count])
                else:
                    print(total)
                    count += 1
            number+=1



part1()