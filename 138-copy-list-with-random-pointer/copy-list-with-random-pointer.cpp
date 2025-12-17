// class Node {
// public:
//     int val;
//     Node* next;
//     Node* random;
    
//     Node(int _val) {
//         val = _val;
//         next = NULL;
//         random = NULL;
//     }
// };

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head)
            return nullptr;
        std::unordered_map<Node*, Node*> old_new;
        old_new[nullptr] = nullptr;
        Node *curr = head;
        while (curr) {
            old_new[curr] = new Node(curr->val);
            curr = curr->next;
        }
        curr = head;
        while (curr) {
            old_new[curr]->next = old_new[curr->next];
            old_new[curr]->random = old_new[curr->random];
            curr = curr->next;
        }
        return old_new[head];
    }
};