import math

# 自分で作った関数 smallしか解けません
def answer(input_file_name, output_file_name):
	input_file = open(input_file_name)
	output_file = open(output_file_name, 'w')
	
	NumDatasets = int(input_file.readline()) #データセットの数
	
	for case_number in range(1, NumDatasets + 1):
		month = int(input_file.readline()) #オープンしてる月数
		income = input_file.readline().split() #net income (month+1個)
		#print(income)
		if month == 2:
			a = -int(income[0])
			b = -2*int(income[0])+int(income[1])
			c = -int(income[0])+int(income[1])+int(income[2])
			if -1 < (-b+math.sqrt(b**2-4*a*c))/2*a and (-b+math.sqrt(b**2-4*a*c))/2*a < 1:
				IRR = (-b+math.sqrt(b**2-4*a*c))/2*a
			else:
				IRR = (-b-math.sqrt(b**2-4*a*c))/2*a
		elif month == 1:
			IRR = (int(income[1])/int(income[0]))-1
		output_file.write('Case #{0}: {1}\n'.format(case_number, IRR))
		
	input_file.close()
	output_file.close()






##############模範解答################
#今回の教訓	「直接解くのは難しいが，値を入れれば正しいか否かは簡単に判断できる
#				方程式のようなものを解く際には2分探索が有効である」

def total_cash(M, C, r): # 上記の関数f(r)に相当する．
	cash = 0
	rate = 1
	for i in range(M, 0, -1):
		cash += C[i] * rate
		rate *= 1 + r
	cash -= C[0] * rate
	return cash


def solve(M, C):
	upper_bound = 1.0
	lower_bound = - 1.0
	while upper_bound - lower_bound > 10 ** -10: # 上界と下界の差が10^-10以下になるまで繰り返す．
		middle = (lower_bound + upper_bound) / 2
		if total_cash(M, C, upper_bound) * total_cash(M, C, middle) > 0:
			upper_bound = middle
		else:
			lower_bound = middle
	return upper_bound


def answer(input_file_name, output_file_name):
	input_file = open(input_file_name)
	output_file = open(output_file_name, 'w')
	T = int(input_file.readline())
	for case_number in range(1, T + 1):
		M = int(input_file.readline())
		C = list(map(int, input_file.readline().split()))
		# mapの出力のままだとリストと同様に扱えない場合があるので，組込み関数listでリストにする．
		output_file.write('Case #{0}: {1:10.9}\n'.format(case_number, solve(M, C)))
		# 有効数字を指定したフォーマット出力の書き方は上記の通り{x:y.z}で
		# 「メソッドformatのx番目の引数を，有効数字y桁で，そのうち小数部分はz桁」という意味になる．
	input_file.close()
	output_file.close()
	return
