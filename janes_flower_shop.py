import math

# �����ō�����֐� small���������܂���
def answer(input_file_name, output_file_name):
	input_file = open(input_file_name)
	output_file = open(output_file_name, 'w')
	
	NumDatasets = int(input_file.readline()) #�f�[�^�Z�b�g�̐�
	
	for case_number in range(1, NumDatasets + 1):
		month = int(input_file.readline()) #�I�[�v�����Ă錎��
		income = input_file.readline().split() #net income (month+1��)
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






##############�͔͉�################
#����̋��P	�u���ډ����͓̂�����C�l������ΐ��������ۂ��͊ȒP�ɔ��f�ł���
#				�������̂悤�Ȃ��̂������ۂɂ�2���T�����L���ł���v

def total_cash(M, C, r): # ��L�̊֐�f(r)�ɑ�������D
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
	while upper_bound - lower_bound > 10 ** -10: # ��E�Ɖ��E�̍���10^-10�ȉ��ɂȂ�܂ŌJ��Ԃ��D
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
		# map�̏o�͂̂܂܂��ƃ��X�g�Ɠ��l�Ɉ����Ȃ��ꍇ������̂ŁC�g���݊֐�list�Ń��X�g�ɂ���D
		output_file.write('Case #{0}: {1:10.9}\n'.format(case_number, solve(M, C)))
		# �L���������w�肵���t�H�[�}�b�g�o�͂̏������͏�L�̒ʂ�{x:y.z}��
		# �u���\�b�hformat��x�Ԗڂ̈������C�L������y���ŁC���̂�������������z���v�Ƃ����Ӗ��ɂȂ�D
	input_file.close()
	output_file.close()
	return
