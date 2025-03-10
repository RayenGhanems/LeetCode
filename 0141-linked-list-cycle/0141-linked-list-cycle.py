# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while(fast):
            slow = slow.next
            fast = fast.next
            if(fast is None):
                return 0
            fast = fast.next
            if(fast == slow):
                return 1
        return 0