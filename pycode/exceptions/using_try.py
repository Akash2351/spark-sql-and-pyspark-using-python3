import random
import sys

try:
    print(f"Received first argument {sys.argv[1]}")
    args = sys.argv
    random.shuffle(args)
    print(f" Random argument {args[0]}")
except (IndexError, KeyError) as err:
    print(f"Error: no arguments, please provide at least one ({err})")
except NameError as ne:
    print(f"Error: random module not loaded: {ne}")
else:
    print(" else is running")
finally:
    print(" in finally")


