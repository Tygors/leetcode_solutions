from typing import List

class Solution:
    def removeElement(self, num_list: List[int], val_to_del:int) -> int:
        left: int = 0
        right: int = len(num_list) - 1
        while left <= right:
            while left <= right and num_list[left] != val_to_del:
                left = left + 1
            while left <= right and num_list[right] == val_to_del:
                right = right - 1
            if left < right:
                num_list[left] = num_list[right]
                left = left + 1
                right = right - 1
        return left
