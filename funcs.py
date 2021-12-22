def minimum_int(liste):
	m = liste[0]

	for i in liste:
		if m > i:
			m = i;
	return m