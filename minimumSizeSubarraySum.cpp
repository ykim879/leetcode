class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int N = nums.size();
        int si = 0;
        int res = N + 1;
        int cur = 0;
        for (int i = 0; i < N; i++) {
            cur += nums[i];
            if (i - si + 1 >= res) {
                cur -= nums[si++];
            }
            if (cur >= target) {
                while(cur - nums[si] >= target) {
                    cur -= nums[si++];
                }
                res = i - si + 1;
            }
        }
        return res > N ? 0 : res;
    }
};
