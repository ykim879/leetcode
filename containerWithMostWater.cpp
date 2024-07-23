#include <algorithm>
class Solution {
public:
    int maxArea(vector<int>& height) {
        //initialize left and right index maxArea
        int l = 0; int r = height.size() - 1; 
        int maxArea = (r-l) * min(height[r], height[l]);
        while (l < r) {
            if (height[l] <= height[r]) {
                int org = height[l];
                for (; l < r; l++) {
                    if (height[l] > org) {
                        break;
                    }
                }
            } else if(height[l] > height[r]) {
                int org = height[r];
                for (; l < r; r--) {
                    if (height[r] > org) {
                        break;
                    }
                }
            }
            //  update max if nededed
            maxArea = max(maxArea, (r-l) * min(height[r], height[l]));
        }
        return maxArea; 
    }
};
