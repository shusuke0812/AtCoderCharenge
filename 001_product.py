"""
a,bの積が偶数か奇数か判定してください

制約
・1 <= a,b <= 10,000
・a, bは整数

入力
a b

出力
積が奇数なら'Odd', 偶数なら'Even'と出力
"""

a, b = (int(x) for x in input().split())

seki = a * b

if seki % 2 == 0:
    print('Even')
else:
    print('Odd')
