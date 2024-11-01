import math

def f(x):
    return math.exp(2*x) - 1 - 2*x - 2*x**2

def df(x):
    return 2*math.exp(2*x) - 2 - 4*x

def newton_method(f, df, x0, tolerance=1e-10, max_iterations=100):
    xn = x0
    print(f"在第 {0} 次迭代后收敛到根：x = {xn},f(x) = {f(xn)}")
    for n in range(1, max_iterations + 1):
        fxn = f(xn)
        dfxn = df(xn)
        
        if dfxn == 0:
            print("导数为零，无法继续迭代。")
            return None 
        xn_next = xn - 3*fxn/dfxn
        print(f"在第 {n} 次迭代后收敛到根：x = {xn_next},f(x) = {f(xn_next)}")
        if abs(xn_next - xn) < tolerance:
            print(f"在第 {n} 次迭代后收敛到根：x = {xn_next},f(x) = {f(xn_next)}")
            return xn_next
        xn = xn_next
    print("超过最大迭代次数，未能收敛。")
    return None

# 选择初始值接近 x=0，例如 x0 = 0.1
root = newton_method(f, df, x0=0.5)
