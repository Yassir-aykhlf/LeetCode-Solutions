/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *rA = headA;
        ListNode *rB = headB;
        while (rA != rB) {
            rA = rA ? rA->next : headB;
            rB = rB ? rB->next : headA; 
        }
        return rA;
    }
};