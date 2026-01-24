try:
    num1,num2 =eval(input("num withs comma separating them"))
    result = num1/num2
    print("tehresultis",result)
except ZeroDivisionError :
    print("/ by 0 is an Error")
except SyntaxError :
    print("Entering num with no , is invalid")
except:
    print("wrongly")
else:
    print("no error")
finally:
    print("no matter what")