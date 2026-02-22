/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode* runnerA = malloc(sizeof(struct ListNode*));
    struct ListNode* runnerB = malloc(sizeof(struct ListNode*));
    runnerA = headA;
    runnerB = headB;
    while (runnerA != runnerB) {
        if (runnerA == NULL) {
            runnerA = headB;
        }
        else {
            runnerA = runnerA->next;
        }
        if (runnerB == NULL) {
            runnerB = headA;
        }
        else {
            runnerB = runnerB->next;
        }
    }
    return runnerA;
}