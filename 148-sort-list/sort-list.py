# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Given the head of a linked list, return the list after sorting it in ascending order.
    """
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        return self.mergeSort(head)
        
    def mergeSort(self, head):
        if not head or not head.next:
            return head
        first = head
        mid = self.findMid(head)
        second = mid.next
        mid.next = None
        sorted_first = self.mergeSort(first)
        sorted_second = self.mergeSort(second)
        return self.mergeList(sorted_first, sorted_second)

    def findMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeList(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next