"""
AtCoDeer君は、赤、緑、青色のカードを持っています。
それぞれのカードには 1 以上 9 以下の整数が書かれており、赤色のカードには r、緑色のカードには g、青色のカードには b が書かれています。
3 つのカードを左から順に赤、緑、青色の順に並べ、左から整数を読んだときにこれが 4 の倍数であるか判定しなさい。

制約
・1≤r,g,b≤9

入力
r g b

出力
AtCoDeer君が作った 3 桁の整数が 4 の倍数ならば YES、そうでないならば NO を出力しなさい
"""

r, g, b = map(int, input().split())

#r_string = str(r)
#g_string = str(g)
#b_string = str(b)

#rgb_string = r_string + g_string + b_string
#rgb = int(rgb_string)

rgb = (100 * r) + (10 * g) + b

if (rgb % 4 == 0):
    print('YES')
else:
    print('NO')



