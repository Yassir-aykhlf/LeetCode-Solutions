# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        l = head
        mid = self.getMid(head)
        r = mid.next
        mid.next = None
        l_sorted = self.sortList(l)
        r_sorted = self.sortList(r)
        return self.merge(l_sorted, r_sorted)

    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, lst1, lst2):
        dummy = ListNode(-1)
        curr = dummy
        while lst1 and lst2:
            if lst1.val < lst2.val:
                curr.next = lst1
                lst1 = lst1.next
            else:
                curr.next = lst2
                lst2 = lst2.next
            curr = curr.next
        curr.next = lst1 or lst2
        return dummy.next