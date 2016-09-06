import os, re, time, sys

ll = re.compile(r"(\d) received")
rep = ("NO response","Partial Response","Alive")

print time.ctime()


for host in range(60,70):
	ip = "10.1.200."+str(host)
	pinging = os.popen("ping -q -c2 "+ip,"r")
	print"testing ....", ip
	sys.stdout.flush()
	while True:
		line = pinging.readline()
		if not line:
			break
		igot = re.findall(ll,line)
		if igot:
			print rep[int(igot[0])]
print time.ctime()
