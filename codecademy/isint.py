def is_int(x):
    try:
        if type(x) == int:
            return True
        elif type(x) == float:
            str_num = str(x)
            posix_num = int(str_num[str_num.index('.')+1:])
            if posix_num == 0:
                return True
            else:
                return False
        else:
            return False
    except Exception   as err:
        print ("Error" + str(err))
print(is_int(111))
print(is_int(10.01))
print(is_int(10.0))