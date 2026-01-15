# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        a = dummy
        for _ in range(left - 1):
            a = a.next
        b = a.next
        for _ in range(right - left):
            c = b.next
            b.next = c.next
            c.next = a.next
            a.next = c
        return dummy.next