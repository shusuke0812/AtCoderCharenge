"""
n枚のカードがあり、i枚目にはaiという数が書かれている。
AliceとBobは互いにカードを1枚ずつ取って、取ったカードの合計数が得点になります。
自身の得点が最大化するように最適な戦略をとった時、AliceはBobより何点多く取るか求める。

制約
・nは1 <= n <=100の整数
・aiは1 <= ai <= 100の整数

入力
N
a1 a2 a3 ... an

出力
両者が最適な戦略を取った時、AliceはBobより何点多く取るかを出力してください。
"""

n = input()
a = list(map(int, input().split()))
alice_score = 0
bob_score = 0

count = 1

a = sorted(a, reverse=True)

for i in a:
    if count % 2 != 0:
        alice_score += i
    else:
        bob_score += i
    
    count += 1

print(alice_score - bob_score)

