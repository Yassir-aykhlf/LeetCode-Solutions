# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow =slow.next
            fast =fast.next.next
        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next =prev
            prev=cur
            cur=nxt
        l,r=head,prev
        while r:
            if r.val != l.val:
                return False
            l = l.next
            r = r.next
        return True