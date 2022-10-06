import math


class Solution:
    def calc_weight(self, x, y):
        def sigmod(x):
            return 1 / (1 + math.exp(-x))

        w = 0
        epochs = 10
        lr = 0.01
        for epoch in range(epochs):
            y_p = [sigmod(xx * w) for xx in x]
            dw = sum([(y[i]-y_p[i]) * x[i] for i in range(len(x))])

            # print(dw)
            w += lr * dw
            # print(y_p)

        return round(w, 5)
        # write code here

if __name__ == "__main__":
    a = Solution()
    x,y = [-3,1,2,1,-2,-6,3,1,-2,-4],[0, 1, 1, 1, 0, 0, 1, 1, 0, 0]
    print(a.calc_weight(x,y))