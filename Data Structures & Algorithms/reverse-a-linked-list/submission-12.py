class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        while head:
            next_node = head.next
            last_node = prev
            prev = head
            prev.next = last_node
            head = next_node

        return prev