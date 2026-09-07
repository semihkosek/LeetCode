class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        gorulenler = {}  
        
        for i, num in enumerate(nums):
            kalan = target - num
            if kalan in gorulenler:
                return [gorulenler[kalan], i]
            
            gorulenler[num] = i