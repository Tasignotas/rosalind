# Problem 9


if __name__ == '__main__':
	i = open('rosalind_subs.txt', 'r')
	s = i.readline().strip()
	t = i.readline().strip()
	i.close()

	ans = ''
	
	for i in range(0, len(s) - len(t) + 1):
		print s[i:i+len(t)]
		if s[i:i+len(t)] == t:
			ans = ans + str(i+1) + ' '
				
	o = open('rosalind_subs_out.txt', 'w')
	o.write(ans)
	o.close()