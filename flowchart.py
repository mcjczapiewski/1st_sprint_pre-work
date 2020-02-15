i = 0
numbers = []


def compare(j):
    if numbers[j] > numbers[j + 1]:
        numbers[j + 1], numbers[j] = numbers[j], numbers[j + 1]


def append(user):
    for n in user:
        if not n == ",":
            numbers.append(int(n))


user_numbers = input("Hi! Give me some numbers, serapated by comma: ")
append(user_numbers)
N = len(numbers)

print(numbers)

while i < N - 1:
    j = 0
    while j < N - i - 1:
        compare(j)
        j += 1
    i += 1

print(numbers)
