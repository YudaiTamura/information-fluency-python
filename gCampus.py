def dijkstra(V, # �L���O���t�̒��_�W��
             E, # �L���}�W��
             length, # �}����
             source, # �n�_
            ):
    #�O�����Ƃ��āC���_���^����ꂽ�炻�̒��_����o�Ă���}�̐�̒��_�̃��X�g�������鎫��successor�����D
    successor = {v: [] for v in V}
    for tail, head in E:
        successor[tail] += head

    #Step 1
    distance = {} # �ŒZ�H��distance�͎����ŏo�͂��邱�Ƃɂ���D
    upper_bound_of_shortest_path_length = sum(length.values())
    # �X���C�h�́��̑���ɁC�ŒZ�H���̎����ȏ�E�Ƃ��āu�}�����̍��v�v���g�����Ƃɂ���D
    for v in V:
        distance[v] = upper_bound_of_shortest_path_length

    #Step 2
    distance[source] = 0 # �n�_���̂��̂ւ̍ŒZ�H����0�ł���D

    #Step 3
    U = V[:] # �W���i���X�g�jU�ɒ��_�W�����R�s�[����D

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
            costs[(u, v)] = c #costs�͂��̓��H��������R�X�g
            setV += v #���_�W��V�ɂ����
            setE += (u, v) #�L���}�W��E�ɂ����
        output_file.write('Case #{0}: {1}\n'.format(case_number,solve(costs, setV, setE)))
        #print(costs)
    input_file.close()
    output_file.close()
    return
