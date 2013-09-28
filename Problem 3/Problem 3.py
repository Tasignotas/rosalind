
if __name__ == '__main__':
	i = open('input.txt', 'r')
	data = i.read()
	
	data = data[::-1]
	
	data = data.replace('A', 'B')
	data = data.replace('T', 'A')
	data = data.replace('B', 'T')
	
	data = data.replace('G', 'B')
	data = data.replace('C', 'G')
	data = data.replace('B', 'C')
	
	o = open('output.txt', 'w')
	o.write(data)
	
	print data
	
	
	# Better use string.maketrans!!!
	