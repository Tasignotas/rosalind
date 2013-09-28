if __name__ == '__main__':

	# Setting up a dictionary for nucleobase count
	# Admittedly, not the very best thing to do efficiency wise...
	base_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
	f = open('rosalind_dna.txt', 'r')
	data = f.read()
	
	# Counting the number of bases:
	for i in data:
		if i in base_dict.keys():
			base_dict[i] += 1
			
	# Printing the results:
	for i in base_dict.keys():
		print i, ':', base_dict[i]
		
		
		
	# Much more clever:
	# print 'A :', data.count('A'), 'C :', data.count('C'), 'T :', data.count('T'), 'G :', data.count('G') 