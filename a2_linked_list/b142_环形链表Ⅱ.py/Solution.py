from ListNode import ListNode

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # 如有环，则快指针fast和慢指针slow总会相遇
            if slow == fast:
                # 将其中一个指针移动回列表的开始
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        # 无环时返回None
        return None