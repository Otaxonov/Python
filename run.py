def check_for_capitalize(func):
    def check_for_isupper(name):
        if name[0].isupper():
            return func(name)
        else:
            return "The person's name should be written in capital letters."
    return check_for_isupper

@check_for_capitalize
def say_hello(name):
    print(f'Hello {name}!')

print(say_hello(name='Sarvar'))
