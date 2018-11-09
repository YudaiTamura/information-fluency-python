#######点の生成########
def generate_points(n, a, b, c, d, x_0, y_0, m):
	x = x_0
	y = y_0
	point = [(x, y)]
	for i in range(1, n):
		x = ((a * x) + b) % m
		y = ((c * y) + d) % m
		point += [(x, y)]
	return point


#############自分の解答##################
def my_solve(point):
	Num = 0
	for i in range(0,len(point)-2):
		for j in range(i+1,len(point)-1):
			for k in range(j+1,len(point)):
				Gx = point[i][0]+point[j][0]+point[k][0] #x軸の値の合計
				Gy = point[i][1]+point[j][1]+point[k][1] #y軸の値の合計
				if Gx % 3 == 0: # xの重心が格子点上か判定
					if Gy % 3 == 0: # yの重心が格子点上か判定
						Num += 1 # 重心が格子点上にあるものの個数
	return Num


def may_answer(input_file_name, output_file_name):
	input_file = open(input_file_name)
	input_data = input_file.readlines()
	input_file.close()
	
	output_file = open(output_file_name, 'w')
	
	N = int(input_data.pop(0))#Nはデータの数
	
	for case_number in range(N):
		n, a, b, c, d, x_0, y_0, m = map(int, input_data.pop(0).split())
		output_file.write('Case #{0}: {1}\n'.format(case_number+1, solve(generate_points(n, a, b, c, d, x_0, y_0, m))))
	
	output_file.close()
	
	return




############単純な模範解答###############
def is_center_integer(p1, p2, p3):
	(x_1, y_1) = p1
	(x_2, y_2) = p2
	(x_3, y_3) = p3
	if (x_1 + x_2 + x_3) % 3 == 0 and (y_1 + y_2 + y_3) % 3 == 0:
		return True
	else:
		return False


def solve_simply(n, a, b, c, d, x_0, y_0, m):
	point = generate_points(n, a, b, c, d, x_0, y_0, m) # まず先述の関数generage_pointsを使って，点集合を生成する．
	
	count = 0
	for i in range(n - 2):
		for j in range(i + 1, n - 1):
			for k in range(j + 1, n):
				if is_center_integer(point[i], point[j], point[k]) == True:
					count += 1
	return count



def answer_simply(input_file_name, output_file_name):
	input_file = open(input_file_name)
	output_file = open(output_file_name, 'w')
	
	N = int(input_file.readline())
	for case_number in range(1, N + 1):
		n, a, b, c, d, x_0, y_0, m = map(int, input_file.readline().split())
		output_file.write('Case #{0}: {1}\n'.format(case_number, solve_simply(n, a, b, c, d, x_0, y_0, m)))
	input_file.close()
	output_file.close()



###########計算時間の計測################
import time 

def solve_simply(n, a, b, c, d, x_0, y_0, m):
	start_time = time.time() # 計算開始時刻をstart_timeに代入する．
	point = generate_points(n, a, b, c, d, x_0, y_0, m)
	
	count = 0
	for i in range(n - 2):
		for j in range(i + 1, n - 1):
			for k in range(j + 1, n):
				if is_center_integer(point[i], point[j], point[k]) == True:
					count += 1
	finish_time = time.time() # 計算終了時刻をfinish_timeに代入する．
	return count, finish_time - start_time # 解答だけでなく，計算時間も返すようにする．





##############工夫した模範解答##############
def solve(n, a, b, c, d, x_0, y_0, m):
	start_time = time.time() # 計算開始時刻をstart_timeに代入する．
	point = generate_points(n, a, b, c, d, x_0, y_0, m)
	
	'''
	ここまでは，先程の関数solve_simplyと同様である．
	ここからが，工夫されている．
	'''
	
	surplus = {
		(0, 0): 0, # キーを(i,j)としてG(i,j)に属する点の数を覚える．点数の初期値は0にしておく．
		(0, 1): 0,
		(0, 2): 0,
		(1, 0): 0,
		(1, 1): 0,
		(1, 2): 0,
		(2, 0): 0,
		(2, 1): 0,
		(2, 2): 0, # 最後のカンマはいらない．しかし後に要素が増えたときのミスを避けるため，最後にもカンマを付けることを習慣としたい．
	}
	
	for p in point: # すべての点に関して以下を繰り返す．
		x, y = p # まず，点の座標値をx, yとする．
		surplus[(x % 3, y % 3)] += 1 # 該当する集合G(i,j)の個数を1増やす．
	
	'''
	ここまでで，G(i,j)に属する点の個数がG[(i, j)]に入っている．
	ここからは，余りの値(i, j)ごとに，重心が整数格子点になる組合せを吟味する．
	全部ベタに書いても良いが，計算間違いが怖いので，組合せの計算は繰り返し文で行う．
	'''
	
	count = 0 # まず，答えの個数を格納する変数の値を0にしておく．
	
	for i in range(3):
		for j in range(3):
			for ii in range(3):
				for jj in range(3):
					if i == ii and j == jj: # (i, j)と(ii, jj)が同じグループならば
						continue # 問題の三角形の定義に反するので飛ばす．
					for iii in range(3):
						for jjj in range(3):
							if iii == i and jjj == j: # (iii, jjj)と(i, j)が同じグループならば
								continue # 問題の三角形の定義に反するので飛ばす．
							if iii == ii and jjj == jj: # (iii, jjj)と(ii, jj)が同じグループならば
								continue # 問題の三角形の定義に反するので飛ばす．
							if (i + ii + iii) % 3 == 0 and (j + jj + jjj) % 3 == 0:
								count += surplus[(i, j)] * surplus[(ii, jj)] * surplus[(iii, jjj)]
	count /= 6 # ここまでの数え方だと三角形の頂点の順番まで考慮していることになるので，順番を無視するため，3! = 6で割る．
	
	'''
	次に，余りが同じ点を3頂点とする三角形の重心は整数格子点になるので，その中で3頂点を選ぶ組合せの数を計算する．
	'''
	for i in range(3):
		for j in range(3):
			if surplus[(i, j)] >= 3:
				count += surplus[(i, j)] * (surplus[(i, j)] - 1) * (surplus[(i, j)] - 2) // 6 # 3つ選ぶ組合せの数をベタに計算している．
	
	finish_time = time.time() # 計算終了時刻をfinish_timeに代入する．
	print('n =', n, ', CPU time:', finish_time - start_time) # 計算時間は画面に表示する．
	return int(count)



def answer(input_file_name, output_file_name):
	input_file = open(input_file_name)
	output_file = open(output_file_name, 'w')
	
	N = int(input_file.readline())
	for case_number in range(1, N + 1):
		n, a, b, c, d, x_0, y_0, m = map(int, input_file.readline().split())
		output_file.write('Case #{0}: {1}\n'.format(case_number, solve(n, a, b, c, d, x_0, y_0, m))) # この行だけsolve_simplyからsolveに書き換えた．
	input_file.close()
	output_file.close()
