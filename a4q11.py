import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

# Define feasibility check
def is_feasible(x1, x2):
    return (
        x1 + 2*x2 <= 10 and
        x1 + x2 <= 6 and
        x1 - x2 <= 2 and
        x1 - 2*x2 <= 1 and
        x1 >= 0 and x2 >= 0
    )

# Constraint boundary lines
lines = [
    (lambda x1: (10 - x1)/2, 'x1 + 2x2 ≤ 10', 'orange'),
    (lambda x1: 6 - x1, 'x1 + x2 ≤ 6', 'brown'),
    (lambda x1: x1 - 2, 'x1 - x2 ≤ 2', 'crimson'),
    (lambda x1: (x1 - 1)/2, 'x1 - 2x2 ≤ 1', 'magenta')
]

# Find intersection points
intersections = []
for (i, (f1, _, _)), (j, (f2, _, _)) in combinations(enumerate(lines), 2):
    for x in np.linspace(0, 10, 1000):
        y1 = f1(x)
        y2 = f2(x)
        if abs(y1 - y2) < 0.01:
            x1, x2 = x, y1
            if is_feasible(x1, x2):
                intersections.append((x1, x2))
                break

# Check feasible intersections on axes
for y in np.linspace(0, 10, 1000):
    x_vals = [10 - 2*y, 6 - y, 2 + y, 1 + 2*y]
    for x in x_vals:
        if x >= 0 and is_feasible(x, y):
            intersections.append((x, y))

# Remove duplicates
intersections = np.unique(np.round(intersections, 4), axis=0)

# Evaluate objective function
Z = [2*x + y for x, y in intersections]
max_Z = max(Z)
opt_point = intersections[np.argmax(Z)]

# Plot
x_vals = np.linspace(0, 10, 400)
plt.figure(figsize=(10, 8))

# Plot constraint lines and arrows
for f, label, color in lines:
    y_vals = f(x_vals)
    plt.plot(x_vals, y_vals, label=label, color=color)
    # Draw arrows on each line
    idx = 150  # sample point for arrow
    plt.arrow(x_vals[idx], y_vals[idx], 0.5, f(x_vals[idx] + 0.5) - y_vals[idx],
              head_width=0.2, head_length=0.2, fc=color, ec=color)

# Feasible region shading
X1, X2 = np.meshgrid(x_vals, x_vals)
feasible = np.array([
    is_feasible(x, y) for x, y in zip(X1.ravel(), X2.ravel())
])
plt.contourf(X1, X2, feasible.reshape(X1.shape), levels=1, colors=['#ccf2ff'], alpha=0.5)

# Plot feasible points
for pt in intersections:
    plt.plot(*pt, 'go')

# Optimal point
plt.plot(*opt_point, 'ro', label=f'Optimal Point: ({opt_point[0]:.2f}, {opt_point[1]:.2f}), Z = {max_Z:.2f}')

# Plot settings
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('Graphical Method for LPP with Arrows')
plt.legend()
plt.grid(True)
plt.show()

# Output
print(f"Optimal solution: x1 = {opt_point[0]:.4f}, x2 = {opt_point[1]:.4f}")
print(f"Maximum value of Z = {max_Z:.4f}")