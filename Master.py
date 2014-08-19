from multiprocessing import Process, Queue, Pool
from subprocess import call
import re, codecs, Queue

ScrapeQueue = Queue.Queue()

def fork(toDo):
	print "Acquired scrape: %s"%(toDo)
	call(["python", "%s"%toDo])
	print "Completed %s"%(toDo)

if __name__ == '__main__':
	p = Pool(5)
	ScrapeQueue = []
	i=1
	while i < 11:
		ScrapeQueue.append("random%d.py"%i)
		i+=1
	print ScrapeQueue
	p.map(fork, ScrapeQueue)
