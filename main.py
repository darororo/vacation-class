import pygame


# --- Constants ---
WHITE = (255, 255, 255)
RED = (200, 50, 50)
PORTAL_COLORS = [(200, 100, 255), (255, 165, 100)]  # Blue and Orange


# --- Player class ---
class Player:
    def __init__(self, x, y, radius=25, speed=4):
        self.pos = [x, y]
        self.radius = radius
        self.speed = speed
        self.color = RED

    def get_rect(self):
        return pygame.Rect(
            self.pos[0] - self.radius,
            self.pos[1] - self.radius,
            self.radius * 2,
            self.radius * 2,
        )

    def handle_input(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.pos[0] -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.pos[0] += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.pos[1] -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.pos[1] += self.speed

    def teleport_to(self, portal):
        self.pos = [portal.rect.centerx + self.radius * 2 + 20, portal.rect.centery]

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)


# --- Portal class ---
class Portal:
    SIZE = 60

    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x - self.SIZE // 2, y - self.SIZE // 2, self.SIZE, self.SIZE)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 5)


# --- Game class ---
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Portal Example (OOP)")

        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player(100, 300, radius=25, speed=20)
        self.portals = [None, None]
        self.portal_index = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                self.portals[self.portal_index] = Portal(x, y, PORTAL_COLORS[self.portal_index])
                self.portal_index = (self.portal_index + 1) % 2

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)

        # Teleport if colliding with a portal
        if all(self.portals):
            if self.player.get_rect().colliderect(self.portals[0].rect):
                self.player.teleport_to(self.portals[1])
            elif self.player.get_rect().colliderect(self.portals[1].rect):
                self.player.teleport_to(self.portals[0])

    def draw(self):
        self.screen.fill(WHITE)

        for portal in self.portals:
            if portal:
                portal.draw(self.screen)

        self.player.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()


# --- Run the game ---
if __name__ == "__main__":
    Game().run()
