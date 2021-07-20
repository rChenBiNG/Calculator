print("Please select the operation mode：")
print("+、Add up")
print("-、Subtract")
print("*、Multiply")
print("/、Except")
print("P、Prescribe")
print("S、Square")



choice = input("Enter your choice：")
choices_method = {
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x*y,
    '/': lambda x, y: x*y,
    'P': lambda x, y: pow(x, 1/y),
    'S': lambda x, y: pow(x, y)


}

if choice in choices_method:
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    func = choices_method[choice]
    result = func(num1, num2)
    print(f'{result}')

else:
    print("Error, it may be that you entered the wrong parameters and the program ends, please restart the program or the program, if the error cannot be resolved, please give me feedback")