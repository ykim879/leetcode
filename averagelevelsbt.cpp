/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> res;
        if(!root) {
            return res;
        }
        vector<TreeNode*> cur = {root};
        while(!cur.empty()) {
            vector<TreeNode*> next;
            double sum = 0;
            double count = cur.size();
            while(!cur.empty()) {
                TreeNode* n = cur.back();
                cur.pop_back();
                if(n->left) {
                    next.push_back(n->left);
                }
                if(n->right) {
                    next.push_back(n->right);
                }
                sum += n->val;
            }
            res.push_back(sum / count);
            cur = next;
        }
        return res;
     }
};
