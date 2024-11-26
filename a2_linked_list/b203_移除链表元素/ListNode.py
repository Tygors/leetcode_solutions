from typing import Union


# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next: Union["ListNode", None] = None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        if not self.next:
            return "[]"
        ret = []
        while self.next:
            ret.append(self.val)
            self = self.next
        return str(ret)