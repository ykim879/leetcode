class Solution {
public:
    int getMinimumDifference(TreeNode* root) {
        int minDiff = INT_MAX;
        int prevVal = -1; // -1 indicates no previous value has been set yet
        inOrderTraversal(root, prevVal, minDiff);
        return minDiff;
    }

private:
    void inOrderTraversal(TreeNode* node, int& prevVal, int& minDiff) {
        if (!node) return;

        // In-order traversal: left, root, right
        inOrderTraversal(node->left, prevVal, minDiff);

        // Process current node
        if (prevVal != -1) {
            minDiff = std::min(minDiff, std::abs(node->val - prevVal));
        }
        prevVal = node->val;

        inOrderTraversal(node->right, prevVal, minDiff);
    }
};
