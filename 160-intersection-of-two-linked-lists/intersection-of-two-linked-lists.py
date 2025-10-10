# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        rA = headA
        rB = headB
        while rA != rB:
            if rA == None:
                rA = headB
            else:
                rA = rA.next
            if rB == None:
                rB = headA
            else:
                rB = rB.next
        return rA