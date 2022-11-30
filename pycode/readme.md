## installation:

https://github.com/pyenv/pyenv
brew update
brew install pyenv

for bash:
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile

for zsh:
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

exec "$SHELL"

### install a specific version
pyenv global 3.10
python3 -m pip install --upgrade pip
pip3
python3

## Distribution:
python3 setup.py --help
python3 setup.py bdist_wheel
python3 setup.py clean

cd ..
pip3 install helpers/dist/help...
pip3 install --editable .
pip3 uninstall -y helpers

### Doctest
 python3 -m doctest strings.py

### Shebang
instead of running python3 main.py, update the file to include the shebang
#!/usr/bin/env python3

and then just run the file:  ./main.py


### Helpful modules
Math and Random modules

math:
sin, cos, tan, hypot, 
floor, ceil, trunc, 
sqrt, factorial

random:
random.random - return between 0.0 to 1.0
choice, sample, shuffle

### platform module
Access underlying platform information

import platform
dir(platform)

platform.system() 
platform.python_version()
platform.uname();

## OOP
python3 -i vehicle.py
car= Vehicle('4 cylinder', ['tire1', 'tire2', 'tire3', 'tire4])
car.description()

If you need multiple constructions, you need to use decorators
@classmethod
...

bike = Vehicle.bicycle();
bike.tires
bike  = Vehicle.bicycle(['t1', 't2'])
bike.description()

// similarly
@staticmethod

// name mangling.. like private variables
see mapping.py 

