# Sample Python MultiProcessing Code to demonstrate the use of Process Class of multiprocessing library.
# This Program is just written to familiarize myself with parallel programming in Python.
# The code iterates over two randomly generated lists at the same time. 
# Each list element is also raised to the power 1/5.0 just to make the function more computationally costly. 
# This Code is similar to writing Parallel OMP setions directive of Open MP in C programming. 

import time
import random
from multiprocessing import Pool
from multiprocessing import Process


def CostlyFunction(x):
	for i in x:
		if i**(1 / 3.0) == 102:
			print 1
		else:
			pass

def GenerateRandomList():
	arr=[]
	for y in range(1,1000000):
		arr.append(random.randint(1,101))
	return arr

if __name__=='__main__':
	t0=time.clock()
	List1=GenerateRandomList()
	List2=GenerateRandomList()
	p = Process(target=CostlyFunction,args=(List1,))
	q = Process(target=CostlyFunction,args=(List2,))
	q.start()
	q.join()
	p.start()
	p.join()
	t1=time.clock()
	print(t1-t0)
