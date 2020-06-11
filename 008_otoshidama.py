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

y = list(map(int, input().split()))

n = y[0]
money_sum = y[1]

# 組み合わせがないときのflag
error_flag = 0

# x = 10000円の枚数, y = 5000円の枚数、z = 1000円の枚数
# x + y + z = n となる組み合わせを [x, y, z] を考える
money_num = []
for i in range(n+1):
    for j in range(n+1-i):
        money_num.append([n-j-i, j, i])

        sum = (n-j-i) * 10000 + j * 5000 + i * 1000

        if sum == money_sum:
            error_flag = 1
            x = n-j-i
            y = j
            z = i
            break
        else:
            # 不要なリスト内のデータはメモリの使用を抑えるため即削除
            money_num.pop(0)
    else:
        continue
    break


if error_flag == 1:
    print(x, y, z)
    # print(ans[0], ans[1], ans[2])
else:
    print('-1 -1 -1')


# ボツ案
# 入力値の金額を各紙幣で割った商と余りを使えば良いと思ったが....
# これだと各紙幣の枚数の合計が入力値の枚数にならないことがある
"""
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
""" 
