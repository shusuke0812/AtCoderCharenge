"""
現在のレートが1200未満であればABCコンテストに参加し、そうでなければARCコンテストに参加する。
現在のレートxが与えられた時、参加するコンテストが何か出力する
"""

x = int(input())
rate = 1200

if x < rate:
    print('ABC')
else:
    print('ARC')
