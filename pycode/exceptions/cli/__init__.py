import sys
from .errors import ArgumentError


def main():
    if len(sys.argv) < 2:
        raise ArgumentError('not enough arguments')
    # assert len(sys.argv) >= 2, "too few argument"
    print(f"Argument is {sys.argv[1]}")
