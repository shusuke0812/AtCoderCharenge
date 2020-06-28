"""
二つの長方形がある。
一つ目の長方形は、縦の辺の長さがA、横の辺の長さがBです。
二つ目の長方形は、縦の辺の長さがC、横の辺の長さがDです。
この二つの長方形のうち面積の大きい方の面積を出力する。
なお、二つの長方形の面積が等しい時はその面積を出力する。

制約
・入力は全て整数
・1 <= A,B,C,D <= 10^4

入力
A B C D

出力
大きい方の長方形の面積。等しい場合はその面積。
"""

a,b,c,d = map(int, input().split())

# print(a,b,c,d)

rectangle_x = a * b
rectangle_y = c * d

if rectangle_x > rectangle_y:
    print(rectangle_x)
elif rectangle_x < rectangle_y:
    print(rectangle_y)
else:
    print(rectangle_x)
