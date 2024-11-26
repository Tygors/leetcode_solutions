# Python3.9.12

import sys


class Solution:
    @staticmethod
    def sortedSquares(num_list: list[int]) -> list[int]:
        # 设置左右两个指针
        left = 0 
        right = len(num_list) - 1
        i = len(num_list) - 1
        # 存放结果的列表
        res: list[int] = [sys.maxsize] * len(num_list)
        # 因为原列表是【非递减顺序】有序的
        while left <= right:
            left_square = num_list[left] ** 2
            right_square = num_list[right] ** 2
            if left_square < right_square:
                res[i] = right_square
                right = right - 1
            else:
                res[i] = left_square
                left = left + 1
            i = i - 1

        return res
        