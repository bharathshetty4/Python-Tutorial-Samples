#program to get the next ip  address 
class IPAddress():
    def __init__(self,ip):
        self.ip=ip

    def __str__(self):

        return self.ip
    def __eq__(self,other):
        if(self.ip == other.ip):
            return 1
        return 0
    def __iter__(self):
        return self

    def next(self):
	newip = '0.0.0.0'
	ipsplit = self.ip.split(".")
	if(int(ipsplit[3]) < 255):
		intipsplit = int(ipsplit[3]) + 1
                ipsplit[3] = str(intipsplit)
	elif(int(ipsplit[2]) < 255):
                ipsplit[3] = '0'
                intipsplit = int(ipsplit[2]) + 1
                ipsplit[2] = str(intipsplit)
	elif(int(ipsplit[1]) < 255):
                ipsplit[2] = '0'
                intipsplit = int(ipsplit[1]) + 1
                ipsplit[1] = str(intipsplit)
    	elif(int(ipsplit[0]) < 255):
		[ipsplit[1]] = '0'
                intipsplit = int(ipsplit[0]) + 1
                ipsplit[0] = str(intipsplit)
	else:
		raise NoextraIPAvailable

	newip = ipsplit[0]+"."+ipsplit[1]+"."+ipsplit[2]+"."+ipsplit[3]
        return newip

    def valid(self):
        flag=1

        ipsplit = self.ip.split(".")
        if(len(ipsplit)>4):
            flag=0

        for i in ipsplit:
            if(int(i)>255 or int(i)<0):
                flag=0
        if(flag==1):
            return 1
        else:
            return 0

ip = IPAddress('254.255.255.255')
if ip.valid():
	print "\nvalid ip is given\n"
else:
	raise ipnotvalid

print (ip)
print ("\nnext ip is:\n")
print next(ip)

