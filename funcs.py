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

def medianne(liste):

	l = sorted(liste)
	size = len(liste)

	if size < 1:
		return 0

	if size%2 == 0:
		return (l[ int((size - 1)/2)] + l[ int((size)/2)])/2.0 # moyenne entre les 2 valeurs mediannes
	else:

		return l[int((size-1)/2)]
