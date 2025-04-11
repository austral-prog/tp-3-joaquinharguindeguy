def check_vowels():
	name2= (f'\n\n{(input("> "))}')
	print(f'\n\nContiene a: {"a" in name2}\nContiene e: {"e" in name2}\nContiene i: {"i" in name2}\nContiene o: {"o" in name2}\nContiene u: {"u" in name2}\n')

	name1= (f'\n\n{(input("> "))}')
	name= (name1.lower())
	print(f'\n\nContiene a: {"a" in name}\nContiene e: {"e" in name}\nContiene i: {"i" in name}\nContiene o: {"o" in name}\nContiene u: {"u" in name}\n')

check_vowels()
