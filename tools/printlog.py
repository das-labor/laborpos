#!/usr/bin/env python3
import email.utils
import datetime

fh = open("../db/boughts")
boughts = fh.readlines()
from_line = 660

s = open("/dev/ttyUSB0", "wb")
s.write(b"\x1b\x52\x06")		# cp858

def printout(st):
	s.write(st.encode("cp858"))
	s.flush()

for bought in boughts:
	if from_line > 1:
		from_line -= 1
		continue
		
	(datestr, ip, pricetext, product) = bought.strip().split("\t")
	date = datetime.datetime.utcfromtimestamp(email.utils.mktime_tz(email.utils.parsedate_tz(datestr)))
	price = "{:6.2f}".format(float(pricetext)).replace(".", ",")
	printstr = (date.strftime("%d.%m. %H:%M:%S") + " " + price + " €  " + product)[:44] + "\n"

	print(printstr, end="")
	printout(printstr)
