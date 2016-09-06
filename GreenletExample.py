from greenlet import greenlet

def taskone(x,y):
	z = gl2.switch(x+y)
	print 'Taskone: ', z

def tasktwo(z):
	print "tasktwo: ", z
	gl1.switch('message')
	print "tasktwo again"


gl1 = greenlet(taskone)
gl2 = greenlet(tasktwo)

gl1.switch("Hello", " World")
