class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> result;
        if(digits.length() == 0) {
            return result;
        }
        switch (digits[0]) {
        case '2':
            result = {"a", "b", "c"};
            break;
        case '3':
            result = {"d", "e", "f"};
            break;
        case '4':
            result = {"g", "h", "i"};
            break;
        case '5':
            result = {"j", "k", "l"};
            break;
        case '6':
            result = {"m", "n", "o"};
            break;
        case '7':
            result = {"p", "q", "r", "s"};
            break;
        case '8':
            result = {"t", "u", "v"};
            break;
        case '9':
            result = {"w", "x", "y", "z"};
        }
        if(digits.length() == 1) {
            return result;
        }
        vector<string> res;
        vector<string> nextCombination = letterCombinations(digits.substr(1));
        for (string &next : nextCombination) {
            for (string &cur : result) {
                string n = cur + next;
                res.push_back(n);
            }
        }
        return res;
    }
};
