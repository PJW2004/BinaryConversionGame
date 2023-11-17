import os
import random
import getopt
import sys
import time

def random_decimal(max_num: int = 10):
    """
    decimal data from random choice
    """
    return random.choice(range(max_num))

LEVEL_BINARY = "binary"
LEVEL_HEXADECIMAL = "hexadecimal"

def covert_binary(decimal: int):
    return format(decimal, "016b")

def covert_hexadecimal(decimal: int):
    return format(decimal, "016x")

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def running(max_num: int, level: str, running_range: int):
    start_time = time.time()

    correct_count = 0
    incorrect_list = []

    for idx in range(1, running_range + 1):
        clear_screen()
        print("-" * 100)
        print(f"Question {idx}/{running_range}: What is the decimal equivalent?")
        
        decimal = random_decimal(max_num)
        if level == LEVEL_BINARY:
            question = covert_binary(decimal)
        elif level == LEVEL_HEXADECIMAL:
            question = covert_hexadecimal(decimal)
        
        user_answer = input(f"{question} = ")

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("[Error] Please enter a valid integer.")
            input("Press Enter to continue...")
            continue

        if user_answer != decimal:
            print("[System] [Incorrect Answer]")
            incorrect_list.append((question, user_answer))
            input("Press Enter to exit...")
            sys.exit(0)
        
        print("[System] [Correct Answer]")
        correct_count += 1
        input("Press Enter to continue...")

    end_time = time.time()

    clear_screen()
    print(f"[Done] [Total play time: {start_time} ~ {end_time}]")
    print(f"Correct Answers: {correct_count}/{running_range}")
    if incorrect_list:
        print("Incorrect Answers:")
        for question, user_answer in incorrect_list:
            print(f"{question} = {user_answer}")
    print("-" * 100)
    print()

if __name__ == "__main__":
    USAGE = """\
Usage: main.py [options] type

Options:
    --help      / -h       -- print this message and exit
    --max_num   / -m       -- maximum number
    --level     / -l       -- binary or hexadecimal
    --range     / -r       -- running range
"""

    def usage(code, msg=''):
        print(USAGE)
        if msg:
            print(msg)
        sys.exit(code)

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hm:l:r:", ["help", "max_num=", "level=", "range="])
    except getopt.error as msg:
        usage(1, msg)

    level = "binary"
    max_num = 1
    running_range = 0

    try:
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                usage(0)
            elif opt in ("-l", "--level"):
                level = arg
            elif opt in ("-m", "--max_num"):
                max_num = int(arg)
            elif opt in ("-r", "--range"):
                running_range = int(arg)
    except Exception as e:
        usage(1, f"{e.__class__.__module__}.{e.__class__.__name__} : {e.args[0]}")

    assert isinstance(max_num, int), usage(1, "max_num is not an integer")
    assert isinstance(level, str), usage(1, "level is not a string")
    assert level in {"binary", "hexadecimal"}, usage(1, "level is not in type binary or hexadecimal")

    running(max_num, level, running_range)
