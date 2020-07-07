"""
文字列sの一部を取り出して先頭が'A'であり末尾が'Z'であるような文字列を作る。
作ることのできる文字列の最大の長さを求める。
なお、sには先頭が'A'であり末尾が'Z'であるような部分文字列が必ず存在することが保証される。

制約
・1 <= |s| <= 200,000
・sは英大文字のみからなる
・sには先頭が'A'であり、末尾が'Z'であるような部分文字列が必ず存在する

入力
s

出力
答えを出力
"""

# 考え：文字列sを先頭から見ていき、最初にAが来る要素番号、最後にZが来る要素番号がわかれば良い
# 方針：Aは文字列を左から探索して最初に検出した要素番号、Zは文字列を右から探索して最初に検出した要素番号

s = input()
s_start = 0
s_end = 0
count = 0

# 文字列sを右から探索できるように逆順に変換する
s_reverse = s[::-1]
# print(s_reverse)

for i in s:
    if i == 'A':
        s_start = count
        break
    count += 1

# カウンタcountを逆順用に変更（降順）
count = len(s) - 1

for j in s_reverse:
    if j == 'Z':
        s_end = count
        break
    count -= 1

ans = s_end - s_start + 1
print(ans)

#EOF
