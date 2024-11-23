import mpmath
import matplotlib.pyplot as plt
import math

def hilbert_matrix_mpmath(n):
    """生成高精度的 Hilbert 矩阵"""
    return mpmath.matrix([[1 / mpmath.mpf(i + j + 1) for j in range(n)] for i in range(n)])

def condition_number_mpmath(H):
    """计算矩阵 H 的高精度行范数条件数"""
    H_inv = mpmath.inverse(H)  # 使用 mpmath 计算逆矩阵
    norm_H = mpmath.norm(H, p=mpmath.inf)  # 计算无穷范数
    norm_H_inv = mpmath.norm(H_inv, p=mpmath.inf)  # 计算逆矩阵的无穷范数
    return norm_H * norm_H_inv

# 设置高精度
mpmath.mp.dps = 50  # 设置小数点后 50 位精度

# 计算条件数
condition_numbers = []
n_values = range(1, 21)
for n in n_values:
    H_n = hilbert_matrix_mpmath(n)
    cond_num = condition_number_mpmath(H_n)
    condition_numbers.append(cond_num)

# 绘图
plt.plot(n_values, [math.log10(float(result)) for result in condition_numbers], marker='o')
plt.xlabel('n')
plt.ylabel('log10(Condition Number)')
plt.title('Condition Number of Hilbert Matrix vs n (High Precision)')
plt.xticks(ticks=n_values)
plt.grid(True)

# 添加注释
for i in range(len(n_values)):
    n = n_values[i]
    y = math.log10(float(condition_numbers[i]))
    cond_num = condition_numbers[i]
    plt.annotate('{:.2e}'.format(float(cond_num)), xy=(n, y), xytext=(0, 20),
                 textcoords='offset points', ha='center', fontsize=8)

plt.show()
