import pygame

# Initialize Pygame
pygame.init()

# Screen settings
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Shining Circle Example")

# Colors
glow_color = (0, 255, 0)  # Green glow
white = (255, 255, 255)

# Function to draw a shining circle
def draw_shining_circle(surface, position, max_radius):
    for i in range(max_radius*2, 0, -2):  # Draw decreasing radius for glow effect
        inner_radius = max_radius/2
        if i < inner_radius:
            color = (255, 255, 255)
        elif i < max_radius:
            a = int(255 * (i-max_radius)/(inner_radius-max_radius))
            color = (a, 255, a)  # Adjust transparency based on radius
        else:
            a = int(255 * (i-max_radius*2)/(-max_radius*2))
            color = (0, a, 0)  # Adjust transparency based on radius
        pygame.draw.circle(surface, color, position, i)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw shining circles
    draw_shining_circle(screen, (300, 200), 80)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
