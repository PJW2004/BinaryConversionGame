import random
import getopt
import sys

def random_decimal(max_num: int = 10):
    """
    decimal data from random choice
    """
    return random.choice(range(max_num))

def running(max_num: int, level: str, running_range: int):
    print(random_decimal(max_num))

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
        if msg: print(msg)
        sys.exit(code)

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hm:l:r:", ["help", "max_num=", "level=", "range="])
    except getopt.error as msg:
        usage(1, msg)

    level         = "binary"
    max_num       = 1
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

    assert isinstance(max_num, int), usage(1, "max_num is not integer")
    assert isinstance(level, str), usage(1, "level is not string")
    assert level in {"binary", "hexadecimal"}, usage(1, "level is not in type binary or hexadecimal")

    running(max_num, level, running_range)
