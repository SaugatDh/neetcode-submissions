# import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]

        for num,freq in count.items():
            bucket[freq].append(num)
        
        res = []

        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                res.append(n)
                if len(res)==k:
                    return res


        # count = Counter(nums)
        # heap =[]

        # for num,freq in count.items():
        #     heapq.heappush(heap,(freq,num))
            
        #     if len(heap)>k:
        #         heapq.heappop(heap)
        
        # return [num for freq,num in heap]
        # count = Counter(nums)
        # result = []
        # sorted_items = sorted(count.items(),key=lambda x:x[1],reverse=True)
        # for item in sorted_items[:k]:
        #     result.append(item[0])
        # return result