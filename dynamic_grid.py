####################グラフ探索で解く################

def solve(R, C, altitude): # グラフ探索
    
    return



def answer(input_file_name, output_file_name):
    input_file = open(input_file_name)
    output_file = open(output_file_name, 'w')
    T = int(input_file.readline())
    for case_number in range(1, T + 1):
        output_file.write('Case #{0}:\n'.format(case_number))
        R, C = map(int, input_file.readline().split())
        for n in range(R):
            altitude += [list(map(int, input_file.readline().split()))]
        N = int(input_file.readline())
        for case_number in range(N):
            opn = input_file.readline().split()   #オペレーション用のリストopn
            if opn[0] == 'Q': #オペがQのとき
                #グラフ探索を行う。 solve()やればいいだけ
                output_file.write(solve(R, C, altitude)) 
            else: #オペがMのとき
                # opn[1]行、opn[2]列の要素をopn[3]に変える
                altitude[int(opn[1])][int(opn[2])] = int(opn[3]) 
    input_file.close()
    output_file.close()
    return
