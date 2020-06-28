"""
2次元座標を考える。
現在地点（sx, sy）にいて、1秒あたり上下左右に距離1だけ進むことができる。
このとき移動前と移動後のx座標, y座標はともに整数でなければならない。
ここから sx<tx< と sy<ty を満たす点（tx, ty）に行き、その後点（sx,sy）に戻り、
また点（tx,ty）に行き、その後点（sx,sy）に戻ります。
このとき、点（sx,sy）と点（tx,ty）を除いて途中で同じ座標を複数回通らないように移動しなければならない。
このような条件を満たす最短経路を求める

制約
・-1000 <= sx < tx <= 1000
・-1000 <= sy < ty <= 1000
・sx, sy, tx, tyは整数である

入力
sx sy tx ty

出力
最短経路を表す文字列Sを出力する
・'U'：上方向
・'D'：下方向
・'L'：左方向
・'R'：右方向
"""

coordinates = list(map(int,input().split()))
s = []
t = []

for i in range(len(coordinates)):
    if i < 2:
        s.append(coordinates[i])
    else:
        t.append(coordinates[i])

# print(s)
# print(t)

dx = t[0] - s[0]
dy = t[1] - s[1]

route = ""

# print("dx: ", dx)
# print("dy: ", dy)

# 経路パターン１
# 行き
for i in range(dx):
    route += "R"
for i in range(dy):
    route += "U"

# 帰り
for i in range(dx):
    route += "L"
for i in range(dy):
    route += "D"

# 経路パターン２（パターン１の外側を通る）
# 行き
route += "D"

for i in range(dx+1):
    route += "R"
for j in range(dy+1):
    route += "U"

route += "L"
route += "U"

for i in range(dx+1):
    route += "L"
for i in range(dy+1):
    route += "D"

route += "R"


# 解答出力
print(route)
