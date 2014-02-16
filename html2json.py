#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
	print "Usage: html2json <input_file>"
	sys.exit(2)

try:
	input_file = open(sys.argv[1])
except IOError:
	print "File \"%s\" not found" % sys.argv[1]
	sys.exit(2)

soup = BeautifulSoup(input_file)

for ul in soup.find_all('ul'):
	print "--------------------------------------------------"
	for li in ul.find_all('li'):
		print(li)
	print "--------------------------------------------------"
