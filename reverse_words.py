#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  reverse_words.py
#  
#  Copyright 2014 ptjoker95 <ptjoker95@ptjoker95notebook>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from collections import namedtuple

Set = namedtuple("Set", ['index', 'words'])

import sys

def main(input_data):
	
	lines = input_data.split('\n')
	
	N = int(lines[0])
	
	sets = []
	
	for i in range(1, N+1):
		sets.append( Set( i-1, lines[i] ) )
	
	output = []
	result = ""
	
	for num, i in enumerate(sets):
		for j in i.words.split(' '):
			output.append(j)
		for k in reversed(output):
			result = result + k + " "
		print "Case #" + str(num+1) + ": " + result
		output = []
		result = ""
		
	return 0

if __name__ == '__main__':
	if len(sys.argv) > 1:
		file_location = sys.argv[1].strip()
		input_data_file = open(file_location, 'r')
		input_data = ''.join(input_data_file.readlines())
		input_data_file.close()
		main(input_data)
	else:
		print 'This test requires an input file.  Please select one from the data directory.'
	

