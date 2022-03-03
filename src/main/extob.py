import math
import pygame.draw
import consts
from consts import BAR_WIDTH


class Extob:
    AU = consts.AU
    G = consts.G
    SCALE = consts.SCALE
    TIMESTEP = consts.TIMESTEP
    OFFSET = -100

    def __init__(self, x, y, radius, color, mass, name, isSun=False, ):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.isSun = isSun
        self.name = name

        self.orbit = []
        self.dist_to_sun = 0
        self.x_vel = 0
        self.y_vel = 0

    def draw(self, window):

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + consts.WIDTH / 2 + self.OFFSET
                y = y * self.SCALE + consts.HEIGHT / 2
                updated_points.append((x, y))
            pygame.draw.lines(window, self.color, False, updated_points, 1)

        x = self.x * self.SCALE + consts.WIDTH / 2 + self.OFFSET
        y = self.y * self.SCALE + consts.HEIGHT / 2

        pygame.draw.circle(window, self.color, (x, y), self.radius)

    def draw_stat(self, window, ind):
        if not self.isSun:
            FONT = pygame.font.SysFont("comicsans", 16)
            distance_text = FONT.render(f"{self.name}: {round(self.dist_to_sun / 1000000000, 1)}e6 km", True, (255, 0, 0))
            window.blit(distance_text, (consts.WIDTH - BAR_WIDTH + 10, 20 * (2 + ind)))

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        dist_x = other_x - self.x
        dist_y = other_y - self.y
        dist = math.sqrt(dist_x ** 2 + dist_y ** 2)

        if other.isSun:
            self.dist_to_sun = dist

        force = self.G * self.mass * other.mass / dist ** 2
        theta = math.atan2(dist_y, dist_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, bodies):
        total_fx = total_fy = 0
        for body in bodies:
            if self == body:
                continue
            fx, fy = self.attraction(body)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP  # a = F/m, v = a*t
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        # self.upd_x(self.x_vel * self.TIMESTEP)
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))
