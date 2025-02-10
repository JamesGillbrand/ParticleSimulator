import math


class Point:
    """
    Point class for each particle
    """
    x: float
    y: float
    vx: float
    vy: float
    fx: float
    fy: float
    mass: float

    def __init__(self, pos: tuple[float, float],
                 vel: tuple[float, float] = (0, 0),
                 f: tuple[float, float] = (0, 0),
                 m: float = 1) -> None:

        self.x, self.y = pos
        self.vx, self.vy = vel
        self.fx, self.fy = f
        self.mass = m

    def distance(self, point: 'Point') -> float:
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

    def direction(self, point: 'Point') -> tuple[float, float]:
        if self == point:
            return 0, 0

        dir_x = point.x - self.x
        dir_y = point.y - self.y

        norm = math.sqrt(dir_x ** 2 + dir_y ** 2)

        dir_x = dir_x / norm
        dir_y = dir_y / norm

        return dir_x, dir_y

    def __eq__(self, other: 'Point') -> bool:
        if (self.x == other.x) & (self.y == other.y):
            return True
        return False

    def __str__(self):
        return f"Point ({self.x, self.y})"


class Swarm:
    """
    Collection of points
    """
    points: list[Point]

    def __init__(self, list: list[Point]) -> None:
        self.points = list

    def __str__(self):
        ans = "Swarm of: \n"
        for point in self.points:
            ans += str(point)
            ans += "\n"
        return ans

    def update(self, func) -> None:
        new_points: list[Point] = [Point((0, 0))]

        for point in self.points:
            moved_point = func(point, self.points)
            new_points.append(moved_point)

        self.points = new_points[1:]
        print("updated")


def gravity(particle: Point, points: list[Point]) -> Point:
    fx, fy = (0, 0)  # Initial forces
    G: float = 6.67 * (10 ** -11)  # Gravitational Constant
    t: float = 1000  # Time between calculations/jumps

    # Iterate through points adding up gravitational force
    for point in points:
        if point != particle:
            r = particle.distance(point)
            dir_x, dir_y = particle.direction(point)

            fx += ((G * particle.mass * point.mass) / (r ** 2)) * dir_x
            fy += (G / (r ** 2)) * dir_y

    vx = fx * t + particle.vx
    vy = fy * t + particle.vy

    fx = fx + particle.fx
    fy = fy + particle.fy

    x = vx * t + 0.5 * (fx * (t ** 2)) + particle.x
    y = vy * t + 0.5 * (fy * (t ** 2)) + particle.y

    new_point = Point((x, y), (vx, vy), (fx, fy))
    return new_point

