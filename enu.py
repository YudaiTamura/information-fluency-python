def subset_from_vector(v, a_set):
	'''特性列と集合を元に，部分集合を返す関数．
	'''
	
	if len(v) != len(a_set):
		return []
	subset = []
	for vi, element in zip(v, a_set):
		if vi == 1:
		subset += element
	return subset


def enumerate_all_subsets(a_set=['a', 'b', 'c']):
	'''部分集合を列挙する関数．
	深さ優先探索を元に部分集合の特性列（characteristic sequence）を列挙する．
	列挙された部分集合をまとめて最後に返す．
	'''
	
	subsets = [] # 部分集合を保存するためのリスト
	S = [[]] # スタック
	while len(S) > 0: # スタックが空でない限り以下を繰り返す．
		v = S.pop() # スタックから0-1列を1つ取り出す．
		if len(v) == len(a_set): # 0-1列が集合の要素数と同じ長さならば，
			subsets += [subset_from_vector(v, a_set)] # その0-1ベクトルが特性列であると見なして，部分集合を作り，保存する．
		else: # 0-1列が集合の要素数よりも短いならば，
			S += [v + [0]] # それに0を追加した列をスタックに入れる．
			S += [v + [1]] # それに1を追加した列もスタックに入れる．
	return subsets # 最後にまとめて，全ての部分集合を返す．




def enumerate_all_permutations(sequence=['a', 'b', 'c']):
	'''順列を列挙する関数．
	深さ優先探索探索を元に順列を列挙する．
	'''
	
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
