from typing import Union


# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next: Union["ListNode", None] = None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        ret = []
        ret.append(self.val)
        cur = self.next
        while cur:
            ret.append(cur.val)
            cur = cur.next
        return str(ret)