from decimal import Decimal
import time
from matplotlib import pyplot as plt

def gcd(a,b): 
	if b==0: 
		return a 
	else: 
		return gcd(b,a%b)

a=[]
b=[]

#Add prime numbers for constructing the graph
key=[[11,17], [83, 97], [313,317],[1951, 1953], [5521,5557]]
 
for i in range(len(key)):
	p=key[i][0]
	q=key[i][1]

	#Enter the message in no
	no= 12

	n = p*q
	t = (p-1)*(q-1)

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
	x=n

	while (x!=0):
		count_bits+=1
		x=x//2
	a.append(count_bits//4)
	b.append(d_time)
	print('n = '+str(n)+' e = '+str(e)+' t = '+str(t)+' d = '+str(d)+' cipher text = '+str(ct)+' decrypted text = '+str(dt))
	print('Keylength = ' + str(count_bits) + ' time = ' + str(d_time))

#Constructing the Graoh 
plt.plot(a, b) 
plt.xlabel('Key Length (bits)') 
plt.ylabel('Decrypted time (seconds)') 
plt.title('Speed Test (RSA)')   
plt.show() 