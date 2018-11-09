import math

def solve simply(r, t):
	m = (1 - 2 * r + math.sqrt((2 * r - 1) ** 2 + 8 * t)) / 4
	return int(m)


def is_possible(m, r, t):
	if 2 * (m ** 2) + (2 * r - 1) * m <= t: # 演算子**の優先順位は演算子*よりも高いので最初の（）は必要ない
		return True
	else:
		return False


def solve(lower_bound, upper_bound, r, t):
	'''2分探索でギリギリのm，すなわち解答を返す関数．
	引数のlower_boundにはmの下界，upper_boundにはmの上界を与える．
	'''
	
	while upper_bound - lower_bound > 1: # mの上界と下界が離れている間は，mの候補を絞るため以下を繰り返す．
		middle = (upper_bound + lower_bound) // 2 # 上界と下界の中間（の小数部分切り捨て）を計算し，
		if is_possible(middle, r, t) == True: # 中間が「塗れる」本数ならば，
			lower_bound = middle # ギリギリのmは中間と上界の間にあるはずなので，新たに中間の本数を下界とする．
		else: # そうでないならば，
			upper_bound = middle # ギリギリのmは下界と中間の間にあるはずなので，新たに中間の本数を上界とする．
	'''
	繰り返しが終わったならば，mの候補は上界か下界のいずれかになっているはずである．
	'''
	if is_possible(upper_bound, r, t) == True: # よって，上界が「塗れる」本数ならば，
		return upper_bound # それを解答として返し，
	else: # そうでないならば，
		return lower_bound # 下界を解答として返す．



def answer(input_file_name, output_file_name):
	input_file = open(input_file_name)
	output_file = open(output_file_name, 'w')
	
	T = int(input_file.readline())
	for case_number in range(1, T + 1):
		r, t = map(int, input_file.readline().split())
		output_file.write('Case #{0}: {1}\n'.format(case_number, solve(0, t, r, t)))
	input_file.close()
	output_file.close()
