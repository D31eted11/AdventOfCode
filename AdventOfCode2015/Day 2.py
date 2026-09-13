totalSquare = 0


with open("Day2Input.txt") as f:
    for line in f.readlines():
        brokenLine = line.split("x")
        length = int(brokenLine[0])
        width = int(brokenLine[1])
        height = int(brokenLine[2])
        a = length*width
        b = width*height
        c = length*height
        d = min(a, b, c)
        area = (2*a) + (2*b) + (2*c) + d
        totalSquare += area
print(totalSquare)