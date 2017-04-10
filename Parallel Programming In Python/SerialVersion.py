#This code achieves similar functionality as the parallel code.

import time
import random
import math
from multiprocessing import Pool

# This function tries to find an element in the list hose cube root is equal to 102..
# This is litrally impossible, since we are generating numbers between 1 and 102
# This is done intentionally so that the entire list is being iteated through.

def CostlyFunction(x):
	arr=[]
	for i in x:
		 arr.append(i**(1 / 3.0))
	return arr;

def rando():
		arr=[]
		for i in range(1,1000000):
				arr.append(random.randint(1,101))
		return arr

if __name__=='__main__':
		t0=time.clock()
		List1=rando()
		List2=rando()
		List1=CostlyFunction(List1)
		List2=CostlyFunction(List2)
		t1=time.clock()
		print(t1-t0)
