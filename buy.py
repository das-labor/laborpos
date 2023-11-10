#!/usr/bin/env python3
import sys
import cgi
import json
import datetime
import time
import os
import html
from email import utils

print("Content-type:text/html\r\n\r\n",end="")

try:
	fh = open("db/boughts", "a")
except IOError:
	sys.exit("Failed to open the database file");

post = cgi.FieldStorage()
boughts = json.loads(post["data"].value);
method = "B" if post["method"].value == "1" else "C" if post["method"].value == "2" else "S"
nowdt = datetime.datetime.now()
nowtuple = nowdt.timetuple()
nowtimestamp = time.mktime(nowtuple)
date = utils.formatdate(nowtimestamp)
ip = os.environ["REMOTE_ADDR"]
printstr = ""

for bought in boughts:
	product = html.unescape(bought["product"]);
	fh.write(date + "\t" + ip + "\t" + str(bought["price"]) + "\t" + method + "\t" + product + "\n")
	
	price = "{:6.2f}".format(bought["price"]).replace(".", ",")
	printstr += (nowdt.strftime("%d.%m. %H:%M:%S") + " " + price + " € " + method + " " + product)[:44] + "\n"

fh.close()

#s = open("/dev/ttyUSB0", "wb")
#s.write(b"\x1b\x52\x06")		# cp858

#def printout(st):
#	s.write(st.encode("cp858"))
#	s.flush()

#printout(printstr)

print("OK",end="")
