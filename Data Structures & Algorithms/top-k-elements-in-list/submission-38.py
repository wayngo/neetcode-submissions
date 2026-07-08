class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        heap = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        #for every value within our count we push the number and 
        #and the amount of times it appears as a key value pair 

        for num in count.keys():
            heapq.heappush(heap, (count[num], num))

            if len(heap) > k :
                heapq.heappop(heap)
        
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res