# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        first = prev.next
        for _ in range(right - left):
            second = first.next
            first.next = second.next
            second.next = prev.next
            prev.next = second
        return dummy.next