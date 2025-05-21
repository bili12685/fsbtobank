#!/usr/bin/env python
# visit https://tool.lu/pyc/ for more information
# Version: Python 3.10

import binascii

def find_all_occurrences(text, pattern):
    occurrences = []
    start = 0
    while True:
        index = text.find(pattern, start)
        if index == -1:
            break  
        occurrences.append(index)
        start = index + 1
    return occurrences

def creat(hex_data, filename):
    binary_data = binascii.unhexlify(hex_data)
    with open(filename, 'wb') as file:
        file.write(binary_data)
# WARNING: Decompyle incomplete


def r(filename):
    with open(filename, 'rb') as file:
        data = file.read()
    hex_data = binascii.hexlify(data)
    d=hex_data.decode("utf-8")
    return d
# WARNING: Decompyle incomplete

print('请将原bank文件、新fsb、本程序放在同一文件夹下！')
print('原文件名为weapon.bank,打入fsb为untitled.fsb，新生成文件名为new.bank')
f1 = './weapon.bank'
d = r(f1)
snd = '534e4420'
fsb = '465342350100'
l1 = find_all_occurrences(d, snd)
l2 = find_all_occurrences(d, fsb)
print(f"找到的 snd 索引: {l1}")
print(f"找到的 fsb 索引: {l2}")
sndindex = []
fsbindex = []
for i in l1:
    if i % 2 == 0:
        sndindex.append(i)
for i in l2:
    if i % 2 == 0:
        fsbindex.append(i)
if len(sndindex) != len(fsbindex):
    print('有错误！！！')
l = len(d)
print(sndindex, fsbindex)
fsblist = []
for i in range(len(sndindex)):
    if i == len(sndindex) - 1:
        t = (l - fsbindex[i]) / 2
        fsblist.append(t)
        print('fsb{0}文件大小：{1}'.format(i + 1, t))
        continue
    t = (sndindex[i + 1] - fsbindex[i]) / 2
    fsblist.append(t)
    print('fsb{0}文件大小：{1}'.format(i + 1, t))
f2 = './untitled.fsb'
newfsb = r(f2)
n = len(newfsb)
print('新fsb文件大小：', n / 2)
x = 1
if n / 2 > fsblist[x - 1]:
    print('超过原本大小！')
else:
    newbank = d.replace(d[fsbindex[x - 1]:fsbindex[x - 1] + n], newfsb)
    f2 = 'new.bank'
    creat(newbank, f2)
input('按回车退出')
