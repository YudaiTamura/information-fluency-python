# 星の分け方を吟味して(部分集合列挙)→キューブの１辺の長さは勝手に決まる
# 計算に3分ぐらいかかる

def subset_from_vector(v, stars):
    if len(v) != len(stars):
        return []
    subset = []
    for vi, element in zip(v, stars):
        if vi == 1:
            subset += [element]
    return subset


def enumerate_all_subsets(stars):
    subsets = [] # 部分集合を保存するためのリスト
    S = [[]] # スタック
    while len(S) > 0: # スタックが空でない限り以下を繰り返す．
        v = S.pop() # スタックから0-1列を1つ取り出す．
        if len(v) == len(stars): # 0-1列が集合の要素数と同じ長さならば，
            subsets += [subset_from_vector(v, stars)] # その0-1ベクトルが特性列であると見なして，部分集合を作り，保存する．
        else: # 0-1列が集合の要素数よりも短いならば，
            S += [v + [0]] # それに0を追加した列をスタックに入れる．
            S += [v + [1]] # それに1を追加した列もスタックに入れる．
    return subsets # 最後にまとめて，全ての部分集合を返す．





def solve(stars):
    subset = enumerate_all_subsets(stars) # starsの部分集合列挙
    min = int(1e8*4) # 最小となる箱の大きさ
    for k in range(len(subset)):
        
        remain = list(set(stars) - set(subset[k])) # 部分集合列挙の際に選ばれなかった星をremainとする
        if len(subset[k]) != 0 and len(subset[k]) != 1: # subsetに対する星と星の距離＋星の半径の最大値を計算し、箱の大きさを出す
            max = 0 # 箱の大きさ
            for i in range(0, len(subset[k])-1):
                for j in range(i+1, len(subset[k])):
                    sx = abs(subset[k][i][0] - subset[k][j][0]) + subset[k][i][3] + subset[k][j][3]
                    sy = abs(subset[k][i][1] - subset[k][j][1]) + subset[k][i][3] + subset[k][j][3]
                    sz = abs(subset[k][i][2] - subset[k][j][2]) + subset[k][i][3] + subset[k][j][3]
                    if sx > max:
                        max = sx
                    if sy > max:
                        max = sy
                    if sz > max:
                        max = sz
        elif len(subset[k]) == 1:
            max = 0
            for i in range(0, len(subset[k])):
                if 2*subset[k][i][3] > max:
                    max = 2*subset[k][i][3]
        if len(remain) != 0 and len(remain) != 1: # remainに対する星と星の距離＋星の半径の最大値を計算し、箱の大きさを出す
            for i in range(0, len(remain)-1):
                for j in range(i+1, len(remain)):
                    rx = abs(remain[i][0] - remain[j][0]) + remain[i][3] + remain[j][3]
                    ry = abs(remain[i][1] - remain[j][1]) + remain[i][3] + remain[j][3]
                    rz = abs(remain[i][2] - remain[j][2]) + remain[i][3] + remain[j][3]
                    if rx > max:
                        max = rx
                    if ry > max:
                        max = ry
                    if rz > max:
                        max = rz
        elif len(remain) == 1:
            for i in range(0, len(remain)):
                if 2*remain[i][3] > max:
                    max = 2*remain[i][3]
        if min > max:
            min = max
    return min



def answer(input_file_name,output_file_name):
    input_file = open(input_file_name)
    output_file = open(output_file_name, 'w')
    T = int(input_file.readline())
    for case_number in range(1, T + 1):
        stars =[]
        N = int(input_file.readline())
        for n in range(N):
            x, y, z, r = map(int, input_file.readline().split())
            stars += [(x, y, z, r)]
        output_file.write('Case #{0}: {1}\n'.format(case_number,solve(stars)))
        print(case_number)
    input_file.close()
    output_file.close()
    return
    
