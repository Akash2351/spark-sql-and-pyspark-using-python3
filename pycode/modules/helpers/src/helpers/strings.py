# modules are just like files.. we can import them in other files.

__all__ = ['extract_lower', 'extract_upper']

def extract_upper(phrase):
    """
    extract_upper takes a string and return a list containing
    only the uppercase characters from the string.

    >>> extract_upper("Hello There, BOB")
    ['H', 'T', 'B', 'O', 'B']
    """
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    return list(filter(str.islower, phrase))

if __name__ == '__main__':
    print(f"Hello from strings..run only if this script is run")