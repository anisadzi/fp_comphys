import pygame

# Pygame initialization
pygame.init()
pygame.font.init()

# Define the background colour using RGB color coding
background_colour = (255, 255, 255)

# Define the dimensions of the screen object (width, height)
screen_width = 1440
screen_height = 950
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the caption of the screen
pygame.display.set_caption('Cycloid Curve')

# Fill the background colour to the screen
screen.fill(background_colour)

# Set up the font
font = pygame.font.Font(None, 28)

# Load the image of the cycloid curve
curve_image = pygame.image.load('cycloid_curve.png')

# Blit the curve image onto the screen
screen.blit(curve_image, (0, 0))

# Cycloid curve information
curve_info = [
    "Cycloid Curve",
    "-----------------",
    "- The cycloid curve is a type of trochoid curve.",
    "- It is traced by a point on the circumference of a rolling circle.",
    "- The equations for a cycloid curve are:",
    "     x = r(t - sin(t))",
    "     y = r(1 - cos(t))",
    "- The curve has symmetry with respect to both the x-axis and the y-axis.",
    "- The length of one arch of the cycloid curve is 8r.",
    "- Applications of the cycloid curve include gear design and pendulum motion.",
]

# Render the text on separate surfaces
text_surfaces = []
for line in curve_info:
    text_surface = font.render(line, True, pygame.Color('black'))
    text_surfaces.append(text_surface)

# Blit the text surfaces onto the screen
text_height = screen_height - 350
for text_surface in text_surfaces:
    screen.blit(text_surface, (25, text_height))
    text_height += 30

# Update the display using flip
pygame.display.flip()

# Variable to keep our game loop running
running = True

# Game loop
while running:
    # For loop through the event queue
    for event in pygame.event.get():
        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False

# Exit Pygame
pygame.quit()
