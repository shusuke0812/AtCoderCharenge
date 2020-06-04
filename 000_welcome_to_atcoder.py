"""
整数a,b,cと文字列sが与えられる。
a+b+cの計算結果と文字列sを並べて表示する。

制約
・1 <= a,b,c <= 1,000
・1<= |s| <= 100

入力
a
b c
s

出力
a+b+c s
"""

a = int(input())
b, c = (int(x) for x in input().split())
s = input()

print(a+b+c, s)
