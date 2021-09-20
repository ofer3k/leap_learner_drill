number1 = int(input('Enter First number : '))
number2 = int(input('Enter Second number : '))
number3 = int(input('Enter Third number : '))

lst = [number1, number2, number3]
print('first way:')
print("The smallest of the 3 numbers is : ", min(lst))
print('------------------------------------------------')
# --------------------------------------another way:----------------------------------------
smallest = 0
if number1 < number2 and number1 < number3 :
    smallest = number1
if number2 < number1 and number2 < number3 :
    smallest = number2
if number3 < number1 and number3 < number2 :
    smallest = number3
print('second way:')
print(smallest, "is the smallest of three numbers.")
