#testing
from multiprocessing import Process, Queue, Pool
from subprocess import call
import sys
import re, codecs, Queue, os
import time

ScrapeQueue = Queue.Queue()

def fork(toDo):
	name = "%s"%(toDo).replace(".py","")
	dir = os.getcwd()
	os.chdir(dir)
	print "Acquired scrape: %s"%(toDo)
	call(["mkdir", "-p", name])
	call(["cp", toDo, "-t", name])
	os.chdir("./%s"%name)
	sys.stdout = open('log.txt','w')
	print call(["python", name + ".py"])
	start = time.time()
	cfile = re.compile("^.*csv$")
	for fname in os.listdir(dir + "/" + "%s"%(name)):
		if cfile.match(fname):
			csvfile = fname
	print "Completed %s"%(toDo)
	print "Filename written:"
	print csvfile
	print "Number of rows:"
	print open('%s'%(csvfile), 'r').read().count("\n")
	print "Completed in:"
	print str(time.time() - start)

if __name__ == '__main__':
	p = Pool(4)
	ScrapeQueue = []
	i=1
	for line in codecs.open("sourcelist.txt","r","utf-8"):
		ScrapeQueue.append(line.strip())
	print ScrapeQueue
	p.map(fork, ScrapeQueue)
