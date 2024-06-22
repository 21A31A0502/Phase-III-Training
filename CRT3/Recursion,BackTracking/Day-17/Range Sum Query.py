from typing import List
class NumArray:
    def __init__(self, nums: List[int]):
        l = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            l[i] = l[i - 1] + nums[i]
        self.nums = nums
        self.l = l

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.l[right]
        return self.l[right] - self.l[left - 1]
nums = [1, 2, 3, 4, 5]
num_array = NumArray(nums)
print(num_array.sumRange(0, 2))  # Output: 6
print(num_array.sumRange(1, 3))  # Output: 9
print(num_array.sumRange(2, 4))    