def si(p,r,t):
	i=p*r*t/100
	return i
	
print si(1000,2,3);

p1=input("Enter principle : ")
r1=input("Enter rate : ")
t1=input("Enter time : ")

print "Intrest =",si(p1,r1,t1)