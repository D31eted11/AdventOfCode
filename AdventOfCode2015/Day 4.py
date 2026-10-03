import hashlib
import numbers


def part1(): #find the 1st MDF hash thats starts with X5 0's
    flag = False
    count = 0
    secretKey = "yzbqklnj"
    while flag == False: #keep iterating till value found
        newKey = secretKey + str(count)
        res = hashlib.md5(newKey.encode()).hexdigest() #encrypt created key
        brokenKey = res[0:5] #takes first 5 digits
        if brokenKey == "00000": #checks if 1st 5 are 0
            print(count)
            flag = True
        else:
            count += 1

def part2(): #find first 6 this time
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