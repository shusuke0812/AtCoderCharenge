"""
英小文字からなる文字列sがある。
tが空文字列である状態から始め、以下の操作を好きな回数繰り返すことで
s=tとすることができるか判定する
 
 　tの末尾に'dream' 'dreamer' 'erase' 'eraser'のいずれかを追加

制約
・1 <= |s| <= 10^5
・sは英小文字からなる

入力
s

出力
s=tとすることができる場合、'YES'
そうでない場合 'NO'
"""

# TODO : RE, WAとなるのでどこがおかしいかデバッグする

s = list(input())
# s = list('erasedream')
s.reverse()

s_len = len(s)

flag = 'NO'

t = []
t_add = ['dream', 'dreamer', 'erase', 'eraser']
t_rev_add = ['maerd', 'remaerd', 'esare', 'resare']

# 方針：入力値の最後尾文字からスライスして文字列マッチングを行う

de = 4 # dream or erase の文字数
dr = 6 # dreamer の文字数
er = 5 # eraser の文字数

while True:
    if s[0] == 'm':
        if s[4] == 'd' or s[4] == 'e':
            flag = 'YES'
            del s[0:de+1]
        else:
            flag = 'NO'
            break

    elif s[0] == 'e':
        if s[4] == 'e':
            flag = 'YES'
            del s[0:de+1]
        else:
            flag = 'NO'
            break

    elif s[0] == 'r':
        if s[6] == 'd':
            flag = 'YES'
            del s[0:dr+1]
        elif s[5] == 'e':
            flag = 'YES'
            del s[0:er+1]
        else:
            flag = 'NO'
            break

    # print('s: ', s)
    # print('flag: ', flag)

    if len(s) <= 0:
        break

print(flag)

        

