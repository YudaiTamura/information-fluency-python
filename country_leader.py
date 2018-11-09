import collections

#smallを解くための関数
def small(input_file_name, output_file_name):
	input_file = open(input_file_name)
	output_file = open(output_file_name, 'w')
	
	NumDatasets = int(input_file.readline()) #データセットの数
	
	for case_number in range(1, NumDatasets + 1):
		NumNames = int(input_file.readline()) #データセット内の名前の数
		max = 0
		name_list = [] #名前のリストを作成
		for n in range(NumNames): #ここでデータセット内の名前をリストに追加していく
			name = input_file.readline()
			name_list.append(name)
		name_list.sort() #アルファベット順にする
		for i in range(NumNames):
			number_of_letters = len(collections.Counter(name_list[i])) #文字の種類の数
			if number_of_letters > max:
				max = number_of_letters
				leader = name_list[i]
		output_file.write('Case #{0}: {1}\n'.format(case_number, leader))
		
	input_file.close()
	output_file.close()
	return

#smallは解けます


#largeを解くための関数
def large(input_file_name, output_file_name):
	input_file = open(input_file_name)
	output_file = open(output_file_name, 'w')
	
	NumDatasets = int(input_file.readline()) #データセットの数
	#print(NumDatasets)
	for case_number in range(1, NumDatasets + 1):
		NumNames = int(input_file.readline()) #データセット内の名前の数
		#print(NumNames)
		max = 0
		name_dict = {} #名前の辞書を作成
		for n in range(NumNames):
			name_dict[n] = input_file.readline() #名前の辞書に名前を入れてゆく
		sorted_name_dict = name_dict #名前の辞書を複製
		for m in range(NumNames):
			sorted_name_dict[m] =''.join(sorted_name_dict[m].split()) #複製した辞書の値(名前)から空白を抜く
		#print(sorted_name_dict)
		sorted(sorted_name_dict.items(), key=lambda x: x[1]) #値をアルファベット順にする#ここができない
		#print(sorted_name_dict)
		for i in range(NumNames):
			number_of_letters = len(collections.Counter(sorted_name_dict[i])) #文字の種類の数
			if number_of_letters > max:
				max = number_of_letters
				leader = sorted_name_dict[i]
		for k, v in sorted_name_dict.items():
			if v == leader:
				keyOfLeader = k
		output_file.write('Case #{0}: {1}\n'.format(case_number, name_dict[k]))
		
	input_file.close()
	output_file.close()
	return






#################模範解答#############################

def different_letters(name):
	'''
	used_alphabets = {} # 文字の種類数を数えるための辞書を用意する．
	for char in name: # 名前のそれぞれの文字に関して以下を繰り返す．
		if char == ' ': # （問題の仮定より）空白文字ならば，
			continue # 何も処理しない．
		else: # そうでない（空白文字でない）ならば，
			used_alphabets[char] = 1 # その文字が使われているしるしとして辞書の値を1にする．
	return len(used_alphabets.keys()) # 辞書のキーの個数が，名前で使われている文字の種類数のはずである．
	'''
	return len(set(name) - set([' '])) #セットの利用


def solve(names):
	max_letters = 0 # 最大文字種類数の最大値を覚えるための変数を用意する．
	leader = '' # リーダーの名前を覚えるための変数を用意する．
	for name in names: # すべての名前に関して以下を繰り返す．
		diff_letters = different_letters(name) # まず，その名前で使われている文字の種類数を数える．
		if max_letters < diff_letters: # その名前の文字の種類数が，それまでの最大値よりも大きいならば，
			max_letters = diff_letters # その種類数を最大値として覚え直し，
			leader = name # その名前をリーダーとする．
		elif max_letters == diff_letters: # そうでなくて，その名前の種類数がそれまでの最大値と同じで，
			if name < leader: # かつ，現時点でのリーダーの名前よりも辞書順で先ならば，
				leader = name # その名前をリーダーとする．
	return leader


def answer(input_file_name, output_file_name):
	input_file = open(input_file_name)
	output_file = open(output_file_name, 'w')
	T = int(input_file.readline())
	for case_number in range(1, T + 1):
		N = int(input_file.readline())
		names = []
		for n in range(N):
			names += [input_file.readline().rstrip()]
		output_file.write('Case #{0}: {1}\n'.format(case_number, solve(names)))
	input_file.close()
	output_file.close()
	return # このreturnは必要ないが，お行儀よく一応付けておく．
