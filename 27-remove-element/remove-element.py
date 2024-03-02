class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for n in range(len(nums)):
            if nums[n] != val:
                nums[k] = nums[n]
                k += 1
        return k