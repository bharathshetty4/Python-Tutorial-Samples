def integers():
    i=1
    while True:
         yield i
         i = i + 1

def squares():
    for i in integers():
        yield i*i
def cubes():
    for i in integers():
        yield i*i*i

def primes():
    start = 3
    num = start
    yield 2
    while (1):
        num = num +1
        flag =1
        divnum = int(num/2)
        for i in range(2,divnum+1):
            if(num % i==0):
                flag=0
        if(flag==1):
            yield num
def integersmodule():
    i=1
    while True:
        n = yield i
        if(n==10):
            i = 0
        else:
            i = i + 1

def get(n,things):
    listvar = []
    i = 0
    while i < n:
        temp =next(things)
        listvar.append(temp)
        if(temp==10):
            things.send(10)
        i = i + 1
    return listvar


l = get(20,integersmodule())
print (l)

