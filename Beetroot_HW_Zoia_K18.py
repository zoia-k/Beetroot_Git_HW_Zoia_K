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


Validator('AB.yz@ma_il.com')