# do_twice returns a function 'wrapper_do_twice' which repeats function it received
def do_twice(func):
    def wrapper_do_twice():
        print("inside do_twice")
        func()
        func()
    return wrapper_do_twice


def whee():
    print("Whee!")


twice = do_twice(whee)
twice()
# inside do _twice
# Whee!
# Whee!

print("")

@do_twice
def decorator_whee():
    print("Whee!")


decorator_whee()
# inside do _twice
# Whee!
# Whee!
