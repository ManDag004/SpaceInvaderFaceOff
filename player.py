import pygame


class Player:
    def __init__(self, x, y, color, player_num):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.color = color
        self.speed = 1
        self.ammo = 7
        self.ammoList = []
        self.player_num = player_num
        self.can_fire = True

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        for ammo in self.ammoList:
            ammo.move()
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

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
            if self.player_num == 0:
                self.ammoList.append(Ammo(self.x + 100, self.y + 45, self.color, (7, 0), self))
            else:
                self.ammoList.append(Ammo(self.x - 10, self.y + 45, self.color, (-7, 0), self))


class Ammo:
    def __init__(self, x, y, color, speed, owner):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.color = color
        self.speed = speed
        self.owner = owner

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]

        if self.has_collided():
            self.self_destroy()

    def has_collided(self):
        return self.x < 0 or self.x > 600 or self.y < 0 or self.y > 800

    def self_destroy(self):
        self.owner.ammoList.remove(self)
        self.owner.ammo += 1
