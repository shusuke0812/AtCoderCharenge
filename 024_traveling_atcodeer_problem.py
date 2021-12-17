"""
クリスマスもあと半年となり、トナカイのAtCoDeer君はプレゼントを配る計画を立てることにしました。
TopCoDeer通りには N 個の家が並んでいます。i 個目の家は座標 ai にあります。彼はこのすべての家にプレゼントを配ることにしました。
好きな場所から開始し好きな場所で終了することができる時、最小の移動距離を求めなさい

制約
・1≤N≤100
・0≤ai≤1000
・ai は整数である。

入力
N
a1 a2 ... aN

出力
AtCoDeer君が動く距離の最小値を出力しなさい
"""

N = map(int, input())
a = list(map(int, input().split()))

a_uniques = list(set(a))
a_uniques.sort()

distance = 0

for i in range(len(a_uniques) - 1):
    distance = distance + a_uniques[i+1] - a_uniques[i]

print(distance)