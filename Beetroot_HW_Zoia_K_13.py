# Task 1
# Write a Python program to detect the number of local variables declared in a function.

def f():
    a = [3, 5, 7, 11]
    res = [a ** 2 for a in a]
    print(res)


def s_of_tri90():
    a = int(input('Input a:> '))
    b = int(input('Input a:> '))
    s = a * b / 2
    print('S = ', s)


def num_var(function):
    print("Number of local variables available:", function.__code__.co_nlocals)


num_var(f)
num_var(s_of_tri90)


# Task 2
# Write a Python program to access a function inside a function
# (Tips: use function, which returns another function)

def f():
    a = 1
    print('def f():', a)

    def x():
        b = 2
        print('def x():', b)

    return x


# f()

def call_f(function):
    function()


call_f(f())


# Task 3
# Write a function called `choose_func` which takes a list of nums and 2 callback functions.
# If all nums inside the list are positive, execute the first function on that list and return the result of it.
# Otherwise, return the result of the second one

# nums1 = [1, 2, 3, 4, 5]

# nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    result = [num ** 2 for num in nums]
    print(result)


def remove_negatives(nums):
    result = [num for num in nums if num > 0]
    print(result)


def choose_func(num_list, func1, func2):
    for num in num_list:
        if num < 0:
            func2(num_list)
    else:
        func1(num_list)




#choose_func([1, 2, 3, 4, 5], square_nums, remove_negatives)
choose_func([1, -2, 3, -4, 5], square_nums, remove_negatives)