def solve(x, y):
	x.sort() # x�������ɕ��בւ���D
	y.sort(reverse=True) # y���~���ɕ��בւ���D
	prod = 0
	for x_i, y_i in zip(x, y):
		prod += x_i * y_i # ����� prod = prod + x_i * y_i �Ɠ����D
	return prod
	
	
def answer(input_file_name, output_file_name):
	input_file = open(input_file_name)
	input_data = input_file.readlines()
	input_file.close()
	
	output_file = open(output_file_name, 'w')
	
	T = int(input_data.pop(0))
	for case_number in range(1, T + 1):
		n = int(input_data.pop(0))
		x = input_data.pop(0)
		x = x.split()
		for i in range(n):
			x[i] = int(x[i])
		y = input_data.pop(0)
		y = y.split()
		for i in range(n):
			y[i] = int(y[i])
		output_file.write('Case #{0}: {1}\n'.format(case_number, solve(x, y)))
	
	output_file.close()
	
	return
