# Script:		internet_speed_monitor.py
#
# Python:		python 2.7
#
# Purpose:		This script is used to check the speed of
#				an internet connection using speedtest-cli
#				library. It saves results in a log file.
#				It also makes a graph of the previous days
# 				results.
#
# Requirements:	numpy - 		sudo pip install numpy
# 				matplotlib - 	sudo pip install matplotlib
#				speedtest-cli - sudo pip install speedtest-cli
#
# Author:		Billy O Sullivan
#


### import library

import speedtest
import time
import os
import numpy as np
import pylab as pl
from time import ctime

### speed function - get readings from speedtest.com
def speed(dtime):
	s = speedtest.Speedtest()
	server = s.get_best_server()
	down = s.download()
	up = s.upload()
	dl = str(down/1000000) 					# convert to mbps
	dl = dl[:5]
	upl = str(up/1000000)	
	upl = upl[:5]
	speedlog = open('speed.txt','a+')
	down = 'download speed ' + dl + '\n'
	up = 'upload speed ' + upl + '\n\n'
	curtime = 'time: ' + dtime + '\n'
	speedlog.write(curtime)
	speedlog.write(down)
	speedlog.write(up)
	speedlog.close()

### logsort function - ensures possibility for a months logs	
def logsort(dtime):
	old = open('speed.txt','r')
	olddata = old.read()
	old.close()
	newlog = 'speed_'+ dtime + '.txt' 		# files named speed_<date>.txt, such as speed_17.txt
	new = open(newlog,'w')
	new.write(olddata)
	new.close()
	clean = open('speed.txt','w')
	firstline = 'Date: ' + ctime() + '\n'
	clean.write(firstline)
	clean.close()

### graph function - makes a graph of previous days logs	
def graph(splitdate):
	logfile = 'speed_' + splitdate + '.txt'
	y = []
	x1 = []
	x2 = []
	with open(logfile) as data:
		for line in data:
			if line.strip():
				line = line.split()
				if line[0] == 'Date:':
					gtitle = line[0] + ' ' + line[1] + ' ' + line[3] + ' ' + line[2]
				if line[0] == 'time:':
					ytime = line[1]
					ytime = ytime.split(':')
					ytime = ytime[0] + '.' + ytime[1]
					ytime = float(ytime)
					y.append(ytime)
				if line[0] == 'download':
					num = float(line[2])
					x1.append(num)
				if line[0] == 'upload':
					num = float(line[2])
					x2.append(num) 	
	data.close()
	plot1, = pl.plot(y,x1,'r')
	plot2, = pl.plot(y,x2,'b')
	pl.title(gtitle)
	pl.ylabel('mb/s mega-bits per second')
	pl.xlabel('Time')
	pl.xlim(00.00, 24.00)
	pl.ylim(0.00, 100.00)
	pl.legend([plot1,plot2],['Download','Upload'], loc='best', numpoints=1)
	name = 'speed_' + splitdate + '.png'
	pl.savefig(name, bbox_inches='tight')
	
### main function
def main():
	firsttime = 0
	while True:
		try:
			if firsttime == 0:
				clean = open('speed.txt','w')
				firstline = 'Date: ' + ctime() + '\n'
				clean.write(firstline)
				clean.close()
				firsttime = firsttime + 1
			splitctime = ctime().split()
			splittime = splitctime[3].split(':')
			splitday = splitctime[0]
			splitdate = splitctime[2]
			if splittime[1] == '00' or splittime[1] == '15' or splittime[1] == '30' or splittime[1] == '45':
				if splittime[0] == '23' or splittime[0] == '00':
					with open('speed.txt','r') as f:
						fline = f.readline()
					f.close()
					fline = fline.strip() 					# deal with white space
					fline = fline.split()
					if fline[0] == 'Date:':	
						daydoc = fline[1]
					if splitday != daydoc:
						logsort(splitdate)
						graph(splitdate)		
				speed(splitctime[3])		
		except:
			print 'error: ' + splitctime[3]
	
if __name__ == "__main__":
	main()


