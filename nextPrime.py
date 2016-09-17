def nextprime(prime):
    num = prime + 1

    while (1):
        flag=1
        divnum = int(num/2)
        for i in range(2,divnum+1):
            if(num % i==0):
                flag=0

        if(flag==0):
            num= num +1
        else:
            return num

    return num

def funcprime(a):
    t=nextprime(a)
    print ("the next prime number is:",t)

a = int(input("Enter a digit:"))
funcprime(a)
