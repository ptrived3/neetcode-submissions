class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        
        for i,n in enumerate(nums):
            num = target - n
            if num in hm:
                return [hm[num], i]
            hm[n] = i
        
        return []