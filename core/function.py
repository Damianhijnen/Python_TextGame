import sys
import re
import time

def inpInt(inp):
    inp = re.sub("[^0-9]", "", inp)
    if inp != "":
        return int(inp)
    else:
        return 0
#test()
def sInput(msg):
    nobreak_line(msg)
    return input(" ")


def nobreak_line(inp):
    for letter in inp:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)

def line(inp):
    for letter in inp:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)
    print("")