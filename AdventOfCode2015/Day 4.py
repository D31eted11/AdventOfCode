import hashlib
import numbers


def part1():
    flag = False
    count = 0
    secretKey = "yzbqklnj"
    while flag == False:
        newKey = secretKey + str(count)
        res = hashlib.md5(newKey.encode()).hexdigest()
        brokenKey = res[0:5]
        if brokenKey == "00000":
            print(count)
            flag = True
        else:
            count += 1

def part2():
    flag = False
    count = 0
    secretKey = "yzbqklnj"
    while flag == False:
        newKey = secretKey + str(count)
        res = hashlib.md5(newKey.encode()).hexdigest()
        brokenKey = res[0:6]
        if brokenKey == "000000":
            print(count)
            flag = True
        else:
            count += 1


part1()
part2()