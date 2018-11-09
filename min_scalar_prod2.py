import numpy

############順列を列挙する関数##########################
def enumerate_all_permutations(sequence):
	permutations = [] # 順列を保存するためのリスト
	S = [([], sequence)] # 「順列の部分列」と「部分列で使われていない残り」の組をスタックに保存する．
	while len(S) > 0: # スタックが空でない限り以下を繰り返す．
		subsequence, remaining = S.pop() # スタックから（「部分列」，「残り」）を1つ取り出す．
		if len(remaining) == 0: # 「部分列で使われていない残り」が空ならば，部分列は順列になっているはずなので，
			permutations += [subsequence] # その部分列を順列に加える．
		else: # 「部分列で使われていない残り」があるならば
			for r in remaining: # その残りのそれぞれに関して，
				remaining_copy = remaining[:] 
				remaining_copy.remove(r) # 残りを1つ取り除いて，
				S += [(subsequence + [r], remaining_copy)] # それを部分列に追加した列と残りをスタックに入れる．
	return permutations # 最後にまとめて，全ての部分集合を返す．


def solve(x, y, n):
	Px = enumerate_all_permutations(x)
	Py = enumerate_all_permutations(y)
	#print(Px) #確認用
	prod = 0
	minprod = 100000000000
	for i in range(n):
		for j in range(n):
			prod = Px[i][i] * Py[j][j]       #ここら辺のfor文間違えてる
				if prod < minprod:
					minprod = prod
	return minprod


def answer(input_file_name, output_file_name):
	input_file = open(input_file_name)
	output_file = open(output_file_name, 'w')
	T = int(input_file.readline())
	for case_number in range(1, T + 1):
		n = int(input_file.readline())
		x = input_file.readline().split()
		for i in range(n):
			x[i] = int(x[i])
		y = input_file.readline().split()
		for i in range(n):
			y[i] = int(y[i])
		output_file.write('Case #{0}: {1}\n'.format(case_number, solve(x, y, n)))	
	input_file.close()
	output_file.close()
	return






########################################模範解答#####################################
def scalar_product(x, y):
	prod = 0
	for x_i, y_i in zip(x, y):
		prod += x_i * y_i
	return prod


def solve1(x, y):
	minimum_scalar_prod = scalar_product(x, y)
	stack = [([], x)]
	while len(stack) > 0:
		subsequence, remaining = stack.pop()
		if len(remaining) == 0:
			scalar_prod = scalar_product(subsequence, y)
			if scalar_prod < minimum_scalar_prod:
				minimum_scalar_prod = scalar_prod
		else:
			for r in remaining:
				remaining_copy = remaining[:]
				remaining_copy.remove(r)
				stack += [(subsequence + [r], remaining_copy)]
	return minimum_scalar_prod


def answer(input_file_name, output_file_name):
	input_file = open(input_file_name)
	output_file = open(output_file_name, 'w')
	T = int(input_file.readline())
	for case_number in range(1, T + 1):
		n = int(input_file.readline()) # 実はここで読み込んだ整数nはこれ以降で使っていない．
		x = list(map(int, input_file.readline().split()))
		y = list(map(int, input_file.readline().split()))
		output_file.write('Case #{0}: {1}\n'.format(case_number, solve1(x, y)))
	input_file.close()
	output_file.close()
	return
