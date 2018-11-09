def solve(S):
	S = S.split()
	S.reverse()
	return S


def answer2(input_file_name, output_file_name):
	input_file = open(input_file_name)
	input_data = input_file.readlines()
	input_file.close()
	
	output_file = open(output_file_name, 'w')
	
	N = input_data[0]
	input_data = input_data[1:]
	N = int(N)
	
	for n in range(N):
		S = input_data[0]
		input_data = input_data[1:]
		S = S.rstrip()
		R = solve(S)
		output_file.write('Case #' + str(n+1) + ': ' + ' '.join(R) + '\n')
	
	output_file.close()
	
	return


def answer(input_file_name, output_file_name):
	input_file = open(input_file_name)
	input_data = input_file.readlines()
	input_file.close()
	
	output_file = open(output_file_name, 'w')
	
	N = int(input_data.pop(0))
	
	for n in range(N):
		S = input_data.pop(0)
		S = S.rstrip()
		R = solve(S)
		output_file.write('Case #' + str(n+1) + ': ' + ' '.join(R) + '\n')
	
	output_file.close()
	
	return