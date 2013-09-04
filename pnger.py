#!/usr/bin/python
'''

@author - e
@date   - 9/3/2013

'''
import sys
import argparse


fakeimage = "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a" +
            "\x00\x00\x00\x0d\x49\x48\x44\x52"+
            "\x00\x00\x00\x80\x00\x00\x00\x44"+
            "\x08\x02\x00\x00\x00\xc6\x25\xaa" +
            "\x3e\x00\x00\x00\xc2\x49\x44\x41" + 
            "\x54\x78\x5e\xed\xd4\x81\x06\xc3" + 
            "\x30\x14\x40\xd1\xb7\x34\xdd\xff" + 
            "\xff\x6f\xb3\x74\x56\xea\x89\x12" +
            "\x6c\x28\x73\xe2\xaa\x34\x49\x03" + 
            "\x87\xd6\xfe\xd8\x7b\x89\xbb\x52" +
            "\x8d\x3b\x87\xfe\x01\x00\x80\x00" +
            "\x00\x10\x00\x00\x02\x00\x40\x00" +
            "\x00\x08\x00\x00\x01\x00\x20\x00" + 
            "\x00\x04\x00\x80\x00\x00\x10\x00" + 
            "\x00\x02\x00\x40\x00\x00\x08\x00" +
            "\x00\x01\x00\x20\x00\x00\x00\xd4" +
            "\x5e\x6a\x64\x4b\x94\xf5\x98\x7c" +
            "\xd1\xf4\x92\x5c\x5c\x3e\xcf\x9c" +
            "\x3f\x73\x71\x58\x5f\xaf\x8b\x79" +
            "\x5b\xee\x96\xb6\x47\xeb\xf1\xea" +
            "\xd1\xce\xb6\xe3\x75\x3b\xe6\xb9" +
            "\x95\x8d\xc7\xce\x03\x39\xc9\xaf" +
            "\xc6\x33\x93\x7b\x66\x37\xcf\xab" +
            "\xbf\xf9\xc9\x2f\x08\x80\x00\x00" +
            "\x10\x00\x00\x02\x00\x40\x00\x00" +
            "\x08\x00\x00\x01\x00\x20\x00\x00" +
            "\x04\x00\x80\x00\x00\x10\x00\x00" +
            "\x02\x00\x40\x00\x00\x08\x00\x00" +
            "\x01\x00\x20\x00\x00\x8c\x37\xdb" +
            "\x68\x03\x20\xfb\xed\x96\x65\x00" +
            "\x00\x00\x00\x49\x45\x4e\x44\xae" +
            "\x42\x60\x82"



def pngit(infile, outfile, nowrite=0):
	outcounter = 0
	with open(outfile, "wb") as theoutf:		
		if nowrite == 0:
        		theoutf.write(fakeimage)
		with open(infile, "rb") as f:
			byte = f.read(1)
			while byte != "":
				if outcounter >= nowrite:
					theoutf.write(byte)	
				else:
					outcounter+=1
				

				byte = f.read(1)

def unpngit(infile, outfile):
	pngit(infile, outfile, 251)

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



