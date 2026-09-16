
def part1():
    totalSquare = 0
    with open("Day2Input.txt") as f:
        for line in f.readlines():
            brokenLine = line.split("x")
            length = int(brokenLine[0])
            width = int(brokenLine[1])
            height = int(brokenLine[2])
            a = length * width
            b = width * height
            c = length * height
            d = min(a, b, c)
            area = (2 * a) + (2 * b) + (2 * c) + d
            totalSquare += area
    print(totalSquare)

def part2():
    totalFeet = 0
    with open("Day2Input.txt") as f:
        for line in f.readlines():
            brokenLine = line.split("x")
            length = int(brokenLine[0])
            width = int(brokenLine[1])
            height = int(brokenLine[2])
            d = max(length, width, height)
            feet = (2*length + 2*width + 2*height) - (2*d)
            bow = length * width * height
            totalFeet += feet + bow
    print(totalFeet)

part1()
part2()