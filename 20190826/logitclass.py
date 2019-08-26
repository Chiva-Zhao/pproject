from functools import wraps


class logitclass(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrap_fun(*args, **kwargs):
            log_string = func.__name__ + " was called"
            with open(self.logfile, 'a') as log_file:
                log_file.write(log_string + '\n')
            self.notify()
            return func(*args, **kwargs)

        return wrap_fun

    def notify(self):
        pass


@logitclass()
def demofun():
    pass


# demofun()

class emaillogitclass(logitclass):
    def __init__(self, email="zzh@jf.com", *args, **kwargs):
        self.email = email;
        super(logitclass, self).__init__(*args, **kwargs)

    def nitify(self):
        # send email here
        pass


@emaillogitclass()
def email_fun():
    pass


email_fun()
