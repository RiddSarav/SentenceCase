def SentenceCase(string):
	string=str(string)
	new_list = string.split(" ")
	new_list2 = new_list[0]
	all_charectars = list(new_list2)	
	all_charectars[0] = all_charectars[0].upper()
	print("".join(all_charectars))

