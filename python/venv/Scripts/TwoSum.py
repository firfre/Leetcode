# example solution for Leetcode

class Solution(object):
    def twoSum(self, nums, target):
        a ={}
        for i, num in enumerate(nums):
            if target-num in a:
                return [a[target - num], i]
            else:
                a[num] = i

def main():
    aSolution = Solution()
    print(aSolution.twoSum([2, 5, 7, 11], 12))

main()