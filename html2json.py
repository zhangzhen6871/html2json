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

for ul1 in soup.find_all('ul'):
	print(ul1.text.strip())
	for li1 in ul1.find_all('li', recursive=False):
		print("& " + li1.text.strip())
		for ul2 in li1.find_all('ul', recursive=False):
			print("   * " + ul2.text.strip())
			for li2 in ul2.find_all('li', recursive=False):
				print("      # " + li2.text.strip())
	print "--------------------------------------------------"
