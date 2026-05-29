class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hm = {}

        # for num in nums:
        #     if num in hm:
        #         return True
        #     else:
        #         hm[num] = 1

        # return False

        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        
        return False
        