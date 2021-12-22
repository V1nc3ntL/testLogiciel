def minimum_int(liste):
	
	if liste == []:
		return 0

	m = liste[0]
	for i in liste:
		if m > i:
			m = i;
	return m