class new_yield():
    def __init__(self,word):
        print word

    def arr1(self):
         yield 1
         print "new"
         yield 3


a = new_yield("")

for i in a.arr1():
    print i
    print "old"


