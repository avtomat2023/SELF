x = ['x = ["x = [" + chr(39) + x[0] + chr(39) + ", " + chr(39) + x[1] + chr(39) + "]"] + x', 'print(chr(10).join(x))']
x = ["x = [" + chr(39) + x[0] + chr(39) + ", " + chr(39) + x[1] + chr(39) + "]"] + x
print(chr(10).join(x))
