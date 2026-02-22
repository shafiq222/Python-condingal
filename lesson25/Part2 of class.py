class parrot:
    spices ="bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
ob1 = parrot("Blu",10)    
ob2 = parrot("woo",15)

print("Blu is a",ob1.spices)
print("woo is a",ob2.spices)

print(ob1.name,"is",ob1.age,"years old")
print(ob2.name,'is',ob2.age,"years old")