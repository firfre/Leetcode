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


def subsetsWithDup(nums, res):
    if len(nums) == 0:
        return res

    if [nums[0]] in res:
        for i in range(len(res)):
            if nums[0] in res[i]:
                res.append(res[i] + [nums[0]])
    elif [nums[0]] not in res:
        for i in range(len(res)):
            res.append(res[i] + [nums[0]])

    return subsetsWithDup(nums[1 : ], res)

# aSolution = Solution1()
# print(aSolution.subsetsWithDup([1, 1, 2]))
#
# aSolution = Solution2()
# print(aSolution.subsetsWithDup([1, 2, 2]))

print(subsetsWithDup([1, 1, 2], [[]]))
