# def greeting():
#     print("Hello Python")

def greeting(name):
    # print("Hello", name)
    return f"Hello {name}"

# my_greeting = greeting("aouwal")
# print(my_greeting)

# greeting("rakib")
# greeting("sakib")
# print("*" * 10)
# greeting("borsha")
# greeting("apu")

def voter_check(age):
    if age >= 18:
        return "She/He is voter"
    else:
        return "You are not eligible to vote"

print(voter_check(18))
print(voter_check(14))