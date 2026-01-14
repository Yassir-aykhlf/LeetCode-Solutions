# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller = ListNode(-1)
        s = smaller
        greater_or_equal = ListNode(-1)
        g = greater_or_equal
        curr = head
        while curr:
            if curr.val < x:
                s.next = ListNode(curr.val)
                s = s.next
            else:
                g.next = ListNode(curr.val)
                g = g.next
            curr = curr.next
        s.next = greater_or_equal.next
        return smaller.next
