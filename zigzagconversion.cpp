class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows == 1) return s;
        int L = s.length();
        string res = "";
        int MAX = 2 * (numRows - 1);
        for (int r = 0; r < numRows; r++) {
            int start = r;
            int hop = MAX - 2 * r;
            int revhop = MAX - hop;
            if(hop == 0) {
                hop = MAX;
            } else if(revhop == 0) {
                revhop = MAX;
            }
            while (start < L) {
                res += s[start];
                start += hop;
                if (start >= L) break;
                res += s[start];
                start += revhop;
            }
        }
        return res;
    }
};
