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


# Task 3

# Write a decorator `arg_rules` that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
# If some of the rules' checks returns False, the function should return False
# and print the reason it failed; otherwise, return the result.


def arg_rules(type_, max_length, contains):
    def take_func(func):
        def check_args(arg):
            if type(arg) != type_:
                raise TypeError('Argument is not a string!')

            if len(arg) > max_length:
                raise ValueError('Maximum length is 15!')

            for symbol in contains:
                if symbol not in arg:
                    raise ValueError(f"Symbol {symbol} must be included !")

            else:
                return func(arg)

        return check_args

    return take_func


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


create_slogan('john05gmail.com')

assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
