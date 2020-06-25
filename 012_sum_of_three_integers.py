"""
2つの整数k,sがあります。
3つの変数x,y,zがあり、0 <= z,y,z <= k を満たす整数値をとります。
x + y + z = s を満たすx,y,zへの値の割り当ては何通りありますか。

制約
・2 <= k <= 2500
・0 <= s <= 3k
・k,sは整数である

入力
k s

出力
問題の条件を満たすx,y,zの組が何通りあるか出力する
"""

k, s = map(int,input().split())
# print(k)
# print(s)

# 組み合わせをカウントする変数
count = 0

# 変数の初期化
x = 0
y = 0
z = 0

for x in range(k+1):
    for y in range(k+1):
        for z in range(k+1):
            if x + y + z == s:
                count += 1

print(count)


