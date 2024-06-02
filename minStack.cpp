#include <queue>
#include <functional>
#include <unordered_map>
class MinStack {
private:
    vector<int> stack;
    priority_queue<int, vector<int>, greater<int>> minHeap;
    unordered_map<int, int> counter;
public:
    MinStack() {
    }
    
    void push(int val) {
        stack.push_back(val);
        minHeap.push(val);
        counter[val]++;
    }
    
    void pop() {
        int val = stack.back();
        stack.pop_back();
        if (--counter[val] <= 0) {
            counter.erase(val);
        }
    }
    
    int top() {
        return stack.back();
    }
    
    int getMin() {
        while(1) {
            int val = minHeap.top();
            if (counter.find(val) != counter.end()) {
                return val;
            }
            minHeap.pop();
        }
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
