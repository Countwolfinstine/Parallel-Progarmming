import time
import random
import math
from multiprocessing import Pool


def CostlyFunction(x):
	for i in x:
		if i**(1 / 3.0) == 102:
			print 1
		else:
			pass

def rando():
		arr=[]
		for i in range(1,1000000):
				arr.append(random.randint(1,101))
		return arr

if __name__=='__main__':
		t0=time.clock()
		List1=rando()
		List2=rando()
		CostlyFunction(List1)
		CostlyFunction(List2)
		t1=time.clock()
		print(t1-t0)
