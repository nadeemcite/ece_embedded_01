def twice(x):
	return x*2
	
print twice(twice(100))

a=[1,2,3,4,5]
b=[ twice(x) for x in a]
print b


def isEven(x):
	return x%2==0

a=[1,2,3,4,5]
b=[ twice(x) for x in a if isEven(x)]
print b	
