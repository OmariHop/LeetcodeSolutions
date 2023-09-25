class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pos = 0  # position to place the next non-zero element
        
        # Traverse the list
        for num in nums:
            if num != 0:  # If the current element is not zero,
                nums[zero_pos] = num  # place it at the zero_pos index
                zero_pos += 1  # Move zero_pos to the next index
        
        # After placing all the non-zero elements at the beginning of the array,
        # fill the remaining positions with zeros.
        for i in range(zero_pos, len(nums)):
            nums[i] = 0
