class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # solve using a hashmap

        hm = {}

        # nums[i] - target = x --> see if that x is already in the hm

        for i in range(len(nums)-1, -1, -1):
            diff = target - nums[i]
            if diff in hm:
                return [i, hm[diff]]
            hm[nums[i]] = i

