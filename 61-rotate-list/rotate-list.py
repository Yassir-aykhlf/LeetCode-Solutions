# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n += 1
        k = k % n
        tail.next = head
        tail = head
        for _ in range(n - k - 1):
            tail = tail.next
        new_head = tail.next
        tail.next = None
        return new_head