class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: if the list is empty or has only one node, return head
        if not head or not head.next:
            return head
        
        # Initialize pointers
        new_head = head.next  # After swapping, the second node becomes the new head
        prev = None
        current = head
        
        while current and current.next:
            first = current
            second = current.next
            
            # Swap the pair
            first.next = second.next
            second.next = first
            
            # Update the previous node to point to the current pair's second node
            if prev:
                prev.next = second
            
            # Move pointers for the next pair
            prev = first
            current = first.next
        
        return new_head
