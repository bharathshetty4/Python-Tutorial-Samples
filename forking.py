import os
import time
child=os.fork()
if child==0:
	print "HI with pid",os.getpid()
	for x in range(10):
		print "child: value of x" ,x
		time.sleep(1)
 	os._exit(0)
#waits till the child completes
#os.wait()
print"parent with pid",os.getpid()
for y in range(10):
                print "parent: value of y" ,y
                time.sleep(1)
os._exit(0)



