"""
x段重ねの鏡餅（X>=1）とは、x枚の円形の鏡餅を縦に積み重ねたもの。
どの餅も真下の餅より直径が小さいとする。
n枚の円形の餅がある時、そのうちi枚目の餅の直径はd cmとする。
この餅の一部または全部を使って鏡餅を作る時、最大で何段重ねの鏡餅を作ることができるか。

制約
・1 <= n <= 100
・1 <= di <= 100
・入力値はすべて整数

入力
n
d1
d2
.
.
.
dn

出力
作ることのできる鏡餅の最大の段数
"""

n = int(input())
d = []

for i in range(n):
    # print(i)
    d.append(int(input()))

d = list(set(d))
d = sorted(d)
# print(d)

print(len(d))