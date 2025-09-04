def floor_divide(a, b):
    return a // b

def string_addiction(a,b):
    return a + b


def main():
    user_input_1 = float(input("Enter first number: "))
    user_input_2 = float(input("Enter second number: "))

    user_input_3 = str(input("Enter first string: "))
    user_input_4=  str(input("Enter second string: "))


    res = floor_divide(user_input_1, user_input_2)
    res2=string_addiction(user_input_3,user_input_4)


    print("Result of floor division:", res)
    print("Final string:", res2)

main()