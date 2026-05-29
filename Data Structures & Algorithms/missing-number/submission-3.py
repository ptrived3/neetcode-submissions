class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        
        missing = 0
        for i in range(0,len(nums)-1):
            if nums[i+1] != (nums[i] + 1):
                missing = nums[i] + 1

        if missing == 0:
            return int(len(nums))

        
        return missing