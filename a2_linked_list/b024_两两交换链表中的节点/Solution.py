
from typing import Optional

from ListNode import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # 待翻转的两个node分别是pre和cur
        pre = head
        cur = head.next
        next = head.next.next

        cur.next = pre  # 交换
        pre.next = self.swapPairs(next)  # 将以next为head的后续链表两两交换

        return cur
