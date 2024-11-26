# 059.螺旋矩阵II

import sys


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        # 初始化n x n的矩阵
        nums: list[list[int]] = [[sys.maxsize] * n for _ in range(n)]
        x_start = 0
        y_start = 0
        loop_cnt = n // 2
        mid = n // 2
        cnt = 1
        for offset in range(1, loop_cnt + 1):
            for i in range(y_start, n - offset):
                nums[x_start][i] = cnt
                cnt = cnt + 1
            for i in range(x_start, n - offset):
                nums[i][n - offset] = cnt
                cnt = cnt + 1
            for i in range(n - offset, y_start, -1):
                nums[n - offset][i] = cnt
                cnt = cnt + 1
            for i in range(n - offset, x_start, -1):
                nums[i][y_start] = cnt
                cnt = cnt + 1
            x_start = x_start + 1
            y_start = y_start + 1
            
        if n % 2 != 0:
            nums[mid][mid] = cnt
        return nums
