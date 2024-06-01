#include <vector>
#include <set>
#include <string>
using namespace std;
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        set<string> s;
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] != '.') {
                    string cur(1, board[r][c]);  // Correct conversion from char to string
                    string arr[] = {
                        cur + "r" + to_string(r),  // Use string literals for 'r', 'c'
                        cur + "c" + to_string(c),
                        cur + to_string(r / 3) + to_string(c / 3)
                    };
                    for (int i = 0; i < 3; i++) {
                        if (s.find(arr[i]) != s.end()) {
                            return false;
                        }
                        s.insert(arr[i]);
                    }
                }
            }
        }
        return true;
    }
};
