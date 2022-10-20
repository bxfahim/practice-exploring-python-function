a = 32
b = 20

#
# addition = a + b
# subs = a - b
# print(addition,subs)

def add_sub(a,b):
    """
    This will return addition and substruction of the numbers
    :param a: first number
    :param b: second number
    :return: addition and substruction
    """
    addition = a + b
    subs = a - b
    return addition,subs

# print(add_sub.__doc__)
# print(add_sub(45,52))
result = add_sub(40, 25)
print(type(result))
