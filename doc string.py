# write a python function to convert fahrenheit to celsius

# c = 5/9 * (f-32) = formula

def fahrenheit_celsius(fahrenheit):
    """
    This function will convert fahrenheit temperature to celsius
    :param fahrenheit: It takes fahrenheit temperature as a parameters
    :return: it will return celsius temperature
    """
    celsius = 5/9 * (fahrenheit - 32)
    return celsius

# print(fahrenheit_celsius(100),"Celsius")

name = "Abdul Aouwal"
print(fahrenheit_celsius.__doc__)
