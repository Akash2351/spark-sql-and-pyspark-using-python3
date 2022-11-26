python3 setup.py --help

python3 setup.py bdist_wheel

python3 setup.py clean 

cd ..
pip3 install helpers/dist/help...

and then use them:
```python
from helpers import extract_lower, extract_upper
# from helpers import variables
# import helpers

name = "Akash Anjanappa"
print(f"Lowercase letters: {extract_lower(name)}")
print(f"Uppercase letters: {extract_upper(name)}")
```