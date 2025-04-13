import numpy as np

def simplex(c, A, b):
    m, n = A.shape

    # Build initial tableau
    tableau = np.zeros((m+1, n+m+1))
    tableau[:-1, :n] = A
    tableau[:-1, n:n+m] = np.eye(m)
    tableau[:-1, -1] = b
    tableau[-1, :n] = -c

    while True:
        # Step 1: Find entering variable (most negative coefficient in bottom row)
        pivot_col = np.argmin(tableau[-1, :-1])
        if tableau[-1, pivot_col] >= 0:
            break  # Optimal reached

        # Step 2: Find leaving variable (minimum ratio test)
        ratios = []
        for i in range(m):
            if tableau[i, pivot_col] > 0:
                ratios.append(tableau[i, -1] / tableau[i, pivot_col])
            else:
                ratios.append(np.inf)
        pivot_row = np.argmin(ratios)
        if all(np.isinf(ratios)):
            raise Exception("Unbounded solution")

        # Step 3: Pivot operation
        pivot_val = tableau[pivot_row, pivot_col]
        tableau[pivot_row] /= pivot_val
        for i in range(m+1):
            if i != pivot_row:
                tableau[i] -= tableau[i, pivot_col] * tableau[pivot_row]

    # Extract solution
    x = np.zeros(n)
    for i in range(n):
        col = tableau[:-1, i]
        if list(col).count(1) == 1 and list(col).count(0) == m-1:
            x[i] = tableau[np.where(col == 1)[0][0], -1]

    max_val = tableau[-1, -1]
    return x, max_val

# Problem data
c = np.array([12, 15, 14])  # profit per ton
A = np.array([
    [1, 1, 1],              # total fuel
    [0.02, 0.04, 0.03],     # phosphorous
    [3, 2, 5]               # ash
])
b = np.array([100, 3, 300])

# Run simplex
solution, max_profit = simplex(c, A, b)

# Display result
for i, val in enumerate(solution, start=1):
    print(f"Coal Grade {chr(64+i)}: {val:.2f} tons")
print(f"Maximum Profit: {max_profit:.2f} BDT")