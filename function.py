# strings="AMAN"
# print(len(strings))



# def name (parameter)

# no return no arguments function
# def sayhello():
#     print("Hello World")

# sayhello() 

# no return with arguments function

# def sayhello(name):
#     print("Hello", name)

# sayhello("Aman")

# name = AMAN

# return with no arguments function

# def add():
#     a=10
#     b=20
#     return a+b
    

# print(add())


# return with arguments function
# def add(a,b):
#     return a+b
    

# answer=add(10,20)
# print(answer)


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):  
    return a*b
def div(a,b):   
    return a/b

print("Select operation.")
print("1.Add \n2.Subtract \n3.Multiply \n4.Divide")
choice = str(input("Enter choice"))
choice=choice.lower()
if choice== "1" or choice== "add":
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))
    print(add(a,b))

elif choice== "2" or choice== "subtract":
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))
    print(sub(a,b))

elif choice== "3" or choice== "multiply":
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))
    print(mul(a,b))

elif choice== "4" or choice== "divide":
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))
    print(div(a,b))
else:
    print("Invalid input")