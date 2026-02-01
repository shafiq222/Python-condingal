L = [4,5,1,2,9,7,10,8]
print("org lst :",L)
sum =0
for i in L:
    sum += i
avg =sum/len(L)
print("sum =",sum)
print("avrage",avg)
L.sort()
print("smallest elment is",L[0])
print("bigest elment is",L[-1])