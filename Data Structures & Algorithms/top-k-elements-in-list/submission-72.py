class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        
        res = []
        for num in range(len(heap)):
            freq, n = heapq.heappop(heap)
            res.append(n)
        return res