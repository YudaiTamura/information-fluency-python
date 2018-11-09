import math

####特性列と集合を元に，部分集合を返す関数#######
def subset_from_vector(v, pancakes):
	if len(v) != len(pancakes):
		return []
	subset = []
	for vi, element in zip(v, pancakes):
		if vi == 1:
			subset += [element]
	return subset


#########部分集合を列挙する関数#######################
def enumerate_all_subsets(pancakes):
	subsets = [] # 部分集合を保存するためのリスト
	S = [[]] # スタック
	while len(S) > 0: # スタックが空でない限り以下を繰り返す．
		v = S.pop() # スタックから0-1列を1つ取り出す．
		if len(v) == len(pancakes): # 0-1列が集合の要素数と同じ長さならば，
			subsets += [subset_from_vector(v, pancakes)] # その0-1ベクトルが特性列であると見なして，部分集合を作り，保存する．
		else: # 0-1列が集合の要素数よりも短いならば，
			S += [v + [0]] # それに0を追加した列をスタックに入れる．
			S += [v + [1]] # それに1を追加した列もスタックに入れる．
	return subsets # 最後にまとめて，全ての部分集合を返す．


def solve(pancakes, K):
	subsets = enumerate_all_subsets(pancakes)
	#print(subsets) #確認用
	maxAS = 0 #ASは最大の表面積
	for i in range(len(subsets)):
		if len(subsets[i]) == K:
			#一番下のパンケーキの半径rmaxを取り出しつつ、パンケーキの横の面積の合計SSを計算
			rmax = 0
			r = []
			h = []
			SS = 0
			for j in range(len(subsets[i])):
				r = int(subsets[i][j][0]) # rはパンケーキの半径
				h = int(subsets[i][j][1]) # hはパンケーキの高さ
				if r > rmax:
					rmax = r
				SS += 2 * math.pi * r * h # SSはパンケーキの横側の面積の合計
			AS = SS + math.pi * rmax**2 #ASはパンケーキ全体の表面積
			if AS > maxAS: # 最大かどうか判断する
				maxAS = AS
	return maxAS


def answer(input_file_name, output_file_name):
	input_file = open(input_file_name)
	output_file = open(output_file_name, 'w')
	T = int(input_file.readline()) #テストケース数
	for case_number in range(1, T + 1):
		C = input_file.readline().split() #C[0]=N, C[1]=Kになる
		N = int(C[0])
		K = int(C[1])
		pancakes = []
		for n in range(N):
			pancakes += [input_file.readline().split()] #pancakesの中にそれぞれのパンケーキのrとhの情報が入ってる
		#print(pancakes) #確認用
		output_file.write('Case #{0}: {1}\n'.format(case_number, solve(pancakes, K)))
	input_file.close()
	output_file.close()
	return





###################模範解答#################
import math # 円周率πを使いたいので数学関数モジュールをimportする．


def syrup_area(pancake):
	'''パンケーキの集合が与えられたら，シロップのかかる面積を返す関数．
	'''
	
	pancake.sort() # 最大半径のパンケーキを見つけるため，半径で並べ替える．（別途最大半径を見つけても良い．）
	area = math.pi * pancake[-1][0] ** 2 # まず上から見た面積（＝最大半径のパンケーキの上面積）を代入し，
	for radius, height in pancake: # それぞれのパンケーキに関して，
		area += 2 * math.pi * radius * height # 側面積を加える．
	return area


def solve1(N, K, pancake):
	'''パンケーキにかかる面積の最大値を返す関数．
	'''
	
	maximum_syrup = 0 # シロップの面積の下限を代入しておく．
	stack = [[]]
	while len(stack) > 0:
		v = stack.pop()
		if len(v) == len(pancake): # パンケーキの部分集合に関して，
			if sum(v) != K: # 部分集合の枚数がKでないならば
				continue # 計算を省略する．
			subset = [] # 特性列vからパンケーキの部分集合を計算する．
			for vi, p in zip(v, pancake):
				if vi == 1:
					subset += [p]
			sa = syrup_area(subset) # パンケーキの部分集合からシロップの面積を計算する．
			if sa > maximum_syrup: # シロップの面積がそれまでの最大値よりも大きかったら，
				maximum_syrup = sa # 最大値を更新する．
		else:
			stack += [v + [0]]
			stack += [v + [1]]
	return maximum_syrup


def answer1(input_file_name, output_file_name):
	input_file = open(input_file_name)
	output_file = open(output_file_name, 'w')
	T = int(input_file.readline())
	for case_number in range(1, T + 1):
		N, K = map(int, input_file.readline().split())
		pancake = []
		for n in range(N):
			radius, height = map(int, input_file.readline().split())
			pancake += [(radius, height)]
		output_file.write('Case #{0}: {1:.6f}\n'.format(case_number, solve1(N, K, pancake)))
		# .6fは「小数点以下6桁で，少数で表示する」という意味である．
	input_file.close()
	output_file.close()
	return
