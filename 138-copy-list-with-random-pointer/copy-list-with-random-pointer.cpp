/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        std::unordered_map<Node*, Node*> cur_copy;
        Node* cur = head;
        while (cur) {
            Node* node = new Node(cur->val);
            cur_copy[cur] = node;
            cur = cur->next;
        }
        cur = head;
        while (cur) {
            Node* node = cur_copy[cur];
            node->next = cur_copy[cur->next];
            node->random = cur_copy[cur->random];
            cur = cur->next;
        }
        return cur_copy[head];
    }
};