class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        fmap = defaultdict(int)
        for num in nums:
            fmap[num] += 1
        
        heapArr = []

        for num, freq in fmap.items():
            heapq.heappush(heapArr,(freq,num))

            if len(heapArr) > k:
                heapq.heappop(heapArr)
        
        return [num for freq,num in heapArr]
        