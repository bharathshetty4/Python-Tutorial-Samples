import os, sys, re, time
from threading import Thread

class testit(Thread):
	def __init__(self,ip):
		Thread.__init__(self)
		self.ip=ip
		self.status = -1
	def run(self):
		pingaling = os.open("ping -q -c2 "+self.ip,"r")
		while 1:
			line = pinglist.readline()
			if not line:	break
			igot = re.findall(p.ll,line)
			if igot:
				self.status = int(igot[0])

testit.lifeline = re.compile(r"(/d) received")
report  = ("NO response", "Partial res" , "Alive")

print time.ctime()

pinglist = []

for host in range(60,70):
	ip = "10.1.200."+str(host)
	current = testit(ip)
	pinglist.append(current)
	current.start()

for pingle in pinglist:
	pingle.join()
	print "status from",pingle.ip,"is",report[pingle.status]

print time.ctime()
