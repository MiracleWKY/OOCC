from multiprocessing import Pool

from multiprocessing import Process

def f(name):
	a = 2**1000000000
	print('solved')
	return a 

if __name__ == '__main__':
	p1 = []
	for i in range(30):
		p = Process(target=f, args=('bob',))
		p1.append(p)
		

	for p in p1:
		p.start()
		p.join()
