import math


def task_a(x, k):
    if k < 1:
        raise ValueError("k має бути >= 1")
    return (x ** k) / k
def task_b(n):
    if n < 1:
        return 0
    p = 1
    for i in range(1, n + 1):
        p *= 1 / (i + math.factorial(1))
    return p
def task_c(n):
    if n <= 0:
        return 0
    if n == 1:
        return 2
    if n == 2:
        return 1
    d_prev2 = 2
    d_prev1 = 1
    d_curr = 0
    for _ in range(3, n + 1):
        d_curr = 2 * d_prev1 - 3 * d_prev2
        d_prev2 = d_prev1
        d_prev1 = d_curr

    return d_curr
def task_d(n):
    if n < 1:
        return 0
    a = [0] * (n + 1)
    if n >= 1:
        a[1] = 0
    if n >= 2:
        a[2] = 1
    for k in range(3, n + 1):
        a[k] = a[k - 1] + k * a[k - 2]
    s = 0
    for k in range(1, n + 1):
        s += (2 ** k) * a[k]
    return s
def task_e(x, epsilon):
    if epsilon <= 0:
        raise ValueError("Точність epsilon має бути > 0")
    term = x
    sin_x = term
    n = 1
    while abs(term) > epsilon:
        n += 1
        term = term * (-x ** 2) / ((2 * n - 2) * (2 * n - 1))
        sin_x += term
    return sin_x
if __name__ == "__main__":
    print("--- Завдання a ---")
    x_val = 2.0
    k_val = 3
    print(f"x_{k_val} для x={x_val}: {task_a(x_val, k_val)}")
    print("\n--- Завдання b ---")
    n_val_b = 5
    print(f"P_{n_val_b}: {task_b(n_val_b)}")
    print("\n--- Завдання c ---")
    for n in range(1, 6):
        print(f"Визначник D_{n}: {task_c(n)}")
    print("\n--- Завдання d ---")
    n_val_d = 4
    print(f"S_{n_val_d}: {task_d(n_val_d)}")
    print("\n--- Завдання e ---")
    x_val_e = math.pi / 4  # 45 градусів
    eps = 1e-6
    my_sin = task_e(x_val_e, eps)
    math_sin = math.sin(x_val_e)
    print(f"x = {x_val_e}")
    print(f"Точність eps = {eps}")
    print(f"Ряд Тейлора: {my_sin}")
    print(f"math.sin():  {math_sin}")
    print(f"Різниця:     {abs(my_sin - math_sin)}")