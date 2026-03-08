from abc import ABC , abstractmethod
class abcclass(ABC):
    def print(self,x):
        print("passes value:",x)
    
    @abstractmethod
    def task(self):
        print("we are inside abcclass task")

class test_class(abcclass):
    def task(self):
        print("we are in test_class taks")

test = test_class()
test.task()
test.print(1000)