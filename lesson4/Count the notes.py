amount=int(input("PLEASE ENTER YYOUR AMOUNT"))
note=amount // 100
note1=(amount % 100)//50
note2=((amount % 100)%50)//10
print("Note 100=",note)
print("Note 50=",note1)
print("Note 10",note2)