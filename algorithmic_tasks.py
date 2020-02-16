import re
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


# PRESENT PARTICIPLE
try:
    if "." not in sys.argv[1]:
        str(sys.argv[1].split())
        vowels = ["e", "y", "u", "i", "o", "a"]
        count = 1
        while sys.argv[count]:
            if not any(i.isdigit() for i in sys.argv[count]):
                word = sys.argv[count].lower()
                ending = re.sub(r"^.*(...)$", r"\g<1>", word)
                if word.endswith("ie"):
                    ing_word = re.sub(r"^(.+)ie$", r"\g<1>ying", word)
                elif word.endswith("c"):
                    ing_word = word + "king"
                elif (
                    (
                        ending[0] not in vowels
                        and ending[1] in vowels
                        and ending.endswith(("w", "x", "y"))
                    )
                    or word == "be"
                    or word.endswith(("ee", "ye", "oe", "nge"))
                    or (
                        ending[0] in vowels
                        and ending[1] in vowels
                        and ending[2] not in vowels
                    )
                ):
                    ing_word = word + "ing"
                elif (
                    ending[0] not in vowels
                    and ending[1] in vowels
                    and ending[2] not in vowels
                ):
                    ing_word = re.sub(
                        r"^(.+)(.)$", r"\g<1>\g<2>\g<2>ing", word
                    )
                elif ending[1] not in vowels and word.endswith("e"):
                    ing_word = re.sub(r"^(.+)e$", r"\g<1>ing", word)
                else:
                    ing_word = word + "ing"
                print(word, "-->", ing_word)
            count += 1
except (IndexError, ValueError):
    pass


# ANAGRAMS
try:
    if "." in sys.argv[1]:
        script_path = os.path.dirname(os.path.normpath(__file__))
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
