#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from bs4 import BeautifulSoup

#if len(sys.argv) != 2:
#	print "Usage: html2json <input_file>"
#	sys.exit(2)

try:
	#input_file = open(sys.argv[1])
	input_file = open("input2.html")
except IOError:
	print "File \"%s\" not found" % sys.argv[1]
	sys.exit(2)

soup = BeautifulSoup(input_file)

i = 0
for ul in soup.findAll('ul'):
	for li in ul.findAll('li'):
		print i + ": " + li.text
		i = i + 1
