lower=int(input("pls enter"))
upper=int(input("pls value"))
print("prime nums inside",lower,"and",upper,"are")

for num in range(lower,upper + 1):
    if num>1:
        for i in range(2,num):
            if (num %  i)==0:
                break
        else:
            print(num)