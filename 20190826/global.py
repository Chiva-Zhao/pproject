def add(value1, value2):
    result = value1 + value2


add(2, 4)


# print(result) # NameError: name 'result' is not defined

def addglobal(value1, value2):
    global result
    result = value1 + value2


addglobal(2, 4)
print(result)


def profile():
    global name
    global age
    name = "Danny"
    age = 30


profile()
print(name, age)


def profile1():
    name = "Danny"
    age = 30
    return (name, age)


profile_data = profile1()
print(profile_data[0], profile_data[1])

def profile2():
    name = "Danny"
    age = 30
    return name, age

profile_data = profile2()
print(profile_data[0], profile_data[1])