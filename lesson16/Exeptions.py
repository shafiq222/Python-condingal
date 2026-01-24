try:
    number = int(input("number pls"))
    print("The number is:",number)
except ValueError as e:
    print("WTF",e)