from points import Point, Swarm
import numpy as np

from points import Point
import numpy as np


from points import Point
import numpy as np

def gravity(particle: Point, points: list[Point]) -> Point:
    fx, fy = 0, 0  # Initialize forces
    G = 6.67e-11   # Gravitational Constant
    t = 1        # Small time step for stability

    new_x, new_y = particle.x, particle.y
    new_vx, new_vy = particle.vx, particle.vy
    new_mass = particle.mass
    new_radius = particle.radius

    to_remove = []  # Track particles to remove

    for point in points:
        if point == particle:
            continue  # Skip self

        r = particle.distance(point)

        # **COLLISION HANDLING**: Merge only if overlapping **beyond a small threshold**
        if r < (particle.radius + point.radius) * 0.1:  # Allow a buffer
            to_remove.append(point)

            # New mass (mass conservation)
            new_mass += point.mass

            # Center of mass approximation
            new_x = (particle.x * particle.mass + point.x * point.mass) / new_mass
            new_y = (particle.y * particle.mass + point.y * point.mass) / new_mass

            # Momentum conservation for velocity
            new_vx = (particle.vx * particle.mass + point.vx * point.mass) / new_mass
            new_vy = (particle.vy * particle.mass + point.vy * point.mass) / new_mass

            # Radius growth (volume conservation)
            new_radius = ((particle.radius ** 3 + point.radius ** 3) ** (1/3))

        else:
            # **GRAVITY CALCULATION**
            dir_x, dir_y = particle.direction(point)
            force = (G * particle.mass * point.mass) / (r ** 2 + 1e-6)  # Avoid division by zero
            fx += force * dir_x
            fy += force * dir_y

    # **UPDATE VELOCITY USING FORCE (Newton's Second Law)**
    ax = fx / new_mass
    ay = fy / new_mass
    new_vx += ax * t
    new_vy += ay * t

    # **UPDATE POSITION USING VELOCITY**
    new_x += new_vx * t
    new_y += new_vy * t

    # **REMOVE MERGED PARTICLES** (Handled in `Swarm.update()`)
    for p in to_remove:
        points.remove(p)

    # **RETURN NEW PARTICLE STATE**
    return Point((new_x, new_y), (new_vx, new_vy), (fx, fy), new_mass, new_radius)
