if __name__ == '__main__':
	
	i = open('rosalind_gc.txt', 'r')
	data = i.read()
	data = data.split('>')[1:]
	
	for i in data:
		sample = i.split('\n')
		name = sample[0]
		seq = ('').join(sample[1:])
		cnt = seq.count('G') + seq.count('C')
		print name
		print '%.6f' % ((cnt * 100.0) / len(seq))