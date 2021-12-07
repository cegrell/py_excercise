from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:        
        num = []
        while head != None:
            num.append(head.val)
            head = head.next
        return int("".join(str(i) for i in num),2)


print(Solution().getDecimalValue(ListNode(1, ListNode(0, ListNode(1)))))
