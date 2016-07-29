from pyspark import SparkContext
from pyspark import SparkConf
import time

# from pyspark import testpy

# rdd.filterTotalTime = 0

conf = SparkConf().setAppName("test")
sc = SparkContext(conf = conf)

global times
times = [0]

def incChar(line):
	lineLen = len(line)
	newL = ""
	for i in range (lineLen):
		newL += chr(ord(line[i])+1)
	print newL

def f(split,iterator):
	it = iterator
	global times
	tmp = it.next()
	print "tmp is " + str(tmp)
	times.append(tmp)
	print "partition id is " + str(split)
	yield float(tmp)/1000000


while True:
	time.sleep(2)
	print "starting..."
	print "map split"
	# print "filter len(25,30)"
	# print "filter word <feed>"
	# print "flatMap split"
	st= time.time()
	tfile = sc.textFile("tt.xml")
	tfile1 = tfile.repartition(6)
	# tfile.cache()
	# tfile.take(5)
	#tfile.saveAsTextFile("testFiles")
	#tfile.foreach(f)
	# fmapped = tfile1.flatMap(lambda line : line.split())
	mapped = tfile1.map(lambda line : line.split())
	filtered = mapped.filter(lambda word : len(word) in range (25,50))
	# filtered = tfile1.filter(lambda word : word == "<feed>")
	fourLetterWords = filtered.flatMap(lambda word : (word,1))
	#op = fourLetterWords.reduceByKey(lambda a,b : a+b)
	'''lineCount = tfile.map(lambda line: line.split())
	numCount = tfile.filter(lambda x: x if (x.isdigit() == True) else '')
	print "Number Count is " + str(numCount.count())
	print "Line Count is " + str(lineCount.count())'''
	# print "transform and take 1000000 action \n"
	# print "\n\ntransform and count action \n"
	# ct1 = time.time()
	#print "\ntotal count is " + str(tfile.count())
	# ct2 = time.time()
	#print "\ncount is " + str(filtered.count())
	# print "\n\ncaching\n\n"
	# filtered.cache()
	# print "\n\ncaching command sent\n\n"
	# filtered.take(5)
	# time.sleep(5)
	# print "\n\n\ntake again\n\n\n"
	# print filtered.take(80)
	# filtered.take(1000000)
	# mapped.take(1000000)
	# fmapped.take(1000000)
	# print "taken 1000000"
	filtered.saveAsTextFile("testFiles")
	#print "\ncount is " + str(fmapped.count())
	# tcount = filtered.count()
	# temp = filtered.take(1000000)
	# print type(temp)
	# filtered.foreach(f)
	et = time.time()
	# filtered.mapPartitionsWithIndex(f).sum()
	# print mapped.take(5)
	# print "time taken to reach count command is " + str(ct1 - st)
	# print "count1 time taken is " + str(ct2 - ct1)
	# print "count2 time taken is " + str(et - ct2)
	print "total time taken is " + str(et - st)
	# print times
	# print "\ncount is " + str(tcount)
	# print "fn takes time = "
	# print(testpy.filterTotalTime)
	#print "unpersisting"
	#tfile.unpersist()
	#filtered.unpersist()
	#print "unpersisting done..."
	#filtered.saveAsTextFile("testFiles")
#	time.sleep(5)
	break



