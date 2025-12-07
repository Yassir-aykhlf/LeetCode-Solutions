/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode *dummy = malloc(sizeof(struct ListNode));
    dummy->next = head;
    struct ListNode *slow = dummy;
    struct ListNode *fast = dummy;
    for (int i = 0; i < n + 1; i++) {
        fast = fast->next;
    }
    while (fast != NULL) {
        fast = fast->next;
        slow = slow->next;
    }
    struct ListNode *to_delete = slow->next;
    slow->next = slow->next->next;
    free(to_delete);
    struct ListNode *result = dummy->next;
    free(dummy);
    return result;
}