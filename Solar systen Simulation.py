import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1600, 1000  
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (173, 216, 230)
BEIGE = (210, 180, 140)
LIGHT_PURPLE = (147, 112, 219)

FONT = pygame.font.SysFont("arial", 16)

class Planet:
    AU = 149.6e6 * 1000  # Astronomical Unit in meters
    G = 6.67428e-11  # Gravitational constant
    SCALE = 150 / AU  # Scale for visual representation
    TIMESTEP = 3600 * 24  # One day in seconds

    def __init__(self, distance_from_sun, radius, color, mass, orbital_velocity, name):
        self.x = distance_from_sun
        self.y = 0
        self.radius = radius
        self.color = color
        self.mass = mass
        self.orbit = []  # For drawing the orbit
        self.name = name  # Name of the planet

        # Set initial orbital velocity
        self.x_vel = 0
        self.y_vel = orbital_velocity  # Orbital velocity along the Y-axis
        self.sun = False  # Flag to identify the Sun

    def draw(self, win):
        # Convert the planet's coordinates into screen coordinates
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        # Draw the orbit path by connecting the stored orbit points
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                px, py = point
                px = px * self.SCALE + WIDTH / 2
                py = py * self.SCALE + HEIGHT / 2
                updated_points.append((px, py))
            pygame.draw.lines(win, self.color, False, updated_points, 2)

        # Draw the planet itself
        pygame.draw.circle(win, self.color, (x, y), self.radius)

        if not self.sun:
            # Render the planet name
            name_text = FONT.render(self.name, 1, WHITE)
            win.blit(name_text, (x - name_text.get_width()/2, y - name_text.get_height()/2))

    def attraction(self, other):
        # Calculate the gravitational attraction between this planet and another
        if other.sun:
            other_x, other_y = 0, 0  # Sun is at the center
            distance_x = other_x - self.x
            distance_y = other_y - self.y
            distance = math.sqrt(distance_x**2 + distance_y**2)

            # Ensure we don't divide by zero in case distance is zero
            if distance == 0:
                return 0, 0

            # Calculate the gravitational force
            force = self.G * self.mass * other.mass / distance**2
            theta = math.atan2(distance_y, distance_x)
            force_x = math.cos(theta) * force
            force_y = math.sin(theta) * force
            return force_x, force_y
        return 0, 0

    def update_position(self, planets):
        # Sum up all the forces acting on this planet
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            # Calculate the attraction force from other planets
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        # Update the velocity of the planet based on the forces acting on it
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        # Update the position of the planet
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP

        # Store the current position for drawing the orbit
        self.orbit.append((self.x, self.y))

        
        if len(self.orbit) > 1700:  
            self.orbit.pop(0)  

def draw_window(win, planets):
    win.fill((0, 0, 0))
    for planet in planets:
        planet.draw(win)
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 20, YELLOW, 1.98892 * 10**30, 0, "Sun")  # Sun at the center
    sun.sun = True

   
    mercury = Planet(0.4 * Planet.AU, 4, DARK_GREY, 3.30 * 10**23, 47.4 * 1000, "Mercury")
    venus = Planet(0.8 * Planet.AU, 6, WHITE, 4.8685 * 10**24, 35.02 * 1000, "Venus")
    earth = Planet(1.2 * Planet.AU, 7, BLUE, 5.9742 * 10**24, 29.783 * 1000, "Earth")
    mars = Planet(1.6 * Planet.AU, 6, RED, 6.39 * 10**23, 24.077 * 1000, "Mars")
    jupiter = Planet(2.4 * Planet.AU, 12, ORANGE, 1.898 * 10**27, 13.07 * 1000, "Jupiter")
    saturn = Planet(3.2 * Planet.AU, 10, BEIGE, 5.683 * 10**26, 9.69 * 1000, "Saturn")
    uranus = Planet(4.0 * Planet.AU, 8, LIGHT_BLUE, 8.681 * 10**25, 6.81 * 1000, "Uranus")
    neptune = Planet(4.8 * Planet.AU, 7, LIGHT_PURPLE, 1.024 * 10**26, 5.43 * 1000, "Neptune")

    planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    while run:
        clock.tick(60)
        draw_window(WIN, planets)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)

    pygame.quit()

if __name__ == "__main__":
    main()
