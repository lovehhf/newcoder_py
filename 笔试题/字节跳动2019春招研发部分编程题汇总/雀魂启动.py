# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
小包最近迷上了一款叫做雀魂的麻将游戏，但是这个游戏规则太复杂，小包玩了几个月了还是输多赢少。
于是生气的小包根据游戏简化了一下规则发明了一种新的麻将，只留下一种花色，并且去除了一些特殊和牌方式（例如七对子等），具体的规则如下：

总共有36张牌，每张牌是1~9。每个数字4张牌。
你手里有其中的14张牌，如果这14张牌满足如下条件，即算作和牌
14张牌中有2张相同数字的牌，称为雀头。
除去上述2张牌，剩下12张牌可以组成4个顺子或刻子。顺子的意思是递增的连续3个数字牌（例如234,567等），刻子的意思是相同数字的3个数字牌（例如111,777）

例如：
1 1 1 2 2 2 6 6 6 7 7 7 9 9 可以组成1,2,6,7的4个刻子和9的雀头，可以和牌
1 1 1 1 2 2 3 3 5 6 7 7 8 9 用1做雀头，组123,123,567,789的四个顺子，可以和牌
1 1 1 2 2 2 3 3 3 5 6 7 7 9 无论用1 2 3 7哪个做雀头，都无法组成和牌的条件。

现在，小包从36张牌中抽取了13张牌，他想知道在剩下的23张牌中，再取一张牌，取到哪几种数字牌可以和牌。

输入描述:
输入只有一行，包含13个数字，用空格分隔，每个数字在1~9之间，数据保证同种数字最多出现4次。

输出描述:
输出同样是一行，包含1个或以上的数字。代表他再取到哪些牌可以和牌。若满足条件的有多种牌，请按从小到大的顺序输出。若没有满足条件的牌，请输出一个数字0

输入例子1:
1 1 1 2 2 2 5 5 5 6 6 6 9

输出例子1:
9

例子说明1:
可以组成1,2,6,7的4个刻子和9的雀头

输入例子2:
1 1 1 1 2 2 3 3 5 6 7 8 9

输出例子2:
4 7

例子说明2:
用1做雀头，组123,123,567或456,789的四个顺子

输入例子3:
1 1 1 2 2 2 3 3 3 5 7 7 9

输出例子3:
0

