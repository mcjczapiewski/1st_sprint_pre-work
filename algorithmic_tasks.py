import sys

# MODULO
# n = 1
# for i in reversed(range(100, 1000)):
#     if n <= 25 and (i % 7 == 0 or i % 9 == 0):
#         print(i)
#         n += 1

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
