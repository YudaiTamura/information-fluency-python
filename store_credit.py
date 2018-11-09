def solve(C, P):
	for i in range(len(P)-1):
		for j in range(i+1, len(P)):
			if P[i]+P[j] == C:
				return i+1, j+1


def answer(input_file_name, output_file_name):
	input_file = open(input_file_name)
	input_data = input_file.readlines()
	input_file.close()
	
	output_file = open(output_file_name, 'w')
	
	N = int(input_data.pop(0))
	for n in range(N):
		C = int(input_data.pop(0))
		I = int(input_data.pop(0))
		P = input_data.pop(0)
		P = P.split()
		for i in range(len(P)):
			P[i] = int(P[i])
		i, j = solve(C, P)
		output_file.write('Case #{0}: {1} {2}\n'.format(str(n+1), str(i), str(j))) 
		
	output_file.close()
	return