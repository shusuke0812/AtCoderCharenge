"""
縦N行、横N列に画素が並んだ画像Aと、縦M行、横M列に画素が並んだテンプレート画像Bが与えられる。
画素は画像を構成する最小単位であり、ここでは1*1の正方形とする。
また、与えられる画像は全て2値画像であり、各画素の色は白と黒の2種類で表されます。
入力において全ての画素は文字で表されており、'.'は白色の画素、'#'は黒色の画素に対応します。
画像AはN個の文字列A1...Anで表されます。
文字列Aiのj文字列目は画像Aの上からi番目、左からj番目の画素に対応します。（1<=i,j<=N）
同様にテンプレート画像BはM個の文字列B1...Bmで表されます。
文字列Biのj文字目はテンプレート画像Bの上からi番目、左からj番目の画素に対応します。（1<=i,j<=M）
画像の平行移動のみ許されるとき、テンプレート画像Bが画像Aに含まれているか判定する。

制約
・1 <= M <> N <= 50
・Aiは'#'と'.'からなる長さNの文字列
・Biは'#'と'.'からなる長さMの文字列

入力
N M
A1
A2
.
.
An
B1
B2
.
.
Bm

出力
画像Aの中にテンプレート画像Bを含む場合は'Yes'、含まない場合は'No'を出力せよ
"""

