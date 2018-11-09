def StoreCredit(C, P):
	i=0
	j=0
	for i in range(len(P)):
		for j in range(i+1,len(P)):
			if P[i] + P[j] == C:
				print(P[i], P[j])
	return


def ReverseWords(S):
	SL = S.split()
	SL.reverse()
	out=''
	for i in range(len(SL)):
		out = out + SL[i] + ' '
	return out[:-1]