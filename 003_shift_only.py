"""
N個の正の整数A1,A2,...Anが書かれています
全ての整数が偶数である時、整数すべてを2で割ったものに置き換えることができます。
書かれている整数に対して上記の操作が何回できるか求める

制約
・1 <= N <= 200
・1 <= Ai <= 10^9

入力
N
A1 A2 ... An

出力
操作回数
"""

n = int(input())
a = list(map(int, input().split()))
k = 0
count = 0
stop_flag = True
# print(n)
# print(a)

# 初めの入力値に奇数が含まれる場合
for i in a:
    if i % 2 != 0:
        stop_flag = False

while stop_flag:
    for i in a:
        a[k] = i / 2
        if a[k] % 2 != 0:
            stop_flag = False
        k += 1
    k = 0
    count += 1


print(count) 
