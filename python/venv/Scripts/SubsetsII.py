class Solution1:
    def subsetsWithDup(self, nums):
        map = {}
        for i in nums:
            map[i] = map.get(i, 0) + 1
        res = [[]]
        for k in map.keys():
            l = len(res)
            for n in range(l):
                for v in range(map[k]):
                    res.append(res[n] + [k] * (v + 1))
        return res

# standard answer from leetcode
class Solution2:
    def subsetsWithDup(self, nums):
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])
        return res

aSolution = Solution1()
print(aSolution.subsetsWithDup([1, 1, 2]))

aSolution = Solution2()
print(aSolution.subsetsWithDup([1, 2, 2]))

