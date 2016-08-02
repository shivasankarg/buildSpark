from pyspark import SparkContext
from pyspark import SparkConf
import time

conf = SparkConf().setAppName("test")
sc = SparkContext(conf = conf)

time.sleep(2)
print "starting..."
st= time.time()
tfile = sc.textFile("/home/seamus4318/Downloads/enwiki-latest-abstract.xml")
# tfile = sc.textFile("README.md")
tfile = tfile.repartition(6)
mapped = tfile.map(lambda line : line.split())
filtered = mapped.filter(lambda word : len(word) in range (25,50))
fmapped = filtered.flatMap(lambda word : (word,1))
fmapped.saveAsTextFile("/home/seamus4318/Downloads/testFiles")
et = time.time()
print "total time taken is " + str(et - st)

