def palind(t):
    e =len(t)-1
    s=0
    while s<e:
        if t[s] != t[e]:
            return False
        s += 1
        e -=1
    return True
t =(1,2,3,3,2,1)
if palind(t):
    print("the tuple is filp flop")
else:
    print("the tuple is not flip flop")