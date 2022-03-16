from bisect import bisect_left,bisect_right
import bisect
class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        n1 = len(nums)
        presum = [0 for _ in range(n1 + 1)]
        for i in range(n1):
            presum[i + 1] = presum[i] + nums[i]

        res = 0
        preWindow = []
        for i, p in enumerate(presum):
            print(f"p:{p}")
            L = bisect_left(preWindow, p - upper)
            print(f"L:{L}")
            R = bisect_right(preWindow, p - lower)
            res += (R - L)
            print(f"R:{R}")
            bisect.insort(preWindow, p)
            print(preWindow)

        return res




if __name__ =="__main__":
    a = Solution()
    # nums = [0,1]
    # k = 0
    nums =[-2,5,-1]
    nums.sort()
    print(nums)
    # a.countRangeSum(nums,lo,hi)
    # print(a.solve(nums,k))
    # a = range(2,3)
    # print([num for num in a])
