# modules are just like files.. we can import them in other files.

__all__ = ['extract_lower', 'extract_upper']

def extract_upper(phrase):
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    return list(filter(str.islower, phrase))

print(f"__name__ in helper: {__name__}")

if __name__ == '__main__':
    print(f"Hello from helpers..run only if this script is run")