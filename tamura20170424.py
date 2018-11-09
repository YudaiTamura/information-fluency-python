def twice(x):
	y = 2*x
	return y
	
	
def wa(x, y):
	return x+y
	
	
def shou_amari(x, y):
	print(x//y)
	print(x%y)
	return
	
def basic_calc(x, y):
	return x+y, x-y, x*y, x/y, x%y
	
	
def body_mass_index(height, weight):
	bmi = weight/(height**2)
	if bmi >= 25:
		return 'fat'
	else:
		return 'not fat'
	
	
def body_mass_index2(height=1.7, weight=70):
	bmi = weight/(height**2)
	if bmi >= 25:
		return 'fat'
	else:
		return 'not fat'
	
	
def body_mass_index3(height=1.7, weight=70):
	bmi = weight/(height**2)
	if bmi >= 25:
		return 'デブ'
	elif bmi >= 18.5:
			return '凡'
	else:
		return 'ガリ'