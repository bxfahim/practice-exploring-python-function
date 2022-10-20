num_list = [1,2,3,4,5,6,7,8,9,11,12,15,25,15,75,69,100]
num_list_2 = [21,222,23,24,25,26,272,28,29,211,212,215,225,215,275,629,1200]

# # Make a list of even numbers from the given list
# even_number_list = []
# for number in num_list:
#     if number % 2 == 0:
#         even_number_list.append(number)
#
# print(even_number_list)

def even_number_finder(number_list):
    even_number_list = []
    for number in number_list:
        if number % 2 == 0:
            even_number_list.append(number)
    return even_number_list

even_list_one = even_number_finder(num_list)
even_list_two = even_number_finder(num_list_2)

print(even_list_one)
print(even_list_two)



