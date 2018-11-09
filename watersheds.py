def lowest_neighbor(i, j, H, W, altitude):
	lowest = (i, j)
	lowest_altitude = altitude[i][j]
	if i > 0 and altitude[i - 1][j] < lowest_altitude:
		lowest = (i - 1, j)
		lowest_altitude = altitude[i - 1][j]
	if j > 0 and altitude[i][j - 1] < lowest_altitude:
		lowest = (i, j - 1)
		lowest_altitude = altitude[i][j - 1]
	if j < W - 1 and altitude[i][j + 1] < lowest_altitude:
		lowest = (i, j + 1)
		lowest_altitude = altitude[i][j + 1]
	if i < H - 1 and altitude[i + 1][j] < lowest_altitude:
		lowest = (i + 1, j)
		lowest_altitude = altitude[i + 1][j]
	return lowest



def stack_DFS(adjacent_vertex, start_vertex, alphabet, label):
	connected_component = [start_vertex]
	stack = [start_vertex]
	(i, j) = start_vertex
	label[i][j] = alphabet
	while len(stack) > 0:
		v = stack.pop()
		for w in adjacent_vertex[v]:
			if w not in connected_component:
				connected_component += [w]
				stack += [w]
				(i, j) = w
				label[i][j] = alphabet
	return # ここではラベルをつけることが目的なので，何も返さなくて良い．




def labeling(H, W, adjacent_vertex):
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
				'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	#for i in range(H):
		#label += [[]]
		#for j in range(W):
			#label[-1] += ['']
	label = [['' for j in range(W)] for i in range(H)] # この1行で，コメントアウトされている直上の4行と同じである．
	for i in range(H):
		for j in range(W):
			if label[i][j] != '':
				continue
			stack_DFS(adjacent_vertex, (i, j), alphabet.pop(0), label)
	return label




def solve(H, W, altitude):
	#adjacent_vertex = {}
	#for i in range(H):
		#for j in range(W):
			#adjacent_vertex[(i, j)] = []
	adjacent_vertex = {(i, j): [] for i in range(H) for j in range(W)}
	# この1行で，コメントアウトされている直上の4行と同じである．
	
	for i in range(H):
		for j in range(W):
			neighbor = lowest_neighbor(i, j, H, W, altitude)
			adjacent_vertex[(i, j)] += [neighbor]
			adjacent_vertex[neighbor] += [(i, j)]
	label = labeling(H, W, adjacent_vertex)
	return label



def answer(input_file_name, output_file_name):
	input_file = open(input_file_name)
	output_file = open(output_file_name, 'w')
	T = int(input_file.readline())
	for case_number in range(1, T + 1):
		H, W = map(int, input_file.readline().split())
		altitude = []
		for h in range(H):
			altitude += [list(map(int, input_file.readline().split()))]
		label = solve(H, W, altitude)
		output_file.write('case #{0}:\n'.format(case_number))
		for h in range(H):
			output_file.write(' '.join(label[h]) + '\n')
	input_file.close()
	output_file.close()
	return
