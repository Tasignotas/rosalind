if __name__ == '__main__':
	f = open('rosalind_rna.txt', 'r')
	data = f.read()
	o = open('output.txt', 'w')
	o.write(data.replace('T', 'U'))