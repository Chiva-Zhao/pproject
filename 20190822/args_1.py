def use_args(var1, *vars):
    print(var1)
    for var2 in vars:
        print(var2)

use_args("hello","my","work","is")