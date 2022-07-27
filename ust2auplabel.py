# coding: utf-8

import os
import math
import utaupy

def tempo2ms(length, bpm):
    # 長さとテンポから秒数を計算する
    #ms = math.floor(( length / 480  * 60 / bpm ) * 1000000 ) / 1000000
    ms = length / 480  * 60 / bpm 
    return ms

def floor6(decimal):
    # 小数点以下6桁に丸める関数
    decimal = math.floor( decimal * 1000000 ) / 1000000
    return decimal

def main():
    # まずustオブジェクトとして読み込み
    fname = 'fanta.ust'
    ustobj = utaupy.ust.load(fname)
    # print(ustobj.tempo)
    sum_ms = 0
    
    # ファイルがあれば削除
    if(os.path.isfile('ラベルトラック.txt')):
        os.remove('ラベルトラック.txt')

    for item in ustobj.notes:
        note_length = item["Length"]
        note_lyric = item["Lyric"]
        
        # 長さとテンポを整数にして引数にする
        ms = tempo2ms(int(note_length), int(float(ustobj.tempo)))
        # 小数点以下6桁に丸める
        ms = floor6(ms)

        output_data = str(sum_ms) + '\t' + str(floor6(sum_ms + ms)) + '\t' + str(note_lyric) + '\n'
        # 秒数を足して小数点以下6桁に丸める
        sum_ms = floor6( sum_ms + ms )

        # ファイルオープン
        with open('ラベルトラック.txt', 'a', encoding='UTF-8') as f:
            f.write( output_data )

if __name__ == '__main__':
    main()