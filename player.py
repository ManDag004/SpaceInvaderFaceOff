import pygame


class Player:
    def __init__(self, x, y, color, player_num):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.color = color
        self.speed = 4
        self.ammo = 7
        self.ammo_list = []
        self.player_num = player_num
        self.can_fire = True
        self.health = 5

    def draw(self, screen, enemy_ammo_in_home_list):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        for ammo in self.ammo_list:
            if ammo.territory == "home":
              ammo.draw(screen)

        for ammo in enemy_ammo_in_home_list:
            ammo.draw(screen)

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
        # fire only one ammo at the press of space
        if keys[pygame.K_SPACE]:
            if self.can_fire:
                self.shoot()
            self.can_fire = False
        if not keys[pygame.K_SPACE]:
            self.can_fire = True

        for ammo in self.ammo_list:
            ammo.move()

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
            if self.player_num == 0:
                self.ammo_list.append(Ammo(self.x + 100, self.y + 45, self.color, (8, 0), self))
            else:
                self.ammo_list.append(Ammo(self.x - 10, self.y + 45, self.color, (-8, 0), self))

    def hit(self, ammo):
        self.health -= 1
        ammo.self_destroy()
        if self.health == 0:
            return False
        return True
    
    def collided_with_ammo(self, ammo):
        return self.x < ammo.x < (self.x + self.width) and self.y < ammo.y < self.y + self.height


class Ammo:
    def __init__(self, x, y, color, speed, owner):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.color = color
        self.speed = speed
        self.owner = owner
        self.territory = "home"

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]

        if self.has_collided_with_wall():
            self.self_destroy()

    def has_collided_with_wall(self):
        if self.x < 0 or self.x > 600 or self.y < 0 or self.y > 800:
            if self.territory == "home":
                self.territory = "enemy"
                if self.speed[0] > 0:
                    self.x = 0
                else:
                    self.x = 600
            else:
                self.self_destroy()

    def self_destroy(self):
        self.owner.ammo_list.remove(self)
        self.owner.ammo += 1
