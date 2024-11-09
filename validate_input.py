import re

def validate_input(value, data_type):
    if data_type == 'integer':
        return value.isdigit()
    elif data_type == 'float':
        try:
            float(value)
            return True
        except ValueError:
            return False
    elif data_type == 'email':
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(email_regex, value))
    return False


print(validate_input("5", "integer"))  # Output: True
print(validate_input("[email protected]", "email"))  # Output: True
