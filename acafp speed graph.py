from decimal import Decimal
import time
from matplotlib import pyplot as plt

def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)

#For Computing the Graph
a=[]
b=[]

#Add prime numbers for constructing the graph
key=[[2,3,5,7],[5, 7, 13, 17], [13,17,19,29],[39,41,47, 53], [67, 71, 73, 79]]

for i in range(len(key)):
	w=key[i][0]
	x=key[i][1]
	y=key[i][2]
	z=key[i][3]

	# Enter the message in no
	no= 12

	n = w*x*y*z
	t = (w-1)*(x-1)*(y-1)*(z-1)

	for e in range(2,t):
		if gcd(e,t)== 1:
			break


	for i in range(1,10):
		x = 1 + i*t
		if x % e == 0:
			d = int(x/e)
			break

	ctt = Decimal(0)
	ctt =pow(no,e)
	ct = ctt % n

	start_time=time.time()
	dtt = Decimal(0)
	dtt = pow(ct,d)
	dt = dtt % n
	end_time=time.time()
	d_time=end_time-start_time

	#Calculate Number of Bits
	count_bits=0
	while (n!=0):
		count_bits+=1
		n=n//2
	a.append(count_bits)
	b.append(d_time)
	print('n = '+str(n)+' e = '+str(e)+' t = '+str(t)+' d = '+str(d)+' cipher text = '+str(ct)+' decrypted text = '+str(dt))
	print('Keylength = ' + str(count_bits) + ' time = ' + str(d_time))

#Constructing the Graph
plt.plot(a, b)
plt.xlabel('Key Length (bits)')
plt.ylabel('Decrypted time (seconds)')
plt.title('Speed Test (ACAFP)')
plt.show()


