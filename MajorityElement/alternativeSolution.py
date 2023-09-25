class Solution:
    def majorityElement(self, nums: List[int]) -> int:

      # Sorting the array, for the majority element the number from the middle to the end of the array is gauarenteed to be in the middle
      #nlogn runtime because of sorting
        nums.sort()
        length = len(nums) - 1

        n = nums[int(length/2)]


        return n
        
