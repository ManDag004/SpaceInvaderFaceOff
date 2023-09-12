import pygame
from network import Network
from player import Player

pygame.init()

SCREEN_INFO = pygame.display.Info()
WIDTH, HEIGHT = SCREEN_INFO.current_w, SCREEN_INFO.current_h

# Create the window with current screen's width and height
screen = pygame.display.set_mode((600, 800))

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


# updates the screen
def redraw(player_1, player_2):
    screen.fill((0, 0, 0))
    player_1.draw()
    player_2.draw()
    pygame.display.update()


def main():
    is_running = True
    n = Network()
    start_pos = read_pos(n.getPos())
    player_1 = Player(start_pos[0], start_pos[1], 100, 100, (255, 0, 0), screen)
    player_2 = Player(0, 0, 100, 100, (0, 0, 255), screen)
    while is_running:
        # clock.tick(60)
        player_2_pos = read_pos(n.send(make_pos((player_1.x, player_1.y))))
        player_2.x = player_2_pos[0]
        player_2.y = player_2_pos[1]
        player_2.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                pygame.quit()

        player_1.move()
        redraw(player_1, player_2)

if __name__ == "__main__":
    main()