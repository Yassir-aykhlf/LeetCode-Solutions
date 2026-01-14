# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_head = ListNode(-1)
        s = smaller_head
        greater_head = ListNode(-1)
        g = greater_head
        curr = head
        while curr:
            if curr.val < x:
                s.next = curr
                s = s.next
            else:
                g.next = curr
                g = g.next
            curr = curr.next
        g.next = None
        s.next = greater_head.next
        return smaller_head.next
