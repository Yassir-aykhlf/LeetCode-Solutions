# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = head
        even_head = prev.next
        while prev.next and prev.next.next:
            odd = prev
            even = prev.next
            odd.next = even.next
            even.next = even.next.next
            prev = odd.next
        prev.next = even_head
        return head