import random
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'Function time : {end - start:.4f}')
    return wrapper

# -----------------------------------

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
# Pas opti mémoire

@timer
def dice(try_n):
    target_ok = 0
    groupes = {} # Dictionnaire clé => valeur
    for i in range(try_n):
        sum_dice = random.randint(1, 6) + random.randint(1, 6)
        if sum_dice not in groupes: # Si la clé existe pas, on la crée
            groupes[sum_dice] = []
        groupes[sum_dice].append(sum_dice)
    for key, value in sorted(groupes.items()):
        print(f'{key} => {round((len(value) / try_n) * 100, 2)}')

# -----------------------------------

@timer
def dice_all_sums(try_n):
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(try_n):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        sum_dice = dice_1 + dice_2
        sums_count[sum_dice] += 1  # Incrémenter le compteur pour la somme obtenue

    for total, count in sorted(sums_count.items()):
        pourcentage = (count / try_n) * 100
        print(f"Somme {total} : {pourcentage:.2f}%")

# -----------------------------------
# Extremement Opti (NumPy) (GPT)

@timer
def dice_numpy(try_n):
    dice_rolls = np.random.randint(1, 7, size=(try_n, 2))
    sums = np.sum(dice_rolls, axis=1)
    
    counts = {i: 0 for i in range(2, 13)}
    unique, counts_arr = np.unique(sums, return_counts=True)
    
    for val, count in zip(unique, counts_arr):
        counts[val] = count

    for total in range(2, 13):
        pourcentage = (counts[total] / try_n) * 100
        print(f"Somme {total} : {pourcentage:.2f}%")

# -----------------------------------

def random_normal(size, average=0.0, scale=1.0, show=False):
    normal_list = (np.random.normal(loc=average, scale=scale, size=size)).tolist()
    if show:
        plt.hist(normal_list, bins=50, density=True)
        plt.axvline(x=0, color='r', linestyle='-')
        plt.show()
    return print(f'Taille : {size}\nMoyenne : {np.mean(normal_list)} - {average}\nÉcart-type : {np.std(normal_list)} - {scale}')

# -----------------------------------












# print(square_root(242))
# print(gcd(252, 105))
# print(lcm(12, 18))
# print(points_in_circle(200))
# dice(100_000_000)
# dice_all_sums(100_000_000)
# dice_numpy(500_000_000)
# random_normal(100_000, show=True)
print(knn())
