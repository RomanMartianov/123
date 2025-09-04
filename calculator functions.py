'''
this is the user inputs for add,subtract,multiply and divide functions
'''
user_input1=float(input("Enter first number: "))

user_input2=float(input("Enter second number: "))

'''
this is add function
'''
def add(user_input1, user_input2):
    res = user_input1 + user_input2
    return res
'''
this is substract function
'''
def subtract(user_input1, user_input2):
    res = user_input1 - user_input2
    return res
'''
this is multiply function
'''
def multiply(user_input1, user_input2):
    res = user_input1 * user_input2
    return res
'''
this is divide function
'''
def divide(user_input1, user_input2):

    if user_input2 !=0:
        res= user_input1 / user_input2
        return res

    else:
        print('Error: You cannot divide by zero!')

    
'''
vars 
'''

a1=add(user_input1, user_input2)
a2=subtract(user_input1, user_input2)
a3=multiply(user_input1, user_input2)
a4=divide(user_input1, user_input2) 

'''
outputs
'''
print("Addition:", a1)
print("Subtraction:", a2)
print("Multiplication:", a3)
print("Division:", a4)