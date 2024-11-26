# 203.移除链表元素
from typing import Optional
from ListNode import ListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 设置一个虚拟的头节点，原链表的所有节点可以按统一的方式删除
        vir_head: ListNode = ListNode(next = head)
        cur_node: ListNode = vir_head
        # 遍历所有节点，找到val进行删除
        while cur_node.next:
            if cur_node.next.val == val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next

        return vir_head.next # 返回真正的链表头
