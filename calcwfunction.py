print("Welcome to my calc")

def add(a ,b):
    return a + b
def div(a ,b):
    return  a / b
def sub(a ,b):
    return a - b
def mul(a ,b):
    return a * b

print("Select your operation:\n1. Sum \n2. Substraction \n3. Multiplication \n4. Division")
x = int(input("Enter your choice: "))

n1 =int(input("Enter first number: "))
n2 =int(input("Enter second number: "))

if x == 1:
    print(n1,"+",n2,"=", add(n1,n2))
elif x == 2:
    print(n1,"+",n2,"=", sub(n1,n2))
elif x == 3:
    print(n1,"+",n2,"=", mul(n1,n2))
elif x == 4:
    print(n1,"+",n2,"=", div(n1,n2))
else:
    print("Invalid choice Input, Please try again")

