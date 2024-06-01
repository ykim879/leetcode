#include <unordered_map>
using namespace std;
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        if (ransomNote.length() == 0) {
            return true;
        }
        //populate ransomeNote as dictionary
        unordered_map<char, int> dict;
        for (char c : ransomNote) {
            dict[c]++;
        }
        //when magazine have anyof key of ransomeNote decrement and erase if it is 0. 
        for (char c: magazine) {
            if (dict.find(c) != dict.end()) {
                dict[c] -= 1;
                if (dict[c] <= 0) {
                    dict.erase(c);
                    if(dict.empty()) {
                        return true;
                    }
                }
            }
        }
        //when dict become empty return true
        return false;
    }
};
