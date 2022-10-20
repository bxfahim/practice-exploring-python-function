# def add(a,b):
#     return a + b
#
# def addition(a,b,c):
#     return a + b+ c
#
# print(add( 7, 6 ))
# print(addition(3,6,5))

def multiple_addition(*number):
    sum = 0
    for n in number:
        sum += n
    return sum

# print(multiple_addition(2,5,26,4))