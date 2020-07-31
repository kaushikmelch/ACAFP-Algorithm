from decimal import Decimal
import time
from matplotlib import pyplot as plt

def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)

w = int(input('Enter the value of w = '))
x = int(input('Enter the value of x = '))
y = int(input('Enter the value of y = '))
z = int(input('Enter the value of z = '))
no = int(input('Enter the value of text = '))

n = w*x*y*z
t = (w-1)*(x-1) *(y-1)*(z-1)

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

dtt = Decimal(0)
dtt = pow(ct,d)
dt = dtt % n

print('n = '+str(n)+' e = '+str(e)+' t = '+str(t)+' d = '+str(d)+' cipher text = '+str(ct)+' decrypted text = '+str(dt))
