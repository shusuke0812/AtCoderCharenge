"""
1以上n以下の整数のうち、10進法での各桁の和がA以上B以下であるものの総和を求めてください。

制約
・1 <= n <= 10^4
・1 <= A <= B <= 36
・入力は全て整数

入力
N A B

出力
1以上n以下の整数のうち、10進法での格桁の和がA以上B以下であるものの総和を出力
"""

n, a, b = (int(x) for x in input().split())
sum = 0
sums = []

for i in range(1, n+1):
    num = list(map(int, str(i)))
    # print(num)
    for j in num:
        sum += j

    # print(sum)
    if sum >= a and sum <= b:
        sums.append(i)

    sum = 0

# print(sums)

for k in sums:
    sum += k

print(sum)
