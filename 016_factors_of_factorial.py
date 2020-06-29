"""
整数nがある。
n!の正の約数の個数を10^9 + 7で割った余りを求める。

制約
・1 <= n <= 10^3

入力
n

出力
n!の正の約数の個数を10^9+7で割った余り
"""

n = int(input())
ans = 1
divisor = []

for i in range(1,n+1):
    ans = ans * i


