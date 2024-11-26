class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        if self.next == None:
            return f"[{self.val}]"
        ret = []
        while self.next!=None:
            ret.append(self.val)
            self = self.next
        return str(ret)