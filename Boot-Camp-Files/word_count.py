def words(Input):
	
	inputs = Input.split()
	seclist = list(inputs)
	result = {}
	
	
	for w in seclist:
	
		try:
			i = int(w)
		except ValueError:
			result[w] = inputs.count(w)
		else:
			result[i] = inputs.count(w)
	return result
