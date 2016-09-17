def gen1():
    for i in 'abcde':
        yield i
def gen2():
    for i in '12345':
        yield i


def chain(func1,func2):
    listnew = []

    for i in gen1():
        listnew.append(i)
    for i in gen2():
        listnew.append(i)
    return listnew

gen3=chain(gen1,gen2)
for x in gen3:
    print (x)
