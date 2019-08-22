def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
args = "var1","var2","var3"
args1 = {"arg1":"var1","arg2":10,"arg3":100.0}
test_args_kwargs(*args)
test_args_kwargs(**args1)
