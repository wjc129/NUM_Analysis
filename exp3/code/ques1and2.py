import numpy as np
import matplotlib.pyplot as plt
import math
def hilbert_matrix(n):
    """生成 Hilbert 矩阵 H_n"""
    H = np.fromfunction(lambda i, j: 1.0 / (i + j + 1), (n, n))
    return H
def condition_number(H):
    """计算矩阵 H 的行范数条件数"""
    H_inv = np.linalg.inv(H)  # 计算 H 的逆矩阵
    norm_H = np.linalg.norm(H, ord=np.inf)
    norm_H_inv = np.linalg.norm(H_inv, ord=np.inf)
    return norm_H * norm_H_inv


def matrix_infinity_norm(H):
    """计算矩阵 H 的无穷范数，即每行元素绝对值之和的最大值"""
    # 计算每行元素绝对值之和
    row_sums = np.sum(np.abs(H), axis=1)
    # 取每行之和的最大值
    return np.max(row_sums)

n = 5  # 示例：生成一个 5x5 的 Hilbert 矩阵
H = hilbert_matrix(n)
infinity_norm_H = matrix_infinity_norm(H)
print("Hilbert 矩阵:\n", H)
print("Hilbert 矩阵的无穷范数:", infinity_norm_H)
condition_num = condition_number(H)
print(f"Condition number: {condition_num}")

