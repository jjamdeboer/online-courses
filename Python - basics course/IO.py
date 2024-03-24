# PATHS INDICATED WITH "../../../*.txt" FOR EXAMPLE
# CAN ALSO WRITE TO A FILE

DURK = open('DURK.txt',mode = 'w+')
DURK.write("DUUUUUUUUUUUUUU\nUUUUUUUUUUUUUUUU\nUUUUUUUUUUUUUUUUUUU\nUUUUUUUUUUUUUUUUURK")
print(DURK.seek(0))
print(DURK.read())

file1 = open('sets.py')
print(file1.read())

print(file1.read())
print(file1.seek(0))
print(file1.read())
file1.close()
file2 = open('WHATWHATWHAT.txt',mode = 'w+')

