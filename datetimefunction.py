import os

def buldfilename(str):
	tmp = str[5:10].replace('-','')
	#print(tmp)
	tmp += '-' + str[11:].replace(':','') +'.jpg'
	#print(tmp)
	return tmp

def CheckImageDir(basepath, timestamp):
	'''
	passes a timestamp value in the format of %Y-%m-%d-%H-%M-%S %sss
	checks to see if the day_path and hour_path exists, if not then 
	the paths are created

	returns the hour_path
	'''
	# basepath = "/home/pi/python/images"
	#basepath = "/home/pi/images"
#	print("basepath exists {}".format(os.path.isdir(basepath)))
	#x = timestamp.split('-')

	#folder = x[0][-2:]+x[1]+x[2]

	folder = timestamp[2:4]
	folder += timestamp[5:7]
	folder += timestamp[8:10]

	day_path = os.path.join(basepath,folder)

	if os.path.isdir(day_path) is False:
		print("Need to create a new directory with the current date")
		os.mkdir(day_path)

	hour_path = os.path.join(day_path,timestamp[11:13])

	if os.path.isdir(hour_path) is False:
		print("Need to create hour directory in the date path")
		os.mkdir(hour_path)

#	print(hour_path)
	return hour_path


def GetMinutes(timestamp):
    mins = float(timestamp[14:16])
    return mins


	#print("The hour path is {}".format(hour_path))
#print(day_path)
#print(timestamp)
#print(x)
#print(folder)

if __name__ == '__main__':
	import datetime
	timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S %f")[:-2]
	CheckImageDir("/home/pi/images",timestamp)