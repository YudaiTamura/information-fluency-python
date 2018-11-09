# Smallの場合、暗号の文字数は2から4の間なので場合分けすれば解ける。
# 文字数が2の時は文字を入れ替えるだけである。
# 文字数が3の時はAMBIGUOUSになる。
# 文字数が4の時だけちゃんと解けばいい。

def solveSmall(listedWord):
    NumToWord_dict = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',
                      14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}
    WordToNum_dict = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,
                      'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
    if len(listedWord) == 2: # 2文字の時
        originalWord = ''.join(reversed(listedWord))
    elif len(listedWord) == 3: # 3文字の時
        originalWord = 'AMBIGUOUS'
    else: # 4文字の時
        number_of_encrypted_word = [] # 暗号化された単語を数字に変換したものを入れるリスト
        number_of_original_word = [0 for i in range(4)] # 元の単語が数字に変換されたものを入れるリスト
        listedOriginalWord = [] # リスト化された元の単語
        
        for i in range(4):#はじめに、暗号化された単語を数字に変換
            number_of_encrypted_word.append(WordToNum_dict[listedWord[i]])
        
        number_of_original_word[1] = number_of_encrypted_word[0]
        number_of_original_word[2] = number_of_encrypted_word[3]
        # 1番目と2番目の数字はそれぞれ暗号化された単語の数字の0番目と3番目を見ればよい
                                            
        number_of_original_word[0] = (number_of_encrypted_word[1] - number_of_original_word[2]) % 26
        number_of_original_word[3] = (number_of_encrypted_word[2] - number_of_original_word[1]) % 26
        # 1番目と2番目の数字が決まるとそれらを用いて0番目と3番目の数字が求まる
        
        for i in range(4): # 数字から文字に変換
            listedOriginalWord.append(NumToWord_dict[number_of_original_word[i]])
        
        originalWord = ''.join(listedOriginalWord) # 一文字ずつリスト化されているので連結

    return originalWord




# largeの場合
def solve(listedWord):
    NumToWord_dict = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',
                      14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}
    WordToNum_dict = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,
                      'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
    
    if len(listedWord) == 2: # 2文字の時
        originalWord = ''.join(reversed(listedWord))
    
    elif len(listedWord) % 2 == 1: # 文字数が奇数の時
        originalWord = 'AMBIGUOUS'
    
    else: # 文字数が2以外の偶数の時
        number_of_encrypted_word = [] # 暗号化された単語を数字に変換したものを入れるリスト
        number_of_original_word = [0 for i in range(len(listedWord))] # 元の単語が数字に変換されたものを入れるリスト
        listedOriginalWord = [] # リスト化された元の単語
        
        for i in range(len(listedWord)):#はじめに、暗号化された単語を数字に変換
            number_of_encrypted_word.append(WordToNum_dict[listedWord[i]])
        
        
        number_of_original_word[1] = number_of_encrypted_word[0]
        number_of_original_word[-2] = number_of_encrypted_word[-1]
        # 1番目と-2番目の数字はそれぞれ暗号化された単語の数字の0番目と-1番目を見ればよい
        
        for i in range(3, len(listedWord), 2):
            number_of_original_word[i] = (number_of_encrypted_word[i-1] - number_of_original_word[i-2]) % 26
            # 3番目の数字から1つおきに右向きに求めてゆく
        
        for i in range(len(listedWord)-4, -1, -2):
            number_of_original_word[i] = (number_of_encrypted_word[i+1] - number_of_original_word[i+2]) % 26
            # -4番目の数字から1つおきに左向きに求めてゆく
        
        
        for i in range(len(listedWord)): # 数字から文字に変換
            listedOriginalWord.append(NumToWord_dict[number_of_original_word[i]])
        
        originalWord = ''.join(listedOriginalWord) # 一文字ずつリスト化されているので連結

    return originalWord



def answer(input_file_name, output_file_name):
    input_file = open(input_file_name)
    output_file = open(output_file_name, 'w')
    T = int(input_file.readline())
    for case_number in range(1, T + 1):
        W = input_file.readline().rstrip()
        listedWord = list(W)
        #output_file.write('Case #{0}: {1}\n'.format(case_number, solveSmall(listedWord)))
        output_file.write('Case #{0}: {1}\n'.format(case_number, solve(listedWord)))
    input_file.close()
    output_file.close()
    return
