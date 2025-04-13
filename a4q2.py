from scipy.optimize import linprog

# Objective function coefficients (cost per unit)
c = [45, 40, 85, 65]  # Minimize cost

# Inequality constraints (left-hand side matrix)
# Each row is a nutrient: protein, fat, carbohydrates
A = [
    [-3, -4, -8, -6],  # Proteins
    [-2, -2, -7, -5],  # Fats
    [-6, -4, -7, -4]   # Carbohydrates
]

# Right-hand side (negative because we convert ≥ to ≤ by multiplying by -1)
b = [-800, -200, -700]

# Bounds for each variable (no negative quantity of food)
x_bounds = [(0, None) for _ in range(4)]

# Solve using linprog
res = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

# Display result
if res.success:
    print("Optimal solution found:")
    for i, val in enumerate(res.x, start=1):
        print(f"Food type {i}: {val:.2f} units")
    print(f"Minimum total cost: {res.fun:.2f} BDT")
else:
    print("No optimal solution found.")