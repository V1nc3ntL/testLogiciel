def minimum_int(liste):
	
	if liste == []:
		return 0

	m = liste[0]
	for i in liste:
		if m > i:
			m = i;
	return m

def moyenne(liste):
	
	if liste == []:
		return 0

	somme = 0;
	length = len(liste)
	
	for i in range(0, length):
		somme = somme + liste[i]
	return somme/length