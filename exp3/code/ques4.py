import mpmath
import matplotlib.pyplot as plt
import csv

def hilbert_matrix_mpmath(n):
    """生成高精度的 Hilbert 矩阵"""
    return mpmath.matrix([[1 / mpmath.mpf(i + j + 1) for j in range(n)] for i in range(n)])

def solve_and_error_mpmath(n):
    """解线性方程组并计算误差"""
    x_true = mpmath.matrix([1] * n)
    H_n = hilbert_matrix_mpmath(n)
    b = H_n * x_true

    # 解线性方程组
    x_hat = mpmath.lu_solve(H_n, b)

    # 计算误差和残差
    error_x = mpmath.norm(x_true - x_hat, p=mpmath.inf)
    residual = mpmath.norm(b - H_n * x_hat, p=mpmath.inf)

    return float(error_x), float(residual)

def plot_errors(n_values, errors_x):
    """绘制误差曲线（对数坐标）"""
    plt.figure()
    plt.plot(n_values, errors_x, label='Error in x', marker='o')
    plt.yscale('log')  # 设置纵坐标为对数坐标
    plt.xlabel('n')
    plt.ylabel('Log Scale Norm')
    plt.title('Log Scale Error in x for Hilbert Matrix')
    plt.xticks(ticks=n_values)
    plt.grid(True, which="both", linestyle='--')
    plt.legend()
    plt.show()

def plot_residuals(n_values, residuals):
    """绘制残差曲线（线性坐标）"""
    plt.figure()
    plt.plot(n_values, residuals, label='Residual norm', marker='x')
    plt.xlabel('n')
    plt.ylabel('Norm')
    plt.title('Residual Norm for Hilbert Matrix (Linear Scale)')
    plt.xticks(ticks=n_values)
    plt.grid(True, linestyle='--')
    plt.legend()
    plt.show()

# 设置高精度
mpmath.mp.dps = 50  # 默认 50 位小数精度

# 计算误差和残差
errors_x = []
residuals = []
n_values = range(1, 21)

for n in n_values:
    error_x, residual = solve_and_error_mpmath(n)
    errors_x.append(error_x)
    residuals.append(residual)

# 分别绘图
plot_errors(n_values, errors_x)
plot_residuals(n_values, residuals)
