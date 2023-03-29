from math import sin, cos
import pygame
from PlayerClass import player


class ProjectileSprite(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.angle = None
        self.x = None
        self.y = None
        self.colour = None
        self.xi = None
        self.yi = None
        self.image = pygame.Surface([5, 5])
        self.rect = self.image.get_rect()
        self.time = 0

    # returns a specific attribute of the projectile
    def getAttr(self, attribute):
        return self.__getattribute__(attribute)

    def update(self):
        if not self.x and not self.y:
            return
        self.rect.center = (self.x, self.y)

    # sets the initial angle of motion
    def setAngle(self, newAngle):
        self.angle = newAngle

    # draws the portal to the screen and calls the update position method, passing in a speed
    def drawProjectile(self, speedCoefficient, screen):
        if self.x is None or self.y is None:
            return
        self.updatePos(speedCoefficient)
        pygame.draw.rect(screen, self.colour, self.rect, 2)
        pygame.draw.circle(screen, self.colour, [self.x, self.y], 5)

    def setAttributes(self, angle, x, y, col):
        self.angle = angle
        self.x = x
        self.y = y
        self.colour = col

    def reset(self):
        self.x, self.y = None, None

    # updates the position of the projectile on the y and x-axis
    def updatePos(self, speedCoefficient):
        if not self.angle:
            return
        self.y -= sin(self.angle) * speedCoefficient
        self.x += cos(self.angle) * speedCoefficient

    def expire(self):
        self.time += 1
        if self.time > 100:
            self.x, self.y = None, None
            self.time = 0

    def startProjectile(self, angle, side, colour):
        player.setCanShoot(side, True)
        # if mouse button is pressed a projectile is created
        if player.getMousePress(side) and player.getCanShoot(side):
            self.setAttributes(angle, player.x + player.xChange, player.y + player.yChange, colour)
            player.setCanShoot(side, False)


projectileSprites = pygame.sprite.Group()
projectile = ProjectileSprite(1)
projectile2 = ProjectileSprite(2)
