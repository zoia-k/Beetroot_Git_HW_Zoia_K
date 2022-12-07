# Task 1
#
# A Person class

# Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters
# and add them as attributes. Make another method called talk() which makes prints a greeting from the person
# containing, for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def greetings(self, person):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old")


person_1 = Person('Carl', 'Johnson', 26)
person_2 = Person('Anna', 'Boleyn', 25)

person_1.greetings(person_1)
person_2.greetings(person_2)


# Task 2

# Doggy age

# Create a class Dog with class attribute `age_factor` equals to 7.
# Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.


class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        human_equivalent = self.dog_age * Dog.age_factor
        return human_equivalent


dog_1 = Dog(12)

print(dog_1.human_age())


# Task 3

# TV controller
#
# Create a simple prototype of a TV controller in Python. It’ll use the following commands:
#
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N
#                       or 'name' exists in the list, or "No" - in the other case.

CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:

    def __init__(self, channels=CHANNELS):
        self.channels = channels
        self.number = 0

    def first_channel(self):
        self.number = 0
        return self.channels[self.number]

    def last_channel(self):
        self.number = len(self.channels)-1
        return self.channels[self.number]

    def turn_channel(self, num):
        self.number = num - 1
        print(self.number)
        return self.channels[self.number]

    def next_channel(self):
        self.number = (self.number % len(self.channels)) + 1
        print(self.number)
        return self.channels[self.number]

    def previous_channel(self):
        self.number = (self.number % len(self.channels)) - 1
        print(self.number)
        return self.channels[self.number]

    def current_channel(self):
        return self.channels[self.number]

    def is_exist(self, name):
        if name in self.channels:
            return "Yes"
        return "No"


print("==============")
controller = TVController(CHANNELS)

print(controller.first_channel() == "BBC")
print(controller.last_channel() == "TV1000")
print(controller.turn_channel(1) == "BBC")
print(controller.next_channel() == "Discovery")
print(controller.previous_channel() == "BBC")
print(controller.current_channel() == "BBC")
print(controller.is_exist("BBC") == "Yes")
print(controller.is_exist("CNN") == "No")


