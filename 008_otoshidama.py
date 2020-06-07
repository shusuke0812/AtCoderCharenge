"""
お札は10000円札、5000円札、1000円札のことを言います。
n枚のお札が入った袋があり、合計がy円だとする。
y円となるお札の組み合わせを求める。

制約
・1 <= n <= 2000
・1000 <= y <= 2*10^7
・nは整数
・yは1000の倍数

入力
n y

出力
y円となる各お札の組み合わせの一例の中からお札の枚数を出力する。
ただし、組み合わせがない場合は'-1 -1 -1'と出力する。
"""

n = int(input())
y = int(input())

ichiman = 10000
gosen = 5000
sen = 1000

i = 0
j = 0
k = 0

# TODO:これだと合計n枚にならない
if y % ichiman != 0:
    k = y // ichiman
    y = y - ichiman * k
    if y % gosen != 0:
        j = y // gosen
        y = y - gosen * j
        if y % sen == 0:
            i = y // sen
        else:
            i = -1
            j = -1
            k = -1
    else:
        j = y // gosen
else:
    k = y // ichiman

if i + j + k <= n:
    print(i,j,k)
else:
    print('-1 -1 -1')
    
