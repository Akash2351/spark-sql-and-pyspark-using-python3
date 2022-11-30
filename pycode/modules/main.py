#!/usr/bin/env python3
print("Importing helpers from main")
import helpers
# import helpers as h
# from helpers import extract_lower, extract_upper
# from helpers import extract_lower as e_low, extract_upper
# from helpers import *

print("importing extras from main")
import extras

print(f"__name__ in main: {__name__}")

name = "Akash Anjanappa"
print(f"Lowercase letters: {helpers.extract_lower(name)}")
print(f"Uppercase letters: {helpers.extract_upper(name)}")