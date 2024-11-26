from typing import List



class Solution:
    def bi_search(self, num_list: List[int], target: int) -> int:
        # 假设target存在于左闭右开区间
        left: int = 0
        right: int = len(num_list)

        while left < right:
            mid: int = left + (right - left) // 2
            if num_list[mid] > target:
                right = mid
            elif num_list[mid] < target:
                left = mid + 1
            else:
                #num_list[mid] == target # 找到了
                return mid
        return -1