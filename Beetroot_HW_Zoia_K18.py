# Task 1
import string


# Email validator

# Create a class method named `validate`, which should be called from the `__init__` method
# to validate parameter email, passed to the constructor.
# The logic inside the `validate` method could be to check
# if the passed email parameter is a valid email string.

class Validator:
    def __init__(self, email):
        self.email = email
        Validator.validate(email)

    @staticmethod
    def validate(email):
        email = email.lower()
        symbols_list = ['.', '-', '_', '@']
        letters_list = [i for i in string.ascii_lowercase]
        digits_list = [str(i) for i in range(10)]
        valid_symbols_list = symbols_list + letters_list + digits_list

        if email[0] in symbols_list:
            raise SyntaxError(f'Symbol "{email[0]}" cannot take the first position')

        for symbol in email:
            if symbol not in valid_symbols_list:
                raise ValueError(f'Symbol "{symbol}" is not valid')

        dog_index = email.index('@')

        for symbol in email[: dog_index]:

            if symbol in symbols_list:
                symbol_i = email.find(symbol)
                if email[: dog_index][symbol_i + 1] in symbols_list:
                    raise ValueError(f'"{symbol}" must be followed by one or more letter or number.')

        domen_dot = email.rfind('.')

        if len(email[domen_dot + 1:]) < 3:
            raise ValueError('The last portion of the domain must be at least two characters')

        for symbol in email[dog_index + 1: domen_dot]:
            if symbol == '.' or symbol == '_':
                raise SyntaxError(f'Domen name cannot contains "{symbol}"')

        print(f'Email "{email}" is valid')


Validator('AB.yz@mail.com')


# Task 2

# Bosses and Workers

# Implement 2 classes, the first one is the Boss and the second one is the Worker.
# Worker has a property 'boss', and its value must be an instance of Boss.
# You can reassign this value, but you should check whether the new value is Boss.
# Each Boss has a list of his own workers.
# You should implement a method that allows you to add workers to a Boss.
# You're not allowed to add instances of Boss class to workers list directly via access to attribute, use getters and setters instead!


class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss
        boss.workers.append(self)

    def get_boss(self):
        return self._boss

    def set_boss(self, new_boss):
        self._boss.workers.remove(self)
        self._boss = new_boss
        new_boss.workers.append(self)


boss_1 = Boss(125412, 'Boss_1', 'Bad Company')
worker_1 = Worker(741852, 'Worker_1', boss_1.company, boss_1)

assert worker_1.get_boss() == boss_1
assert boss_1.workers[0] == worker_1

boss_2 = Boss(296412, 'Boss_2', 'Good Company')
worker_2 = Worker(741482, 'Worker_2', 'Good Company', boss_2)

worker_1.set_boss(boss_2)

assert worker_2.get_boss() == boss_2
assert boss_2.workers[1] == worker_1
assert len(boss_1.workers) == 0

#print(boss_2.workers)