import pygame
from network import Network
from player import Player

pygame.init()

SCREEN_INFO = pygame.display.Info()
WIDTH, HEIGHT = SCREEN_INFO.current_w, SCREEN_INFO.current_h

# Create the window with current screen's width and height
screen = pygame.display.set_mode((600, 800))


# updates the screen
def redraw(player_1, player_2):
    screen.fill((0, 0, 0))
    player_1.draw(screen)
    player_2.draw(screen)
    pygame.display.update()


def main():
    is_running = True
    n = Network()
    player_1 = n.getPlayer()
    while is_running:
        # set refresh rate to 60 fps
        pygame.time.delay(16)
        player_2 = n.send(player_1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                pygame.quit()

        player_1.move()
        redraw(player_1, player_2)

if __name__ == "__main__":
    main()