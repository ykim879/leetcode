class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i1 = s.length() - 1;
        //loop then each time decrement i2
        for (int i2 = t.length() - 1; i2 >= 0; i2--) {
        // if i1 is s.rend() then return true
            if (i1 < 0) {
                return true;
            }
            //same then decrement i1
            if (s[i1] == t[i2]) {
                i1--;
            }
        }
        return i1 < 0 ? true : false;
    }
};
