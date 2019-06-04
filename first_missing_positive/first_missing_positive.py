class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        end = len(nums) - 1
        for i in range(len(nums)):
            num = nums[i]
            while num > 0 and num <= len(nums) and num != nums[num - 1]:
                next_num = nums[num - 1]
                nums[num - 1] = num
                num = next_num
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
