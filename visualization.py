import matplotlib.pyplot as plt
import numpy as np
from points import Point, Swarm
from functions import gravity
from matplotlib.animation import FuncAnimation

# Create initial swarm
particles = [Point((np.random.uniform(-10, 10), np.random.uniform(-10, 10)),
                   (0, 0),
                   (0, 0), 100) for _ in range(200)]

swarm = Swarm(particles)

# Setup plot
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
scat = ax.scatter([], [], s=100)

# Animation update function
def update(frame):
    # Update swarm positions
    swarm.update(gravity)

    # Get updated positions for plotting
    x_data = [point.x for point in swarm.points]
    y_data = [point.y for point in swarm.points]

    # Update scatter plot
    scat.set_offsets(np.c_[x_data, y_data])
    return scat,


# Create animation
ani = FuncAnimation(fig, update, frames=500, interval=50, blit=True)

plt.show()

print("finished")
