import math

def f(x):
    return math.exp(x) - 3 * x ** 2

def f_prime(x):
    return math.exp(x) - 6 * x

def newton_method(x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        if fpx == 0:
            print("导数为零，无法继续迭代。")
            return None
        x_new = x - fx / fpx
        print(f"第 {i+1} 次迭代，x = {x_new}")
        if abs(x_new - x) < tol:
            print(f"迭代收敛，根为：{x_new}")
            return x_new
        x = x_new
    print("超过最大迭代次数，未找到根。")
    return None

# 初始值
x0 = 3.5
# 调用牛顿迭代法
newton_method(x0)
