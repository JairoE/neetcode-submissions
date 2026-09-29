class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}

        for num in nums: 
            if num in numCount: 
                numCount[num] +=1
            else:
                numCount[num] = 1
        
        sorted_items = sorted(numCount.items(), key=lambda item: item[1], reverse=True)
        return [num for num, count in sorted_items[:k]]
        