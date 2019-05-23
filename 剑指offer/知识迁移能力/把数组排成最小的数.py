# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

重新定义排序方式

3+32>32+3 -> 3>32
321+32<32+321 -> 321<32
x+y<y+x --> x<y
"""


class Solution:
    def PrintMinNumber(self, numbers):
        """
        假三路快排
        :param numbers:
        :return:
        """
        nums = [str(x) for x in numbers]

        def quickSort(nums):
            if not nums:
                return ''
            l = [x for x in nums if int(x + nums[0]) < int(nums[0] + x)]
            m = [x for x in nums if int(x + nums[0]) == int(nums[0] + x)]
            r = [x for x in nums if int(x + nums[0]) > int(nums[0] + x)]
            return quickSort(l) + ''.join(m) + quickSort(r)

        return quickSort(nums)

    def PrintMinNumber2(self, numbers):
        """
        Python sorted函数的cmp参数
        :param numbers:
        :return:
        """
        from functools import cmp_to_key
        func = lambda x, y: int((x + y)) - int((y + x))
        nums = sorted([str(x) for x in numbers], key=cmp_to_key(func))
        return ''.join(nums)

    def PrintMinNumber3(self, numbers):
        # write code here
        if not numbers:
            return ""
        numbers = list(map(str, numbers))
        n = len(numbers)
        # 冒泡排序
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                # j+1和j拼装出的数<j和j+1拼装出的数时 交换j和j+1 保证更小的在前面
                if int(numbers[j + 1] + numbers[j]) < int(numbers[j] + numbers[j + 1]):
                    numbers[j + 1], numbers[j] = numbers[j], numbers[j + 1]
                # print(numbers)
        return ''.join(numbers)


s = Solution()
print(s.PrintMinNumber([3, 32, 321]))
print(s.PrintMinNumber2([3, 32, 321]))
