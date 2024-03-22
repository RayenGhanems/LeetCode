# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a=[]
        current=head
        while current != None:
            a.append(current.val)
            current=current.next
        for i in range(int(len(a)/2)):
            if a[i]!=a[-i-1]:
                return 0
        return 1