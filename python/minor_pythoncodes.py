#!/usr/bin/python
# -*- Coding: utf-8 -*-

{i:"a%03d"%i for i in range(3)}
# -> {0: 'a000', 1: 'a001', 2: 'a002'}
# dictのkey-valueの両方に対して，ループ変数を使える

{ i%10 for i in range(20)}
# -> {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# 集合型を内包表記で

(i*2 for i in range(10))                                                                                                                                                                    
# -> <generator object <genexpr> at 0x7fb2f5e41db0> 
# ジェネレータも内包表記できる

[ (i*3,j*2) for i in range(2) for j in range(3) ]
# -> [(0, 0), (0, 2), (0, 4), (3, 0), (3, 2), (3, 4)] 
# 二重内包表記のスマートな書き方
[ (i,j) for i in [-1,0,1] for j in [-1,0,1] if abs(i) + abs(j) == 1]
# -> [(-1, 0), (0, -1), (0, 1), (1, 0)] 
# 四近傍をワンラインで

for i in range(10) : pass
# ->
# 「何もしない」ができる
