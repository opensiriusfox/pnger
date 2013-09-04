#!/usr/bin/python
'''

@author - e
@date   - 9/3/2013



'''
import sys
import argparse

def pngit(infile, outfile):

	with open(outfile, "wb") as theoutf:
        	theoutf.write("\x89\x50\x4E\x47\x0D\x0A\x1A\x0A")
		with open(infile, "rb") as f:
			byte = f.read(1)
			while byte != "":
				theoutf.write(byte)	
				byte = f.read(1)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('-i', '--input', help='the input file you want to perform a png or unpng operation on.')
	parser.add_argument('-o', '--output', help='the output file after the png or unpng operation.')
	parser.add_argument('-u', '--unpng', action='store_true', help='use this flag to unpng a file that looks like a png file')

	args = parser.parse_args()

	if (not (args.input or args.output)):
        	print "Usage:"
        	print "\tpython pnger.py -i <from_file> -o <to_file> [optional] -u"
        	print "Example:"
        	print "\tpython pnger.py -i NSASecrets.txt -o NSASecrets.png"
        	print "\tpython pnger.py -i example.cpp    -o ireallyenjoycarpeting.png"
        	print "\tpython pnger.py -i example.png    -o example.cpp --unpng"
	else:
		if args.unpng:
			unpngit(args.input, args.output)	
		else:
			pngit(args.input, args.output)



