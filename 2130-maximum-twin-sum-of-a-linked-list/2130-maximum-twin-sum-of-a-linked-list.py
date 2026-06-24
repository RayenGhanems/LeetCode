# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l = []
        while head != None:
            l.append(head.val)
            head = head.next

        n=len(l)  ## which is an even number
        
        if n ==2:
            return sum(l)

        l = [a + b for a, b in zip(l[:n//2], l[-1:n//2 - 1:-1])]
        return max(l)

        # out = l[0]+ l[-1]
        # for i in range(1,int(len(l)/2)):
        #     out = max(out, l[i]+l[-(i+1)])
        # return out
        
        