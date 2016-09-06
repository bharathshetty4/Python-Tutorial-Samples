import sys, time, signal

def sig_handler(signum, frame):
	print "signal recieved" , signum
	raise Exception

def worker():
	signal.signal(signal.SIGALRM, sig_handler)
	signal.alarm(10)
	try:
		while True:
			print "Hello"
			time.sleep(2)
	except Exception:
		print "timeout"
	finally:	return


worker()
for x in range(5):
	print "Do work ..",x
	time.sleep(2)
