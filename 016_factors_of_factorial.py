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

factorial = 1
divisor = []
ans = 0

for i in range(1,n+1):
    factorial = factorial * i

# print(factorial)

for i in range(1,factorial+1):
    if factorial % i == 0:
        divisor.append(i)

# print(divisor)

ans = len(divisor) % (10 ** 9 + 7)

print(ans)
