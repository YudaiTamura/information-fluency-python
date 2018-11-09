def solve(gBuses, NumBus, input_file):
    NumCity = int(input_file.readline()) # 街Pの数NumCity
    counter = [0 for s in range(NumCity)] # gBusが何回、街Pを通ったかカウントするリストcounter
    for j in range(NumCity):
        P = int(input_file.readline()) # 街P
        for k in range(NumBus):
            if(gBuses[k][0] <= P and P <= gBuses[k][1]): # gBusの出発地gBuses[k][0]、gBusの目的地gBuses[k][1]
                counter[j] += 1 # 条件を満たしていれば1増やす
    # counterの要素は数値なので文字列に変換
    str_counter = list(map(str, counter))
    answer = ' '.join(str_counter)
    return answer


def answer(input_file_name,output_file_name):
    input_file = open(input_file_name)
    output_file = open(output_file_name, 'w')
    T = int(input_file.readline()) # テストケース数T
    for case_number in range(1, T + 1):
        NumBus = int(input_file.readline()) # gBusの数NumBus
        # gBusをリストとして取り出す。
        pre_gBus0 = input_file.readline().split() # とりあえず文字列のまま取り出す
        pre_gBus = list(map(int, pre_gBus0)) # 文字列を数値に変換
        gBuses = [] # ここから本命のgBusのリストgBusesとしてpre_gBusを整形する
        # リストのn番目にn番のgBusの出発地と目的地の両方を格納するためにリストを二重構造にする
        for i in range(NumBus):
            elementOfgBuses = []
            elementOfgBuses += [pre_gBus[i*2]]
            elementOfgBuses += [pre_gBus[i*2+1]]
            gBuses += [elementOfgBuses]
        print(case_number)
        output_file.write('Case #{0}: {1}\n'.format(case_number,solve(gBuses,NumBus, input_file)))
        input_file.readline()
    input_file.close()
    output_file.close()
    return
