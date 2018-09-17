def divide(n1, n2):
	if n2 == 0:
		return None
	if n1 == 0:
		return '0'
	integar = str(n1 / n2)
	reminder = n1 % n2
	re = ''
	flag = 0
	while reminder:
		tmp = reminder * 10 / n2
		tmp_rem = reminder * 10 % n2
		if tmp_rem == 0:
			re += str(tmp)
			break
		else:
			if str(tmp) in re:
				flag = 1
				break
			re += str(tmp)
			reminder = tmp_rem
		
	if not re:
		return integar
	if flag == 0:
		return integar+'.'+re
	else:
		for i in range(len(re)):
			if re[i] == str(tmp):
				s = i
				break
		return integar + '.' + re[:i]+ '(' + re[i:] + ')'

print 4,'/',2,'-->',divide(4,2)
print 2,'/',4,'-->',divide(2,4)   
print 1,'/',3,'-->',divide(1,3)
print 131,'/',7,'-->',divide(131,7)
print 2113,'/',9900,'-->',divide(2113,9900)

