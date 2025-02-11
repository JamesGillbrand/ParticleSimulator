import matplotlib.pyplot as plt
import numpy as np
from points import Point, Swarm
from functions import gravity
from matplotlib.animation import FuncAnimation

# Create initial swarm
particles = [
    Point(
        pos=(np.random.uniform(-10, 10), np.random.uniform(-10, 10)),
        vel=(np.random.uniform(-.1, .1), np.random.uniform(-.1, .1)),  # Add slight initial velocity
        m=np.random.normal(20, 10),  # Give reasonable mass
        r=np.random.uniform(.5, 2)  # Give varied sizes
    )
    for _ in range(1000)

]
particles.append(Point(pos=(0, 0), vel=(0, 0), m=100, r=5))

swarm = Swarm(particles)

# Setup plot
fig, ax = plt.subplots()
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
scat = ax.scatter([], [], s=100)

# Animation update function
def update(frame):
    # Update swarm positions
    swarm.update(gravity)

    # Get updated positions for plotting
    x_data = [point.x for point in swarm.points]
    y_data = [point.y for point in swarm.points]
    sizes = [point.radius * 20 for point in swarm.points]

    # Update scatter plot
    scat.set_offsets(np.c_[x_data, y_data])
    scat.set_sizes(sizes)

    return scat,


# Create animation
ani = FuncAnimation(fig, update, frames=500, interval=50, blit=True)

plt.show()

print("finished")