例子说明3:
来任何牌都无法和牌
"""

def isHu(nums):
    """
    判断是否可以胡牌
    :param nums:
    :return:
    """
    if not nums:
        return True
    l = len(nums)
    count0 = nums.count(nums[0])
    # 没出现过雀头，且第一个数字出现的次数 >= 2,去掉雀头剩下的能不能和牌
    if l % 3 != 0 and count0 >= 2 and isHu(nums[2:]) == True:
        return True
    # 如果第一个数字出现次数 >= 3，去掉这个刻子后看剩下的能和牌
    if count0 >= 3 and isHu(nums[3:]) == True:
        return True
    # 如果存在顺子，移除顺子后剩下的能和牌
    if nums[0] + 1 in nums and nums[0] + 2 in nums:
        last_nums = nums.copy()
        last_nums.remove(nums[0])
        last_nums.remove(nums[0] + 1)
        last_nums.remove(nums[0] + 2)
        if isHu(last_nums) == True:
            return True
    # 以上条件都不满足，则不能和牌
    return False

def main(nums):
    """
    最多有9种抽牌方法可以和牌，计算每一种能不能和牌
    除掉已经出现4次的牌,也就是遍历可以抓到的牌
    :return:
    """
    d = {}
    for i in nums:
        d[i] = d.get(i,0) + 1
    card_list = set(range(1,10)) - {i for i,v in d.items() if v==4}
    res = []
    for i in card_list:
        if isHu(sorted(nums + [i])):  # 如果这种抽牌方式可以和牌
            res.append(i)  # 加入和牌类型列表
    res = ' '.join(str(x) for x in sorted(res)) if res else '0'
    print(res)


s = "1 1 1 3 4 5 5 5 5 6 7 9 9"
nums = [int(x) for x in s.split()]
main(nums)

# 想的太复杂了 应该用递归解决
# def hu(nums):
#     """
#     所有胡牌的情况
#     :param nums:
#     :return:
#     """
#     if len(nums) == 7:
#         for i in range(1, 7):
#             if nums[i] - nums[i - 1] != 1:
#                 return 0
#         return [nums[0], nums[3], nums[6]]
#     elif len(nums) == 5:
#         if nums == [2, 3, 4, 5, 6]:
#             return [1, 4, 7]
#         if nums == [3, 4, 5, 6, 7]:
#             return [2, 5, 8]
#         if nums == [4, 5, 6, 7, 8]:
#             return [3, 6, 9]
#     elif len(nums) == 4:
#         if nums[1] - nums[0] == 1 and nums[2] - nums[1] == 1 and nums[3] - nums[2] == 1 and nums[4] - nums[3] == 1:
#             return [nums[0], nums[-1]]
#     elif len(nums) == 2:
#         if nums[1] == nums[0]:
#             return [nums[0]]
#         if nums[1] - nums[0] == 1:
#             if nums[1] != 9 and nums[0] != 0:
#                 return [nums[0] - 1, nums[1] + 1]
#             elif nums[0] == 0:
#                 return [3]
#             else:
#                 return [7]
#         if nums[1] - nums[0] == 2:
#             return [nums[1] - 1]
#     elif len(nums) == 1:
#         return [nums[0]]
#     else:
#         return 0
#
#
# def check(nums):
#     """
#     除掉雀头看剩下11个麻将能不能听牌
#     :param nums:
#     :return:
#     """
#     d = {}
#     for i in nums:
#         d[i] = d.get(i, 0) + 1
#     res = 0
#     for i, v in d.items():
#         if v >= 3:
#             for _ in range(3):
#                 nums.remove(i)
#
#     ls = [[1, 2, 3], [7, 8, 9], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8]]
#     i = 0
#     while i < len(ls):
#         if len(nums) <= 5:
#             res = hu(nums)
#             if res:
#                 break
#         if all(x in nums for x in ls[i]):
#             for j in ls[i]:
#                 nums.remove(j)
#         else:
#             i += 1
#     if res:
#         return res
#     return 0
#
#
# def check2(nums):
#     """
#     没有雀头的情况
#     胡牌的情况有剩下1,4,7个牌
#     :param nums:
#     :return:
#     """
#     d = {}
#     for i in nums:
#         d[i] = d.get(i, 0) + 1
#     res = 0
#     for i, v in d.items():
#         if v >= 3:
#             for _ in range(3):
#                 nums.remove(i)
#     ls = [[1, 2, 3], [7, 8, 9], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8]]
#     i = 0
#     while i < len(ls):
#         if len(nums) == 7 or len(nums)==4 or len(nums)==1:
#             res = hu(nums)
#             if res:
#                 break
#         if all(x in nums for x in ls[i]):
#             for j in ls[i]:
#                 nums.remove(j)
#         else:
#             i += 1
#     if res:
#         return res
#     return 0
#
#
# def main(nums):
#     # print(sorted(nums))
#     d = {}
#     for i in nums:
#         d[i] = d.get(i, 0) + 1
#     res = []
#     for i, v in d.items():
#         if v >= 2:
#             tmp = nums.copy()
#             for _ in range(2):
#                 tmp.remove(i)
#             r = check(tmp)
#             if r:
#                 res += r
#     r2 = check2(nums)
#     if r2:
#         res += r2
#     if res:
#         res = ' '.join(str(x) for x in sorted(set(res)))
#     else:
#         res = '0'
#     print(res)
#
#
# s = "2 1 4 9 2 9 3 3 9 9 8 7 3"
# nums = [int(x) for x in s.split()]
# main(nums)
