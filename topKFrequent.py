class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter -> for each counter elements we are going to sort them and return the sorted[:k]
        # O(n) + O(nlogn) + O(1)
        # O(n) + monolithic stack(inside of stack's count is dynamic and cannot be sure this stack is monolithic) of length k vs min heap with k elements O(nlogk)
        counter = Counter(nums)
        h = []
        for num, count in counter.items():
            heapq.heappush(h, (count, num))
            if len(h) > k:
                heapq.heappop(h)
        return [num for _, num in h]
