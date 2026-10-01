def part1():
    vowels = ['a', 'e', 'i', 'o', 'u']

    notAllowed = ['ab', 'cd', 'pq', 'xy']
    with open("Day5Input.txt") as f:
        for line in f:
            print(line)
            vowel_count = 0
            strings = [*line]
            for char in strings:
                if char in vowels:
                    vowel_count += 1

            if vowel_count >= 3:
                print(line)



part1()