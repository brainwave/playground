code = '''\
# This program prints a part of its own source code
code = {!r}
print(code[3:37] + code[37:])
'''

print(code.format(code))
