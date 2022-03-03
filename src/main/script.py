import pygame
import consts
from extob import Extob
from consts import AU

pygame.init()

WIDTH, HEIGHT = consts.WIDTH, consts.HEIGHT
WIND = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

pygame_icon = pygame.image.load('../assets/earth_icon512.png')
pygame.display.set_icon(pygame_icon)

BAR_WIDTH = consts.BAR_WIDTH
rect = pygame.Rect((WIDTH - BAR_WIDTH, 0), (BAR_WIDTH, HEIGHT))
GRAY = (178, 178, 178)

LScale = 0.5


def main():
    isRunning = True
    clock = pygame.time.Clock()

    sun = Extob(0, 0, 30 * LScale, consts.YELLOW, consts.SUN_MASS, "Sun", True)
    earth = Extob(-1 * AU, 0, 13 * LScale, consts.BLUE, consts.EARTH_MASS, "Earth")
    mars = Extob(-1.524 * AU, 0, 10 * LScale, consts.RED, consts.MARS_MASS, "Mars")
    venus = Extob(0.723 * AU, 0, 12 * LScale, consts.VWHITE, consts.VENUS_MASS, "Venus")
    mercury = Extob(0.387 * AU, 0, 7 * LScale, consts.DGRAY, consts.MERC_MASS, "Mercury")
    jupyter = Extob(5.204 * AU, 0, 16 * LScale, consts.BROWN, consts.JUPT_MASS, "Jupyter")
    harley_comet = Extob(5.87 * AU, 0, 6, consts.BLUE, consts.HARL_MASS, "Harley")

    # km/s * 1000 = m/s
    earth.y_vel = 29.783 * 1000
    mars.y_vel = 24.077 * 1000
    venus.y_vel = -35.02 * 1000
    mercury.y_vel = -47.4 * 1000
    jupyter.y_vel = -13.07 * 1000
    harley_comet.y_vel = -7823.2  # m/s

    space_bodies = [sun, mercury, venus, earth, mars, jupyter, harley_comet]

    while isRunning:
        clock.tick(60)
        WIND.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

        pygame.draw.rect(WIND, GRAY, rect)
        for ind, body in enumerate(space_bodies):
            body.update_position(space_bodies)
            body.draw(WIND)
            body.draw_stat(WIND, ind)

        pygame.display.update()
    pygame.quit()


main()
