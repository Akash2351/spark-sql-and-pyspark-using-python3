import sys

my_file = open('xmen.txt', 'w+')
my_file.write('Beast\n')
my_file.write('Phoenix\n')
my_file.writelines(['Cyclops\n', 'Bishop\n'])

my_file.close()

my_file = open('xmen.txt', 'r')
print(my_file.read())
my_file.close()

#my_file.seek(0)
# with open('xmen.txt', 'w+') as my_file:
# ...

# read bytes
with open('xmen.txt', 'rb') as fl:
    print(fl.readlines())
    b_array = bytearray(10)
    fl.readinto(b_array)
    print(b_array)

sys.stdout.write("test write to out")
# lines = sys.stdin.readlines()
