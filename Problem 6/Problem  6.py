if __name__ == '__main__':
	i = open('rosalind_hamm.txt', 'r')
	data = i.read()
	
	str1 = data.split('\n')[0]
	str2 = data.split('\n')[1]
	
	diffcnt = 0
	
	for i in range(0, len(str1)):
		if str1[i] != str2[i]:
			diffcnt += 1
	
	print diffcnt