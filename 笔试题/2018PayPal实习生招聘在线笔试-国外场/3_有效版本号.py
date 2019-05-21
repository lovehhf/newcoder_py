# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
现在给出一棵树，树的结点名字表示项目的名称和版本号，用逗号分隔，例如结点名字为a,1表示项目的名称为a，版本号为1。
每个结点的名字都是唯一的。但树里可以出现项目名称相同，但版本号不同的结点。
对于某个名称的项目来说，**真正有效的版本号是距离根节点最近的是这个项目名称的结点里的版本号。**
如果**多个相同项目名称，不同版本的结点距离根节点的距离相同，则生效版本为在输入中先出现的结点的版本**。
此外，输入中给出的依赖关系可能存在循环依赖的例外情况，例如a,1依赖b,1，b,1又依赖a,1，这种情况就不是一颗有效的树。

输入描述:
输入由多行组成。
第一行是要检查的项目的名称，要检查的项目必定会存在于输入中。
第二行是根节点的项目名称及版本号。
接下来每行表示两个项目之间的依赖关系。用->表示前者依赖后者，即后者是前者的子节点。
例如a,1->b,1，表示1版本的a依赖1版本的b。
结点名字由项目名称和版本号组成，用逗号分隔，项目名称是a-z的单个字符，版本号是1-9的正整数。

输出描述:
如果给的输入能组成一颗有效的树，则输出要检查的项目的生效版本号。
如果给的输入不能组成一颗有效的树，则输出-1。

输入例子1:
e
a,1
b,1->e,2
c,1->e,1
a,1->b,1
a,1->c,1
a,1->d,1

输出例子1:
2

例子说明1:
e,2和e,1离根节点的距离一样，但e,2先出现在输入中，所以e生效的版本是2

输入例子2:
b
a,1
a,1->b,1
a,1->c,1
d,1->a,1
b,1->d,1

输出例子2:
-1

例子说明2:
由于存在a,1->b,1->d,1->a,1的循环依赖，无法构建出有效的树，依赖关系无效，所以输出为-1
"""

import sys


def solve(r):
    pass


def main():
    r = []
    c = input()
    root = input()
    d = {root: 0}
    queue = []
    for line in sys.stdin:
        line = line.strip()
        # if not line:
        #     break
        a, b = line.split('->')
        r.append((a, b))
        if b in d:
            return -1
        if a in d:
            d[b] = d[a] + 1
        else:
            queue.append((a, b))
        # print(a,b,d)
    # print(queue)
    while queue:
        a, b = queue.pop(0)
        if a in d:
            d[b] = d[a] + 1
        else:
            queue.append((a, b))
    if c == root[0]:
        return root[2]
    res = []
    for k, v in d.items():
        if k[0] == c:
            res.append((k, v))
    res.sort(key=lambda x: x[1])
    res = [x for x in res if x[1] == res[0][1]]
    for i in r:
        if i[1] in [x[0] for x in res]:
            return i[1][2]

    # return r[0][0]


ans = main()
print(ans)
