# Task 1
#
# School
#
# Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student, and another one called Teacher.
# Try to find as many methods and attributes as you can which belong to different classes,
# and keep in mind which are common and which are not.
# For example, the name should be a Person attribute,
# while salary should only be available to the teacher.

class Person:
    def __init__(self, first_name, last_name, age, phone_num):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_num = phone_num

    def __repr__(self):
        return f'{self.first_name} ,{self.last_name} ,{self.age}, {self.phone_num}, {type(self.phone_num)}'

    def __str__(self):
        return f'{self.first_name} ,{self.last_name} ,{self.age}, {self.phone_num}'


class Teacher(Person):
    teachers = 0

    def __init__(self, first_name, last_name, age, phone_num, subject, experience, salary):
        super().__init__(first_name, last_name, age, phone_num)
        self.subject = subject
        self.experience = experience
        self.salary = salary
        Teacher.teachers += 1


teacher_1 = Teacher('Olga', 'Ivanova', 36, '0963652000', 'Biology', 5, 20000)
teacher_2 = Teacher('Victor', 'Petrov', 42, '0962325452', 'Physics', 8, 24000)

print(repr(teacher_1))
print(repr(teacher_2))
print(str(teacher_1))
print(str(teacher_2))
print(Teacher.teachers)


class Student(Person):
    students = 0
    students_list = []

    def __init__(self, first_name, last_name, age, phone_num, group, specialty, GPA):
        super().__init__(first_name, last_name, age, phone_num)
        self.group = group
        self.speciality = specialty
        self.GPA = GPA
        Student.students += 1
        Student.students_list.append(self)


student_1 = Student('Anna', 'Vasina', 23, '+380962705555', 'B-5', 'Biology', 4.6)
student_2 = Student('Oleg', 'Efremov', 22, '+380962705000', 'P-4', 'Physics', 3.8)
student_3 = Student('Irina', 'Svetina', 24, '+380962704000', 'B-3', 'Physics', 4.8)

print(Student.students_list)


# Task 2

# Mathematician
#
# Implement a class Mathematician which is a helper class for doing math operations on lists
#
# The class doesn't take any attributes and only has methods:
#
# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'


class Mathematician:

    def __init__(self):
        pass

    def square_nums(self, nums_list):
        square_list = []
        for num in nums_list:
            square_list.append(num ** 2)
        return square_list

    def remove_positives(self, nums_list):
        return [num for num in nums_list if num < 0]

    def filter_leaps(self, nums_list):
        return [num for num in nums_list if num % 400 == 0 or num % 100 != 0 and num % 4 == 0]


list_1 = [7, 11, 5, 4]
list_2 = [26, -11, -8, 13, -90]
list_3 = [2001, 1884, 1995, 2003, 2020]

print(Mathematician().square_nums(list_1))
print(Mathematician().remove_positives(list_2))
print(Mathematician().filter_leaps(list_3))

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]