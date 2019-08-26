from functools import wraps


def logit(logfile="log.txt"):
    def logging(func):
        @wraps(func)
        def wrap_func(*args, **kwargs):
            log_str = func.__name__ + " was called"
            print(log_str)
            # 打开logfile， 并写⼊内容
            with open(logfile, "a") as logfiles:
                logfiles.write(log_str + "\n")
            return func(*args, **kwargs)
        return wrap_func
    return logging

@logit()
def myfun1():
    pass
# myfun1()
@logit("log2.txt")
def myfun2():
    pass
# myfun2()