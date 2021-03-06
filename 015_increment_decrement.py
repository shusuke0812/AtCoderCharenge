"""
ある整数xを持っており、最初はx=0である。
長さnの文字列sを使って次の操作をn回行う。
i回目の操作ではsi='I'ならばxの値を1増やし、si='D'ならばxの値を1減らす。

操作の途中でxがとる値の最大値を出す。

制約
・1 <= n <= 100
・|s| = n
・sには'I', 'D'以外の文字は含まれない

入力
n
s

出力
操作の途中での整数xがとる値の最大値を出力する
"""

n = int(input())
s = input()

x = 0
x_max = 0
s_list = []

for i in s:
    s_list.append(i)

# print(s_list)

for i in s_list:
    if i == 'I':
        x += 1
        if x > x_max:
            x_max = x
    elif i == 'D':
        x -= 1


print(x_max)
