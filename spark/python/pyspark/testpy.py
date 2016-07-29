import rdd

global SHIVAlog 
SHIVAlog = 0

global filterTotalTime
filterTotalTime = 0

class calcTime(object):
	# global filterTotalTime
	filterTotalTime = 0

	# global mapTotalTime
	mapTotalTime = 0

	# global flatMapTotalTime
	flatMapTotalTime = 0

	# global timeT
	timeT = None

	def setTime(timeToSet):
		# global timeT
		timeT = timeToSet
		print "setTime is "	 + str(timeT)

	def getTime():
		# global timeT
		return timeT

global c
c = calcTime()