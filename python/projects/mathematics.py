import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def square_root(n):
    x = n / 2
    prev = 0

    while abs(x - prev) > 1e-6: # On continue jusqu'à ce que la différence soit minime /// 1e-6 = 0.000001
        prev = x
        x = 0.5 * (x + n / x)

    return x

# -----------------------------------

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

# -----------------------------------

def lcm(x, y):
    return abs(x * y) // gcd(x, y) # // → division entière (retourne un int, le résultat arrondi vers le bas)

# -----------------------------------

def points_in_circle(n_points, side_length=1.0, circle_radius=None, seed=None, show=True):
    if seed is not None:
        np.random.seed(seed)

    if circle_radius is None:
        circle_radius = side_length / 2

    center = np.array([side_length / 2, side_length / 2])
    points = np.random.rand(n_points, 2) * side_length

    inside = np.linalg.norm(points - center, axis=1) <= circle_radius
    count_inside = inside.sum()

    if show:
        fig, ax = plt.subplots()
        ax.scatter(points[:, 0], points[:, 1], s=10)
        ax.add_patch(patches.Rectangle( (0, 0), side_length, side_length, fill=False))
        ax.add_patch(patches.Circle(center, circle_radius, fill=False))
        ax.set_aspect('equal')
        ax.set_xlim(0, side_length)
        ax.set_ylim(0, side_length)
        ax.set_title(f'Points dans le cercle : {count_inside} / {n_points}')
        plt.show()

    return count_inside

# -----------------------------------







# print(square_root(242))
# print(gcd(252, 105))
# print(lcm(12, 18))
for i in range(1):
    print(points_in_circle(1000))