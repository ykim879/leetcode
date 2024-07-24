class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() == 0) {
            return 0;
        }
        int res = 0; int l = 0; int r = 1;
        set<int> visited = {s[0]};
        for(; r < s.size(); r++) {
            if (visited.find(s[r]) != visited.end()) {
                res = max(res, r-l);
                while(l < r) {
                    visited.erase(s[l]);
                    if(s[l++] == s[r]) {
                        break;
                    }
                }
            }
            visited.insert(s[r]);
        }
        return max(res, r-l);
    }
};
