class myclass:
    __privatevar = 27 
    def __privmeth(self):
        print("i am inside class,myclass")
    def hello(self):
        print("private variable value",myclass.__privatevar)

foo = myclass()
foo.hello()
foo.__privmeth