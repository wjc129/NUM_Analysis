import sympy as sp

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

val_x0_l = 0.0
val_x0_g = 1.0

epsilon = 1e-7  # 容许误差
root1 = newton_method(f_expr, val_x0_l, epsilon)
root2 = newton_method(f_expr, val_x0_g, epsilon)
root3 = newton_method(f_expr, 0.75, epsilon)

while(abs(val_x0_g - val_x0_l) > epsilon):
    x0 = (val_x0_g + val_x0_l) / 2
    root0 = newton_method(f_expr, x0, epsilon)
    if root0 != None and abs(root0 - 0) < epsilon:
        val_x0_l = x0
    else:
        val_x0_g = x0

print('val_x0_l:', val_x0_l)
print('val_x1_g:', val_x0_g)