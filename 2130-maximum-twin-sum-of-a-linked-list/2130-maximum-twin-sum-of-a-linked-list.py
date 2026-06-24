# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ############################# solution 1
        # l = []
        # while head != None:
        #     l.append(head.val)
        #     head = head.next

        # n=len(l)  ## which is an even number

        # if n ==2:
        #     return sum(l)

        # l = [a + b for a, b in zip(l[:n//2], l[-1:n//2 - 1:-1])]
        # return max(l)
        ################################# solution 2
        # out = l[0]+ l[-1]
        # for i in range(1,int(len(l)/2)):
        #     out = max(out, l[i]+l[-(i+1)])
        # return out
        
        ################################## solution 3
        l, slow, fast, i= [], head, head, 1
        while fast and fast.next:
            fast = fast.next.next
            l.append(slow.val)
            slow = slow.next
        
        out = slow.val + l[-i]
        while slow.next:
            i += 1
            slow = slow.next
            out = max(out, slow.val + l[-i])
        return out

        
            