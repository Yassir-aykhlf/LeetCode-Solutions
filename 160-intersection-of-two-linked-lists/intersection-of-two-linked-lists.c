/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode *ra = headA;
    struct ListNode *rb = headB;
    while (ra != rb) {
        ra = ra ? ra->next : headB;
        rb = rb ? rb->next : headA;
    }
    return ra;
}