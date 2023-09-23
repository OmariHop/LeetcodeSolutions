class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sorting the array to utilize the iterative approach 
        nums.sort()
        length = len(nums)
        
        # To avoid IndexError
        for i in range(length - 1):  
            if nums[i] + 1 != nums[i + 1]:
                return nums[i] + 1

        # Handle the case when the missing number is 0 or the largest number in the sequence
        return 0 if nums[0] != 0 else length


        # Time complexity nlogn sort() + one iterative pass through our array
        # O(nlogn)

        
