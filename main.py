import pygame

pygame.init()

SCREEN_INFO = pygame.display.Info()
WIDTH, HEIGHT = SCREEN_INFO.current_w, SCREEN_INFO.current_h

# Create the window with current screen's width and height
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 1

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed


def redraw(player):
    # update screen
    screen.fill((0, 0, 0))
    player.draw()
    pygame.display.update() 


def main():
    is_running = True
    player_1 = Player(0, 0, 100, 100, (255, 0, 0))

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                pygame.quit()
        
        player_1.move()
        redraw(player_1)  

if __name__ == "__main__":
    main()