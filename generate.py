
def generator(num_letters):
	from random import randint
	available = 'abcdefghijklmnopqrstuvwABCDEFGHIJKLMNOPQRSTUVW0123456789'
	result = ''
	for i in range(num_letters):
		result += available[randint(0, -1+len(available))]
	return result+'='

[print(generator(x)) for x in range(5, 100)]	
