# -*- coding:utf-8 -*-

__author__ = 'huanghf'

import re

s = 'aabcddefg'
sub_string = 'a?c'

sub_string = re.sub('\?', '[^\0.]{1,3}', sub_string)
print(sub_string)
# sub_string = '[^\0.]'
result = re.findall(sub_string, s)
if not result:
    print(-1)
else:
    min_len = min([len(x) for x in result])
    print(min_len)
