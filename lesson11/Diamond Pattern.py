rowsize=int(input("num"))
if rowsize%2==0:
    halfrow=int(rowsize/2)
else:
    halfrow=int(rowsize/2)+1
space =halfrow-1
for m in range(1,halfrow+1):
    for n in range (1, space+1):
        print(end =" ")
    space =space-1
    num = 1
    for n in range (2*m-1):
        print(end=str (num))
        num=num+1
    print( )
space = 1
for m in range(1,halfrow):
    for n in range (1, space+1):
        print(end =" ")
    space =space+1
    num = 1
    for n in range (1,2*(halfrow-m)):
        print(end=str (num))
        num=num+1
    print( )
