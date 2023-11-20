import pygame
from network import Network

pygame.init()

SCREEN_INFO = pygame.display.Info()
WIDTH, HEIGHT = SCREEN_INFO.current_w, SCREEN_INFO.current_h
# WIDTH, HEIGHT = 600, 800

# Create the window with current screen's width and height
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# updates the screen
def redraw(player_1, enemy_ammo_in_home_list):
    screen.fill((0, 0, 0))
    player_1.draw(screen, enemy_ammo_in_home_list)
    pygame.display.update()


# game over screen
def game_over(did_win):
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 100)
    if did_win:
        text = font.render("You Win!", True, (255, 0, 0))
    else:
        text = font.render("You Lose!", True, (255, 0, 0))
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(2000)


def main():
    is_running = True
    n = Network()
    player_1 = n.getPlayer()
    while True:
        # set refresh rate to 60 fps
        pygame.time.delay(16)
        player_2 = n.send(player_1)

        if player_1.has_won:
            game_over(True)
            break

        elif player_2.has_won:
            game_over(False)
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        enemy_ammo_in_home_list = [ammo for ammo in player_2.ammo_list if ammo.territory == "enemy"]
        player_1.move()
        redraw(player_1, enemy_ammo_in_home_list)

        # check if the ammo of player 1 has hit player 2
        ammo_in_enemy_territory = [ammo for ammo in player_1.ammo_list if ammo.territory == "enemy"]
        for ammo in ammo_in_enemy_territory:
            if player_2.collided_with_ammo(ammo):
                player_2.hit(ammo)


if __name__ == "__main__":
    main()

