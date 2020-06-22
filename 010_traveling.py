"""
2次元平面上での移動を考える。
時刻0に点（0,0）を出発し、1以上n以下の各iに対し、
時刻tiに点（xi,yi）を訪れる予定。

時刻tに点（x,y）にいる時、時刻t+1には点（x+1,y）,（x-1,y）,
（x,y+1）,（x,y-1）のうちいずれかに存在することができ、その場に止まることは出来ない。
入力値のプランが成立するか確認する

制約
・1 <= n <= 10^5
・0 <= xi <= 10^5
・0 <= yi <= 10^5
・1 <= ti <= 10^5
・ti < ti+1 (1 <= i <= n-1）
・入力は全て整数

入力
n
t1 x1 y1
t2 x1 y2
・
・
tn xn yn

出力
入力のプランが実行可能なら'Yes', 不可能なら'No'
"""

n = int(input())
t = []  # 移動距離
xy = [] # 座標
for i in range(1,n+1):
    t_temp, x_temp, y_temp = list(map(int, input().split()))
    t.append(t_temp)
    xy.append([x_temp, y_temp])

# print(t)
# print(xy)

k = 0
flag = 'No'
guki = ''

for j in xy:
    """
    TODO:これだと(0, 0)から計算していることになる
         移動したら各座標から移動距離を出すように変更する
         dt, dxy
    """
    # 座標までの距離を計算
    distance = j[0] + j[1]
    # print(distance)

    # 移動距離と座標までの距離の偶奇判定
    if t[k] % 2 == 0 and distance % 2 == 0:
        guki = 'Even'
    elif t[k] % 2 != 0 and distance % 2 != 0:
        guki = 'Odd'
    else:
        guki = ''
    # print(guki)

    if t[k] < distance:
        flag = 'No'
        break
    elif t[k] == distance:
        flag = 'Yes'
    elif t[k] > distance:
        if guki == '':
            flag = 'No'
            break
        else:
            flag = 'Yes'
    
    # print(flag)
    k += 1
    guki = ''
    distance = 0

print(flag)

