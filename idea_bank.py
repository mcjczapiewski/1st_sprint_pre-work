import sys
import os
import io

script_dir = os.path.dirname(os.path.abspath(__file__))
bank = os.path.join(script_dir, "my_bank.txt")
list_memory = []


def read_open(x):
    with io.open(bank, 'r', encoding='utf-8') as read_bank:
        number = 1
        for line in read_bank:
            list_memory.append(line)
            if x == 1:
                print(str(number) + '.  ' + line.split('\n')[0])
            number += 1


try:
    if sys.argv[1] == "--list":
        read_open(1)
    elif sys.argv[1] == "--delete":
        try:
            sys.argv[2] == int(sys.argv[2])
            line_to_delete = int(sys.argv[2]) - 1
            read_open(0)
            with io.open(bank, 'w', encoding='utf-8') as bank_write:
                item_number = 0
                for item in list_memory:
                    if not line_to_delete == item_number:
                        bank_write.write(item)
                    item_number += 1
            read_open(1)
        except (IndexError, ValueError):
            print("Specify an integer number after --delete")

except IndexError:
    with io.open(bank, "a", encoding="utf-8") as my_bank:
        while True:
            print("What is you new idea?")
            new_idea = input()
            my_bank.write(new_idea + "\n")
            my_bank.seek(0)
            read_open(1)
