import sys                          # for args
import time                         # for UNIX epoch
from dataclasses import dataclass   # for dataclass "struct"
from getpass import getpass         # for hidden seed input

# ANSI colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

"""
Print the help screen
"""
def print_help() -> None:
    print("\n>>>>>>>>>>>>>>>>>>>THE PSEUDO-RANDOM NUMBER GENERATOR<<<<<<<<<<<<<<<<<<<")
    print("\nThis is the help menu\n")
    print("Some general rules: ")
    print("\t- help flags cannot be used with other flags")
    print("\t- flags can be used together (-l --time), but cannot be mixed (-lt)\n")
    print("=========================== Available commands ============================")
    print("-h, --help       open this HELP menu")
    print("-t, --time       sets the seed as the current UNIX time in miliseconds")
    print("-f, --fast       just print the random number - no seeds, no prompts")
    print("(seed is UNIX epochs/ iterations == 999 )")
    print("-s, --seed,      print the used seed on the stdout")
    print("===========================================================================")
    print("\nrlph was ere\n")
    exit()

"""
PRNG using Linear Congruential Generator which uses modular (mod) arithmatic as the "randomizer"
-   the same seed leads to the same values
-   at some point the values are going to repeat (the function has a period), because there
is a limited amount of numbers that the modulo can return

Function:  X(n+1) = (a * X(n) + c) mod m

"""
def linear(seed:int, iterations:int, print_values:bool) -> int:
    
    if iterations == 1:
        print_values = False

    prev_num:int = seed
    random_num = 0

    # the posix parameters
    a:int = 25214903917 
    c:int = 11
    m:int = 2 ** 48

    for i in range(1, iterations+1):
        random_num =  (a * prev_num + c) % m
        if print_values:
            print(f"Random number #{i}: {random_num}")
        if random_num == seed and i > 1:
            print(f"Found a period on iteration {i} !!")
            input("Press any key to continue ... ")
        prev_num = random_num
    
    return (random_num)

def print_green_return(num:int) -> None:
    print(Colors.OKGREEN + "Your random number: ", num, Colors.ENDC)


"""
Run the program fast.
(No prompts, no intermediary outputs)
"""
def run_fast() -> None:
    random_num = linear(time.time_ns(), 999, False)
    print_green_return(random_num)
    exit()

"""
An input that catches a ValueError if the user doesnt provide an int.
"""
def safe_input(message:str, secure=False) -> int:
    try:
        if (secure):
            user_in = int(getpass(message))
        else:
            user_in = int(input(message))
    except ValueError:
        print(Colors.FAIL + "--> ValueError: the input can only contain ints!", Colors.ENDC)
        exit()
    else:
        return (user_in)
