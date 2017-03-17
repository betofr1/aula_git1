def maior (lista):
	if len(lista) == 0:
		return 0
	m = lista[0]
	for i in range(1,len(lista)):
		if lista[i] > m:
			m = lista[i]
	return m
