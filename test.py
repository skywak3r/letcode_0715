import math
import numpy as np

exp = math.exp
log = math.log

def sigmoid(x):
    return 1/(1 + exp(-x))

f = lambda x: x**2 - 2*x + 1

#数据
x = np.arange(-2,2,0.01)

a = -1
b = -1
c = -1
ff = lambda x: 4 *x - 2
learning_rate = 0.01
iterations = 300
count = 0
for i in range(iterations):
    x0 = x - ff(x) * learning_rate
    if abs(sum(f(x) - f(0))) < 0.01:
        break
    x = x0
    count += 1
    print(count)
# print(x)
print(f(x))

#模型参数初始化
w = 0
b = 0

#超参
learning_rate = 0.05 #学习率
iterations = 300 #迭代轮数

# for k in range(iterations):
#     dl_dw = 0
#     dl_db = 0
#     logL = 0
#
#     #对所有样本，计算参数的更新梯度
#     for i in range(len(x)):
#         y_pred_i = sigmoid(w*x[i]+b)
#         dl_dw += (y[i]-y_pred_i) * x[i]
#         dl_db += (y[i]-y_pred_i) * 1
#         logL += (y[i]*log(y_pred_i) + (1-y[i])*log(1-y_pred_i))
#     #更新模型参数
#     w += learning_rate * dl_dw
#     b += learning_rate * dl_db
#
# print("w={}, b={}".format(w, b))