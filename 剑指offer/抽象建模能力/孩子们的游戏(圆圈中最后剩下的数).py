# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。
其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。
每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,
从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。
请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
"""


class Solution:
    def remove_num(self, nums, start, m):
        """
        从指定索引开始删除报数为m的元素
        :param nums:
        :param start:
        :param m:
        :return: 下一次报数开始的索引,新数组
        """
        n = len(nums)
        pop_index = (m + start - 1) % n
        nums.pop(pop_index)
        return pop_index, nums

    def LastRemaining_Solution(self, n, m):
        if n==0 and m==0:
            return -1

        nums = list(range(n))
        i = 0
        while len(nums) > 1:
            i, nums = self.remove_num(nums, i, m)
            # print(nums)
        return nums[0]


s = Solution()
print(s.LastRemaining_Solution(5,3))
