from functools import wraps


# Task 1

# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
# For example:
# "add called with 4, 5"


def logger(func):
    @wraps(func)
    def wrap(*args):
        print(f'{func.__name__} called with {args}')
        func(*args)

    return wrap


@logger
def add(x, y):
    return x + y


add(4, 5)


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


square_all(1, 2, 3, 4)

# Task 2
# Write a decorator that takes a list of stop words
# and replaces them with * inside the decorated function


def stop_words(words_list=[]):
    def check_slogan(func):
        def check_words(arg):
            slogan = func(arg)
            print(slogan)
            for word in words_list:
                slogan = slogan.replace(word, '*')
            print(slogan)
            return slogan

        return check_words

    return check_slogan


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
assert create_slogan("Jane") == "Jane drinks * in his brand new *!"

