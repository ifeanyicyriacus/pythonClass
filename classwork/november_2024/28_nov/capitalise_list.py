def capitalise_list(word_list:list) -> list:
	return [x.lower().capitalize() for x in word_list]
	#return [(x[0].upper() + x[1:].lower()) for x in word_list]
