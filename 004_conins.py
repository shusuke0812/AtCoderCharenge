"""
500円玉をa枚、100円玉をb枚、50円玉をc枚持っています。
これらの硬貨の中から何枚かを選び、合計金額をちょうどx円にする方法は何通りありますか。
同じ種類の硬貨同士は区別できず、２通りの硬貨の選び方はある種類の硬貨についてその硬貨を選ぶ枚数が異なるとき区別されます。

制約
・0 <= a,b,c <= 50
・a+b+c >= 1
・50 <= x <= 20,000
・a,b,cは整数である
・xは50の倍数である

入力
a
b
c
x

出力
硬貨を選ぶ方法の個数
"""

a = int(input())
b = int(input())
c = int(input())
x = int(input())

count = 0

for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if x == 500 * i + 100 * j + 50 * k:
                count += 1

print(count)
