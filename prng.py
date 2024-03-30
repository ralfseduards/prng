#!/usr/bin/env python3

"""
A Pseudo Random Number Generator (PRNG) - takes a seed and calculates the next numbers
using a math function
"""

from utils import *     # the utils file

def main() -> None:
    argv = sys.argv
    argc = len(argv)

    @dataclass
    class Flags:
        """ A class for keeping track of flags. """
        time:bool = 0
        fast:bool = 0
        show_seed:bool = 0

    flags = Flags()

    # check for help flag
    if (("-h" in argv) or ("--help" in argv)):
        print_help()

    # parse flags
    for i in range(1, argc):
        match argv[i]:
            case "-f" | "--fast":
                flags.fast = 1
            case "-s" | "--seed":
                flags.show_seed = 1
            case "-t" | "--time":
                flags.time = 1
            case _:
                print("There is an unrecognized flag in your input", file=sys.stderr)
                print("Run the program with -h or --help flags.", file=sys.stderr)
                return


    # run fast (no user input, no printing intermediary)
    if (flags.fast):
        run_fast()

    # get seed
    if (flags.time):
        seed = time.time_ns()
        print("You are using the TIME flag! Your seed will be the current UNINX epoch in miliseconds.")
        if (flags.show_seed):
            print(f"Seed: {seed}")
        else:
            print("Seed: XXXXXX")
    else:
        if (flags.show_seed):
            seed = safe_input("\nInput your seed number (will show on stdin): ")
        else:
            seed = safe_input("\nInput your seed number (invisible because of missing -s flag): ", secure=True)

    # get the number of iterations 
    iter = safe_input("\nInput the number of iterations: ")
    while iter <= 0:
        iter = safe_input("Itearations have to be >= 1! Choose your number: ")
    
    # do you want to see the intermediary numbers?
    intermediary = safe_input("\nDo you want to see the intermediary numbers(1 or 0): ")
    while intermediary not in (1, 0):
        intermediary = safe_input("Wrong input, input 1 or 0: ")
    print("")

    # running the genarator
    random_number = linear(seed=seed, iterations=iter, print_values=intermediary)
    print_green_return(random_number)
    
if __name__ == "__main__":
    main()