# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        anchor = dummy
        for _ in range(left - 1):
            anchor = anchor.next
        curr = anchor.next
        for i in range(right - left):
            curr_next = curr.next
            curr.next = curr_next.next
            curr_next.next = anchor.next
            anchor.next = curr_next
        return dummy.next