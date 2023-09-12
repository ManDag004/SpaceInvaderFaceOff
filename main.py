import pygame
from network import Network

pygame.init()

SCREEN_INFO = pygame.display.Info()
WIDTH, HEIGHT = SCREEN_INFO.current_w, SCREEN_INFO.current_h

# Create the window with current screen's width and height
screen = pygame.display.set_mode((600, 800))

# updates the screen
def redraw(player_1, enemy_ammo_in_home_list):
    screen.fill((0, 0, 0))
    player_1.draw(screen, enemy_ammo_in_home_list)
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

        enemy_ammo_in_home_list = [ammo for ammo in player_2.ammo_list if ammo.territory == "enemy"]
        player_1.move()
        redraw(player_1, enemy_ammo_in_home_list)

        # check if the ammo of player 1 has hit player 2
        ammo_in_enemy_territory = [ammo for ammo in player_1.ammo_list if ammo.territory == "enemy"]
        for ammo in ammo_in_enemy_territory:
            if player_2.collided_with_ammo(ammo):
                is_running = player_2.hit(ammo)


if __name__ == "__main__":
    main()