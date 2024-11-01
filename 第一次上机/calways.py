import numpy as np
import sys
epsilon = sys.float_info.epsilon
# 方式1 f(x) = ln(x+1)
# 泰勒展开为n=1∑∞​(−1)n+1nxn​
def func1(x,iter_num = 11):
    x = np.double(x)  # 确保x是双精度浮点数
    y = np.double(0.0)  # 初始化为双精度浮点数
    for i in range(1,iter_num+1):
        y += (-1)**(i+1)*x**i/np.double(i)      
    return y

# 方式2 f(x) = -ln(1+x） 
# 泰勒展开为 -x +x^2/2 -x^3/3 +x^4/4 -x^5/5 +x^6/6 -x^7/7 +x^8/8 -x^9/9 +x^10/10
def func2(x, iter_num=11):
    x = np.double(x)  # 确保x是双精度浮点数
    y = np.double(0.0)  # 初始化为双精度浮点数
    for i in range(1, iter_num + 1):
        y += (-1.0)**i * x**i / np.double(i)  # 确保除法中的i是双精度
    return y
# 方式3 f(x) = ln((1+x)/(1-x))
def func3(x, iter_num=11):
    x = np.double(x)  # 确保x是双精度浮点数
    y = np.double(0.0)  # 初始化为双精度浮点数
    for i in range(1, iter_num + 1):
        y += np.double(2.0) * x**(2*i-1) / np.double(2*i-1)  # 保证分母是双精度
    return y

def fun2_1(x):
    x = np.double(x)  # 确保x是双精度浮点数
    y = np.double(0.0)  # 初始化为双精度浮点数
    i=0
    while True:
        i+=1
        y_ori = y
        y += (-1.0)**(i)*x**i/np.double(i)
        if  abs(y-y_ori)<epsilon:
            break
    return y ,i

def fun3_1(x):
    x = np.double(x)  # 确保x是双精度浮点数
    y = np.double(0.0)  # 初始化为双精度浮点数
    i=0
    while True:
        i+=1
        y_ori = y
        y += np.double(2.0) * x**(2*i-1) / np.double(2*i-1)  # 保证分母是双精度
        if  abs(y-y_ori)<epsilon:
            break
    return y ,i
