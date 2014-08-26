from multiprocessing import Process, Queue, Pool
from subprocess import call
import sys
import re, codecs, Queue, os
import time

ScrapeQueue = Queue.Queue()

def fork(toDo):
	sys.stdout = open('log.txt', 'w')
	start = time.time()
	print start
	os.chdir("/home/matth/new-coder/scrape/")
	print "Acquired scrape: %s"%(toDo)
	name = "%s"%(toDo).replace(".py","")
	call(["mkdir", "-p", name])
	call(["cp", toDo, "-t", name])
	os.chdir("./%s"%name)
	print call(["python", name + ".py"])
	cfile = re.compile("^.*csv$")
	for fname in os.listdir("/home/matth/new-coder/scrape/%s"%(name)):
		if cfile.match(fname):
			csvfile = fname
	print "Completed %s"%(toDo)
	print "Filename written:"
	print name
	print "Number of rows:"
	print open('%s'%(csvfile), 'r').read().count("\n")
	print "Completed in:"
	print str(time.time() - start)

if __name__ == '__main__':
	p = Pool(2)
	ScrapeQueue = []
	i=1
	for line in codecs.open("sourcelist.txt","r","utf-8"):
		ScrapeQueue.append(line.strip())
	print ScrapeQueue
	p.map(fork, ScrapeQueue)
