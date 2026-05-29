class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {nums[len(nums)-1] : len(nums)-1}

        for i in range(len(nums)-2, -1, -1):
            goal = target - nums[i]
            if goal in hm:
                return [i, hm[goal]]
            else:
                hm[nums[i]] = i
        
        return []
            