no=int(input("Enter number pls:"))
if(no < 50):
    amount=no * 2.60
    surcharge=25
elif(no <=100):
 amount=130+((no-50)*3.25)
 surcharge=35
elif(no <=200):
   amount=130+160.50+((no -100)*5.26)
   surcharge=45
else:
   amount=130+162.50+526+((no -200)*8.45)
   surcharge=75
total=amount+surcharge
print("Bill =",total)