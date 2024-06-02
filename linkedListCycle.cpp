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
    bool hasCycle(ListNode *head) {
        if (!head || !head->next) {
            return false;
        }
        ListNode* ahead = head->next->next;
        while(ahead) {
            if (ahead == head) {
                break;
            }
            if (!ahead->next) {
                ahead = ahead-> next;
                break;
            }
            head = head->next;
            ahead = ahead->next->next;
        }
        delete(ahead);
        return ahead? true : false;
    }
};
