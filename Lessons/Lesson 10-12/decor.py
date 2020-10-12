def do_twice_decorator(y):
    def wrapper(*args, **kwargs):
        return y(args[0])
    return wrapper

@do_twice_decorator
def my_func(x):
    print("my_func")
    return f"this is my_func with {x}"

#my_func = do_twice_decorator(my_func)

print(my_func(5))
