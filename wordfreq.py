#!/usr/bin/env python

'''
count the words in a text file and output the
sorted word frequency to a file
'''

import sys
import logging
import argparse
import operator
import re
from datetime import datetime

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--file', type=str, help='count words of this file')
	parser.add_argument('--out', type=str, help='output to this file')
	args = parser.parse_args()
	return [args.file, args.out]

def main():
	[infile, outfile] = parse_args()

	# build word freuency list from document 
	word_map = dict()
	with open(infile, 'r') as f:
		for line in f:
			words = line.split()
			for word in words:
				if word[-1] == '-' or word[0] == '-':
					continue # ignore words split by new line
				if '/' in word or '\\' in word:
					continue # ignore websites

				# normalize each word
				word = str(re.sub(r'[^A-z\']+', '', word).lower())
				word = re.sub(r'[\`\']+$', '', word)
				word = re.sub(r'^[\`\']+', '', word)

				if not word:
					continue # empty strings
				elif not word_map.get(word):
					word_map[word] = 1
				else:
					word_map[word] += 1

	# sort and output the list into a text doc
	sorted_word_map = sorted(word_map.items(), key=operator.itemgetter(1), reverse=True)
	if outfile:
		with open(outfile, 'w') as out:
			for element in sorted_word_map:
				out.write(str(element))
				out.write('\n')
	else:
		for element in sorted_word_map:
			print(str(element))

	return 0

# run as a standalone script
if __name__ == '__main__':
	sys.exit(main())