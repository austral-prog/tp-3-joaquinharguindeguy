def slice_simple():
	texto = "Awesome"
	medio= (int(int(len(texto))/2))
	
	print(texto.lower()[:3])
	print(texto.lower()[medio-1 : medio+2])
	print(f'{texto.lower()[:4:]}{texto.lower()[4::]}')

	
