def dijkstra(V, # 有向グラフの頂点集合
             E, # 有向枝集合
             length, # 枝長さ
             source, # 始点
            ):
    #前準備として，頂点が与えられたらその頂点から出ている枝の先の頂点のリストを引ける辞書successorを作る．
    successor = {v: [] for v in V}
    for tail, head in E:
        successor[tail] += head

    #Step 1
    distance = {} # 最短路長distanceは辞書で出力することにする．
    upper_bound_of_shortest_path_length = sum(length.values())
    # スライドの∞の代わりに，最短路長の自明な上界として「枝長さの合計」を使うことにする．
    for v in V:
        distance[v] = upper_bound_of_shortest_path_length

    #Step 2
    distance[source] = 0 # 始点そのものへの最短路長は0である．

    #Step 3
    U = V[:] # 集合（リスト）Uに頂点集合をコピーする．

    #Step 4
    while len(U) > 0:
        #Step 4-1
        minimum_of_d = upper_bound_of_shortest_path_length
        v = U[0]
        for u in U:
            if distance[u] < minimum_of_d:
                v = u
                minimum_of_d = distance[v]
        #Step 4-2
        U.remove(v)
        #Step 4-3
        for w in successor[v]:
            if distance[w] > distance[v] + length[(v, w)]:
                distance[w] = distance[v] + length[(v, w)]

    #Step 5
    return distance




def solve(costs, setV, setU):
    extra = []
    dijkstra(setV, setU, costs, 0)
    return extra





def answer(input_file_name, output_file_name):
    input_file = open(input_file_name)
    output_file = open(output_file_name, 'w')
    T = int(input_file.readline())
    for case_number in range(1, T + 1):
        N, M = map(int, input_file.readline().split())
        costs = {}
        setV = {}
        setE = {}
        for m in range(M):
            u, v, c = map(int, input_file.readline().split())
            costs[(u, v)] = c #costsはその道路をかかるコスト
            setV += v #頂点集合Vにいれる
            setE += (u, v) #有向枝集合Eにいれる
        output_file.write('Case #{0}: {1}\n'.format(case_number,solve(costs, setV, setE)))
        #print(costs)
    input_file.close()
    output_file.close()
    return
