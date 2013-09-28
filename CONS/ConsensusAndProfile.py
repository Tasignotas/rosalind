# Problem ID: CONS
import re

if __name__ == '__main__':
	f = open('input.txt', 'r')
	
	strands = [x.strip() for x in f.readlines()]

	matrix = zip(*strands)

	profile_matrix = map(lambda x: dict((base, x.count(base)) for base in "ACGT"), matrix)

	consensus = [max(x,key = x.get) for x in profile_matrix]

	print "".join(consensus);

	for base in "ACGT":
		print base+":",
		for x in profile_matrix:
			print x[base],
		print ""