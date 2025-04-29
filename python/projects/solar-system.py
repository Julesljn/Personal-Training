import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


def solarSystem(show=False):
    planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    radii = [0.383, 0.949, 1.0, 0.532, 11.21, 9.45, 4.01, 3.88]
    distances = [0.39, 0.72, 1.0, 1.52, 5.2, 9.58, 19.22, 30.05]

    if show:
        fig = plt.figure(figsize=(12, 12))
        ax = fig.add_subplot(111, projection='3d', )
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')

        sun = ax.scatter(0, 0, 0, color='yellow', s=500, label='sun')

        def update(frame):
            colors = ['yellow', 'orange', 'red', 'darkred']
            sun_color = random.choice(colors)
            
            sun_size = random.randint(400, 600)
            
            sun.set_facecolor(sun_color)
            sun.set_sizes([sun_size])
    
            return [sun]

        ani = FuncAnimation(fig, update, frames=100, interval=100, blit=True)

        # ax.set_axis_off()
        plt.show()






solarSystem(show=True)