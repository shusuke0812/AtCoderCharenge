"""
６面サイコロがある。
サイコロは１から６までの整数がそれぞれの面に書かれており、向かい合う面に書かれた数の和はどれも７である。
サイコロを好きな面が上向けになるように置いたのち何回か以下の操作を行います。
・操作：サイコロを手前、奥、左、右のどれかの方向に９０°だけ回転させる。
　　　　その後、上を向いている面に書かれた数をyとしてy点得る。
合計でx点以上得るために必要な最小の操作回数を求める。

制約
・1 <= x <= 10^15
・xは整数

入力
x

出力
答え
"""

s = int(input())
count = 0

# 考え：初めに５の面を上にし、６、５、６、５の面を繰り返し上にしていくと良さそう
# 方針：while中、奇数回目にsから６を引く、偶数回目にsから５を引くことを繰り返す計算を行う

# TODO：この方法だとsが大きい場合、計算に時間がかかる
while s > 0:
    if count == 0 or count % 2 != 0:
        s = s - 6
    else:
        s = s - 5

    count += 1

print(count)
