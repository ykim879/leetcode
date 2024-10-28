class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort inplace intervals with start date to save time
        intervals.sort(key=lambda x: x[0])
        # stack
        stack = []
        for interval in intervals:
            if stack and stack[-1][1] >= interval[0]:
                stack[-1][1] = max(stack[-1][1], interval[1])
            else:
                stack.append(interval)
        return stack
