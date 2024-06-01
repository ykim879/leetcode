#include <string>
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> res;
        if (nums.size() == 0) {
            return res;
        }
        string before = "";
        string arw = "->";
        for (int i = 0; i < nums.size() - 1; i++){
            if(before.empty()) {
                if (nums[i] + 1 != nums[i+1]) {
                    res.push_back(to_string(nums[i]));
                } else {
                    before = to_string(nums[i]);
                }
            } else if (nums[i] + 1 != nums[i+1]) {
                res.push_back(before + arw + to_string(nums[i]));
                before.clear();
            }
        }
        string cur = to_string(nums[nums.size() - 1]);
        before.empty() ? res.push_back(cur) : res.push_back(before + arw + cur);
        return res;
    }
};
