import heapq
class Solution:
    def cuttingRope(self, n: int) -> int:
        factor = []
        def multiMax(nums):
            ans = 1
            for i in nums:
                ans *= -i
            return ans
        heapq.heappush(factor,-n)
        # heapq.heappush(factor,-4)
        src = 1
        # print(multiMax([3,4,5]))
        def split(nums):
            maxFac = -1 * heapq.heappop(nums)
            src1 = maxFac // 2
            src2 = maxFac - src1
            heapq.heappush(nums,-src1)
            heapq.heappush(nums,-src2)
            return nums
        # heapq.heappush(factor, -9)
        # print(split(factor))

        # test = [-3,-2,-2]
        # test1 = split(test)
        # print(f"test:{test}")
        # print(multiMax(test))
        if n <4:
            return n
        while True:
            factor = split(factor)
            tmp = multiMax(factor)
            if tmp > src:
                src = tmp
                continue
            break
            # print(src)
            # print(factor)
        # print(factor)
        return src









        # def dfs(count, row, col, used):
        #     # print(word[1])
        #
        #
        #     if (row < 0 or row > m or col < 0 or col > n or not used[row][col] and (board[row][col] != word[count-1])):
        #         print(word[count])
        #
        #         return 0
        #     print(word[count])
        #     used[row][col] = True
        #     up = dfs(count + 1, row - 1, col, used)
        #     down = dfs(count + 1, row + 1, col, used)
        #     left = dfs(count + 1, row, col - 1, used)
        #     right = dfs(count + 1, row - 1, col + 1, used)
        #     count = 1 + up + down + left + right
        #     used[row][col] = False
        #
        #     return count
        # for i in range(m):
        #     for j in range(n):
        #         ans = max(count,dfs(count,i,j,used))
        # # dfs(count, 0, 0, used)
        # return count == len(word)

if __name__ == "__main__":
    a = Solution()
    b = 8
    print(a.cuttingRope(b))

