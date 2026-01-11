def add(A,B):
    return A+B
def subtract(A,B):
    return A-B
def multiply(A,B):
    return A*B
def divide(A,B):
    return A/B
print("please select an option okay")
print("a.add")
print("b.subtract")
print("c.multiply")
print("d.divide")
choice = input("please enter ur choice a/b/c/d")
num =int(input("please enter 1st number"))
num1 = int(input("please enter 2nd number"))

if choice =="a":
    print(num , "+" , num1 ,"=",add(num,num1))
elif choice =="b":
    print(num , "-" , num1 ,"=",subtract(num,num1))
elif choice =="c":
    print(num , "*" , num1 ,"=",multiply(num,num1))
elif choice =="d":
    print(num , "/" , num1 ,"=",divide(num,num1))
else:
    print("invalid input")