def solve(tickets, N):
    answer = [tickets[0]]
    # anwerのdestがどこの空港のsrcと一致するか見る
    for i in range(N):
        for j in range(N):
            if(answer[-1][1] == tickets[j][0]):
                answer = answer + [tickets[j]]
    # answerのsrcがどこの空港のdestと一致するか見る
    for i in range(N):
        for j in range(N):
            if(tickets[j][1] == answer[0][0]):
                answer = [tickets[j]] + answer
    # answerを出力用に整形する
    ansForOutput = ''
    for t in range(N):
        ansForOutput += '-'.join(answer[t])
        ansForOutput += ' '
    return ansForOutput

def answer(input_file_name,output_file_name):
    input_file = open(input_file_name)
    output_file = open(output_file_name, 'w')
    T = int(input_file.readline()) # テストケース数T
    for case_number in range(1, T + 1):
        N = int(input_file.readline()) # チケットの枚数N
        tickets = [] # チケットの配列tickets
        # チケットのn番目にn番のチケットの出発空港と目的空港の両方を格納するためにリストを二重構造にする
        for i in range(N):
            elementsOfTickets = []
            elementsOfTickets += [input_file.readline().strip()] # 出発空想
            elementsOfTickets += [input_file.readline().strip()] # 到着空港
            tickets += [elementsOfTickets]
        output_file.write('Case #{0}: {1}\n'.format(case_number,solve(tickets, N)))
    input_file.close()
    output_file.close()
    return