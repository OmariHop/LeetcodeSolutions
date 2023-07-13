class Solution(object):
    def search(self, nums, target):
        if len(nums) == 0:
            return -1

        low = 0
        high = len(nums) - 1

        while(low<=high):
            mid = (low + high) // 2
            if nums[mid] > target:    
                high = mid -1  
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] == target:
                return mid

        return - 1
