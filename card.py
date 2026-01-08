import pygame

# fo reference
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Card-specific values
CARD_COLOR = (70, 130, 180)
CARD_BORDER = (30, 30, 30)
CARD_SCALE = 1.5
CARD_WIDTH = 63 * CARD_SCALE
CARD_HEIGHT = 88 * CARD_SCALE

lock_points = [(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2), (SCREEN_WIDTH * 3 / 4, SCREEN_HEIGHT / 2)]

class Card:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        self.dragging = False

        # track offeset from mouse
        self.offset_x = 0
        self.offset_y = 0

    def handle_event(self, event : pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
                mouse_x, mouse_y = event.pos
                self.offset_x = self.rect.x - mouse_x
                self.offset_y = self.rect.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            # drop
            self.dragging = False

            # snap to closest lock_point
            dist_min = float('inf')
            dist_min_idx = -1
            for i in range(len(lock_points)):
                d = (lock_points[i][0] - self.rect.x) ** 2 + (lock_points[i][1] - self.rect.y) ** 2
                if d < dist_min:
                    dist_min = d
                    dist_min_idx = i
            self.rect.x = lock_points[dist_min_idx][0]
            self.rect.y = lock_points[dist_min_idx][1]
            


        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y

    def draw(self, surface):
        pygame.draw.rect(surface, CARD_COLOR, self.rect, border_radius=8)
        pygame.draw.rect(surface, CARD_BORDER, self.rect, 2, border_radius=8)