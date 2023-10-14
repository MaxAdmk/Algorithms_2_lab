from typing import List
import unittest


def three_sum(target: int, nums: List[int]) -> bool:
    nums.sort()
    count = 0
    for i, a in enumerate(nums):

        if i > 0 and a == nums[i-1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            count += 1
            three_sum = a + nums[l] + nums[r]
            if three_sum > target:
                r -= 1
            elif three_sum < target:
                l += 1
            elif three_sum == target:
                return True

    print(count)
    return False


# class TestThreeSum(unittest.TestCase):
#     def test_three_sum(self):
#         target = 1000000008
#         arr = [1,2,3,4,1000000000]
#         self.assertTrue(three_sum(target,arr))
#
#
# if __name__ == '__main__':
#     unittest.main()


arr = [1, 2, 3, 999999999, 1000000000]
target = 2000000003
result = three_sum(target, arr)
print(result)
