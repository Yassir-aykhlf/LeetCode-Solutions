# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        r1, r2 = headA, headB
        while r1 != r2:
            if r1 != None:
                r1 = r1.next
            else:
                r1 = headB
            if r2 != None:
                r2 = r2.next
            else:
                r2 = headA
        return r1