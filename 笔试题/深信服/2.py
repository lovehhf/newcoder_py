# -*- coding:utf-8 -*-

d = input()   # 输入第一行 加密字典
t = input()   # 输入第二行 加密还是解密
s = input()   # 输入第三行
encode_dict = {}
decode_dict = {}
d1 = ''.join([chr(ord('a')+i) for i in range(0,26)] + [str(i) for i in range(0,10)]) # a-z 0-9的字符串

for i in range(36):
    encode_dict[d1[i]] = d[i]    # 加密字典

for i in range(36):
    decode_dict[d[i]] = d1[i]    # 解密字典

res = ''
# 加密
if t == '1':
    for char in s:
        res += encode_dict[char]

# 解密
if t == '0':
    for char in s:
        res += decode_dict[char]