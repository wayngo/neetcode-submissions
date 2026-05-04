class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1 ) count how many times each element appears in our array and store it 
        #2 ) Based on how many times each eleemnt appears in our array we can look at our hashmap
        #3 ) We can add numbers to a list use their index for how many times they appear 
        #4 ) [[1,2,3], [4,5], [6,7]]
        #5 ) iterate backwards in the array 

        count = {}
        freq = [[] for i in range(len(nums) + 1)
]
        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = [] 
        for i in range(len(freq) - 1, 0 , -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
    