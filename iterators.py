class Numbers:
    def __init__(self, start, end=None , skip=0):
	if(end == None):
		self.start = 1
		self.end = start
	else:
		self.start = start
	        self.end = end
	if(skip > 0):
		self.skip = skip-1
	else:
		self.skip = 0
    
    def __str__(self):
        return 'Numbers({0},{1})'.format(self.start,self.end)

    def __iter__(self):
        return self

    def next(self):
        if (self.start > self.end):
            raise StopIteration
        self.start = self.start + 1 +self.skip
        return self.start -  1 - self.skip  

print ( "FOR 10,20,2")
nums = Numbers(10,20,2)
print (next(nums))
print (next(nums))
print ("printing others:")
for n in nums:
    print (n)

print ("---------------")
print ( "FOR 10,20")

nums1 = Numbers(10,20)
print (next(nums1))
print (next(nums1))
print ("printing others:")
for n in nums1:
    print (n)


print ("---------------")
print ( "FOR 10")

nums2 = Numbers(10)
print (next(nums2))
print (next(nums2))
print ("printing others:")
for n in nums2:
    print (n)
