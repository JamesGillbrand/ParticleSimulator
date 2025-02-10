from points import Point, Swarm


def gravity(particle: Point, points: list[Point]) -> Point:
    fx, fy = (0, 0)  # Initial forces
    G: float = 6.67 * (10 ** -11)  # Gravitational Constant
    t: float = 500  # Time between calculations/jumps

    # Iterate through points adding up gravitational force
    for point in points:
        if point != particle:
            r = particle.distance(point)
            dir_x, dir_y = particle.direction(point)

            fx += ((G * particle.mass * point.mass) / (r ** 2)) * dir_x
            fy += ((G * particle.mass * point.mass) / (r ** 2)) * dir_y

    vx = fx * t + particle.vx
    vy = fy * t + particle.vy

    fx = fx + 0.1 * particle.fx
    fy = fy + 0.1 * particle.fy

    x = vx * t + 0.5 * (fx * (t ** 2)) + particle.x
    y = vy * t + 0.5 * (fy * (t ** 2)) + particle.y

    new_point = Point((x, y), (vx, vy), (fx, fy))
    return new_point
