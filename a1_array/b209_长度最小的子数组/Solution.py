# 209.长度最小的子数组

import sys


class Solution:
    @staticmethod
    def minSubArrayLen(target: int, num_list: list[int]) -> int:
        n = len(num_list)
        left, right = 0, 0
        min_len: int = sys.maxsize
        sum = 0

        # 当右指针还没到达列表末尾
        while right < n:
            sum  = sum + num_list[right]

            # 如果累加值已经大于目标值或者等于目标值时，则滑动窗口，然后尝试更新最小长度
            while sum >= target:
                min_len = min(min_len, right - left + 1)
                sum = sum - num_list[left]
                left = left + 1

            right = right + 1
        
        ans: int = min_len if min_len != sys.maxsize else 0
        return ans

