import sympy as sp
import numpy as np
def newton_method(f_expr, x0, epsilon, max_iter=1000):
    x = sp.symbols('x')
    f = sp.lambdify(x, f_expr, 'numpy')
    df_expr = sp.diff(f_expr, x)
    df = sp.lambdify(x, df_expr, 'numpy')
    x_n = x0
    for i in range(max_iter):
        f_xn = f(x_n)
        df_xn = df(x_n)
        if df_xn == 0:
            #print("在 x = {} 处导数为零，无法继续迭代。".format(x_n))
            return None
        x_new = x_n - f_xn / df_xn
        if abs(x_new - x_n) < epsilon:
            #print("经过 {} 次迭代，找到根：x = {}".format(i+1, x_new))
            return x_new
        x_n = x_new
    #print("超过最大迭代次数，未能收敛。")
    return None


x = sp.symbols('x')
f_expr = x**3/3 - x  # 定义函数 f(x)

epsilon = 1e-7  # 容许误差
# val_x0_l = -1.001
# val_x0_g = -0.7745967

val_x0_g = 1-epsilon
val_x0_l = 0.7746
array1 = np.arange(val_x0_l, val_x0_g, 0.001)

result1 = [newton_method(f_expr, x0, epsilon) for x0 in array1]

rounded_array1 = np.round(result1, 5)

# 检查所有舍入后的值是否相等
all_equal1 = np.all(rounded_array1 == rounded_array1[0])


while(abs(val_x0_g - val_x0_l) > epsilon):
    x0 = (val_x0_g + val_x0_l) / 2
    root0 = newton_method(f_expr, x0, epsilon)
    if root0>0:
        val_x0_l = x0
    else:
        val_x0_g = x0
print(val_x0_l, val_x0_g)
print(all_equal1, rounded_array1[0])
