valid = False
while not valid:
    try:
        n = int(input("bla blah balh"))
        while n%2 ==0:
            print("bye bye")
        valid = True
    except ValueError :
        print("in valid")