# 347. Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = 1  + freq.get( n , 0 )

        heap = []
        for n , freq in freq.items():
            heapq.heappush( heap , ( freq , n ))
        
        m = heapq.nlargest( k , heap )
        res = [ n for freq , n in m ]
        return res
