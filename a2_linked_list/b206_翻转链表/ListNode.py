
from typing import Union


class ListNode:
    def __init__(self, val=0, next: Union["ListNode", None] = None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        if not self.next:
            return "[]"
        ret = []
        cur = self.next
        while cur:
            ret.append(cur.val)
            cur = cur.next
        return str(ret)