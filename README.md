# Solar System Simulation

This project is a Python-based solar system orbit simulation built using the Pygame library. It models the gravitational interactions and orbital motions of the Sun and planets in a simplified 2D space.

## Features
- Realistic scaling of distances and masses (scaled down for visualization purposes).
- Simulates the gravitational forces and orbital paths of planets.
- Displays the planets' orbits and their names.

## Installation
1. Ensure you have Python 3 installed on your system.
2. Install the required library:
   ```bash
   pip install pygame
   ```

## How to Run
1. Save the script as a `.py` file (e.g., `solar_system.py`).
2. Run the script using Python:
   ```bash
   python solar_system.py
   ```

## Controls
- Close the simulation by clicking the close button on the simulation window.

## Planetary Details
Each planet is initialized with the following parameters:
- **Distance from the Sun:** The average distance of the planet from the Sun (in astronomical units, AU).
- **Radius:** The visual size of the planet in the simulation.
- **Color:** The color of the planet for representation.
- **Mass:** The mass of the planet (in kilograms).
- **Orbital Velocity:** The initial velocity of the planet (in m/s).
- **Name:** The name of the planet, displayed in the simulation.

### Included Planets
- Sun (center of the system, stationary)
- Mercury
- Venus
- Earth
- Mars
- Jupiter
- Saturn
- Uranus
- Neptune

## Key Classes and Functions

### `Planet` Class
Defines the properties and behavior of a planet.
- **Attributes:** Distance from the Sun, radius, color, mass, velocity, and orbital path.
- **Methods:**
  - `draw(win)`: Draws the planet and its orbit.
  - `attraction(other)`: Calculates the gravitational force exerted by another planet.
  - `update_position(planets)`: Updates the planet's position and velocity based on gravitational forces.

### `draw_window(win, planets)`
Renders the simulation window and draws all planets.

### `main()`
Main loop of the simulation that:
- Initializes the planets.
- Updates their positions.
- Continuously redraws the simulation window.

## Simulation Scaling
- **Distance:** Scaled to make the vast distances in the solar system visually manageable.
- **Time:** Each frame represents one day in the simulation.

## Dependencies
- `pygame`

## Notes
- The simulation simplifies the solar system by assuming circular orbits and neglecting minor perturbations.
- The Sun is fixed at the center and does not move.

## References
- [Pygame Documentation](https://www.pygame.org/docs/)
- [NASA Solar System Overview](https://solarsystem.nasa.gov/)
- [Planetary Data from ESA](https://www.esa.int/Science_Exploration/Space_Science)
- [Astronomical Constants - Wikipedia](https://en.wikipedia.org/wiki/Astronomical_constant)

## Acknowledgments
- Inspired by the real-world dynamics of planetary motion and simplified for educational and visual purposes.

