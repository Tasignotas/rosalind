def newfib(n, k, val):
	if val[n] != -1
		return val[n]
	else:
		return newfib(n-1, k) + k * newfib(n-2, k)
		
		
if __name__ == '__main__':
	o = open('output.txt', 'w')
	val = [0, 1, 1] + [-1] * 37
	data = newfib(29, 2, val)
	o.write(str(data))