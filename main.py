import pygame

pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Portal Example")

# Colors
WHITE = (255, 255, 255)
RED = (200, 50, 50)
PORTAL_COLORS = [(0, 100, 255), (255, 165, 0)]  # Blue and Orange

# Circle (player)
circle_pos = [100, 300]
circle_radius = 15
circle_speed = 5

# Portals
portals = [None, None]  # fixed size list for 2 portals
portal_index = 0  # which portal to place next

# Clock
clock = pygame.time.Clock()
running = True

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            size = 60
            rect = pygame.Rect(x - size // 2, y - size // 2, size, size)
            portals[portal_index] = rect
            portal_index = (portal_index + 1) % 2  # alternate portals

    # Movement (WASD / Arrow keys)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        circle_pos[0] -= circle_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        circle_pos[0] += circle_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        circle_pos[1] -= circle_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        circle_pos[1] += circle_speed

    # Teleport check (only if both portals exist)
    if all(portals):
        circle_rect = pygame.Rect(
            circle_pos[0] - circle_radius,
            circle_pos[1] - circle_radius,
            circle_radius * 2,
            circle_radius * 2,
        )

        if circle_rect.colliderect(portals[0]):
            circle_pos = [portals[1].centerx + circle_radius * 2 + 20, portals[1].centery]
        elif circle_rect.colliderect(portals[1]):
            circle_pos = [portals[0].centerx + circle_radius * 2 + 20, portals[0].centery]

    # Draw
    screen.fill(WHITE)

    # Draw portals
    for i, portal in enumerate(portals):
        if portal:
            pygame.draw.rect(screen, PORTAL_COLORS[i], portal, 5)

    # Draw circle
    pygame.draw.circle(screen, RED, circle_pos, circle_radius)

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
