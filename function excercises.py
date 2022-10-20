# write a python function to multiply all the numbers in a list.

numbers = [2,5,4,9,8,2,3,5,65]

def multiply_list(list):
    result = 1
    for number in list:
        result *= number
    return result

result = multiply_list(numbers)
print(result)



# write a python functon that take a number as a parameter and
# check the number is prime or not.

def check_prime(number):
    if (number == 1):
        return False
    elif (number == 2):
        return True
    else:
        for x in range(2,number):
            if (number % x) == 0:
                return False
            else:
                return True

print(check_prime(9))

