import io
import sys
import os

# MODULO
n = 1
for i in reversed(range(100, 1000)):
    if n <= 25 and (i % 7 == 0 or i % 9 == 0):
        print(i)
        n += 1


# THE GREATEST COMMON DIVISOR
try:
    sys.argv[1] == int(sys.argv[1])
    sys.argv[2] == int(sys.argv[2])
    remaining = ""
    a, b = first, second = int(sys.argv[1]), int(sys.argv[2])
    while not remaining == 0:
        remaining = a % b
        a, b = b, remaining
    print(
        "The greatest common divisor of "
        + str(first)
        + " and "
        + str(second)
        + " is: "
        + str(a)
    )
except (IndexError, ValueError):
    print("Specify two integers in command line to calculate the divisor.")


# ANAGRAMS
script_path = os.path.dirname(os.path.normpath(__file__))
try:
    if "." in sys.argv[1]:
        anagram_file = os.path.join(script_path, sys.argv[1])
        anagram_bank = []
        printed = []
        with io.open(anagram_file, "r", encoding="utf-8") as anagrams:
            print("WORK IN PROGRESS...")
            for line in anagrams:
                word = line.split("\n")[0]
                for item in anagram_bank:
                    if (
                        (item + " " + word) in printed
                        or (word + " " + item) in printed
                        or word == item
                    ):
                        continue
                    if len(word) == len(item):
                        if all(i in item for i in word) and all(
                            j in word for j in item
                        ):
                            printed.append(word + " " + item)
                anagram_bank.append(word)
        counter = 1
        for item in sorted(printed):
            print(str(counter) + "\t" + item)
            counter += 1
except IndexError:
    pass
