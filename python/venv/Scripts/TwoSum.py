class TwoSum(object):
    def twoSum(self, nums, target):
        a ={}
        for i, num in enumerate(nums):
            if target-num in a:
                return [a[target - num], i]
            else:
                a[num] = i

aTwoSum = TwoSum()
print(aTwoSum.twoSum([2, 5, 7, 11], 12))