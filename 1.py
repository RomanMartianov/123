a=int(input('Enter any number:'))

if a%2==0:
    print('even number')

else:
    print('odd number')


b=3

c=bin(a*b)[2:]

print(c)