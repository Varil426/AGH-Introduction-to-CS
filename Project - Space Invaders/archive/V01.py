import pygame
import time
import random
pygame.init()

version = "0.1"
refreshRate = 33
process = True
bg = 0

screenWidth = 1280
screenHeight = 720
spacingVertical = 50
spacingHorizontal = 380

gameWidth = screenWidth - spacingHorizontal
gameHeight = screenHeight - spacingVertical * 2
gameArea = pygame.Surface((gameWidth, gameHeight))

pygame.display.set_caption("Space Invaders " + version)
window = pygame.display.set_mode((screenWidth, screenHeight))

class UI(object):
    def __init__(self):
        self.healthBarLength = gameWidth - 100
        self.healthBar = pygame.Surface((self.healthBarLength, 20))
    def draw(self):
        window.blit(font.render("Health", False, (255,255,255)), (20, screenHeight - 45))
        pygame.draw.rect(self.healthBar, (0, 0, 0), (0, 0, self.healthBarLength, 20))
        pygame.draw.rect(self.healthBar, (255, 255, 255), (0, 0, self.healthBarLength, 20), 1)
        pygame.draw.rect(self.healthBar, (255, 255, 255), (0, 0, int(self.healthBarLength * player.health/100), 20))

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = 100
        self.velocity = 15
        self.damage = 25
        self.maxBullets = 10
        self.bulletsVelocity = 15
        self.timeBetweenShots = 0.5
        self.lastBullet = 0
    def draw(self):
        pygame.draw.rect(gameArea, (255, 0, 0), (self.x, self.y, self.width, self.height))

class enemy(object):
    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.velocity = 5
        self.bulletVelocity = 10
    def draw(self):
        pygame.draw.rect(gameArea, (0, 255, 0), (self.x, self.y, self.width, self.height))

class projectile(object):
    def __init__(self, x, y, velocity, color):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.width = 10
        self.height = 20
        self.color = color
    def draw(self):
        pygame.draw.rect(gameArea, self.color, (self.x, self.y, self.width, self.height))

class AI(object):
    def __init__(self):
        self.enemiesDirection = 1
        self.counter = 1
        self.lastShot = 0
    def AIControls(self):
        if self.enemiesDirection > 0:
            for row in enemies:
                index = len(row) - 1
                if index > -1:
                    if row[index].x + row[index].velocity * self.enemiesDirection > gameWidth - row[index].width:
                        self.enemiesDirection = -1
        else:
            for row in enemies:
                if len(row) > 0:
                    if row[0].x + row[0].velocity * self.enemiesDirection < 0:
                        self.enemiesDirection = 1
        for row in enemies:
            for enemy in row:
                enemy.x += enemy.velocity * self.enemiesDirection
        if time.time() - self.lastShot > self.counter:
            row = random.randrange(0, 4)
            while len(enemies[row]) == 0:
                row = random.randrange(0, 4)
            column = random.randrange(0, len(enemies[row]))
            selected = enemies[row][column]
            enemyBullets.append(projectile(selected.x + selected.width//2, selected.y + selected.height, selected.bulletVelocity, (255, 0, 0)))
            self.lastShot = time.time()

def importImages():
    global bg
    bg = pygame.image.load('assets/img/bg.jpg')

def generateEnemies():
    startingHeight = 20
    stepVertical = 100
    startingWidth = 75
    stepHorizontal = 100
    for i in range(0, 4):
        for j in range(0, 8):
            enemies[i].append(enemy(startingWidth + j*stepHorizontal, startingHeight + stepVertical*i, 50, 50, 25))

def killEnemy(index, enemy):
    enemies[index].pop(enemies[index].index(enemy))

def removeBullet(bullet):
    bullets.pop(bullets.index(bullet))

def removeEnemyBullet(bullet):
    enemyBullets.pop(enemyBullets.index(bullet))

def colision():
    startingHeight = 20
    stepVertical = 100
    for bullet in bullets:
        if bullet.y > startingHeight and bullet.y < startingHeight + stepVertical:
            for enemy in enemies[0]:
                if enemy.y < bullet.y and enemy.y + enemy.height > bullet.y and enemy.x < bullet.x + bullet.width and enemy.x + enemy.width > bullet.x:
                    enemy.health -= player.damage
                    if enemy.health <= 0:
                        killEnemy(0, enemy)
                    removeBullet(bullet)
        elif bullet.y > startingHeight + stepVertical * 1 and bullet.y < startingHeight + stepVertical * 2:
            for enemy in enemies[1]:
                if enemy.y < bullet.y and enemy.y + enemy.height > bullet.y and enemy.x < bullet.x + bullet.width and enemy.x + enemy.width > bullet.x:
                    enemy.health -= player.damage
                    if enemy.health <= 0:
                        killEnemy(1, enemy)
                    removeBullet(bullet)
        elif bullet.y > startingHeight + stepVertical * 2 and bullet.y < startingHeight + stepVertical * 3:
            for enemy in enemies[2]:
                if enemy.y < bullet.y and enemy.y + enemy.height > bullet.y and enemy.x < bullet.x + bullet.width and enemy.x + enemy.width > bullet.x:
                    enemy.health -= player.damage
                    if enemy.health <= 0:    
                        killEnemy(2, enemy)
                    removeBullet(bullet)
        else:
            for enemy in enemies[3]:
                if enemy.y < bullet.y and enemy.y + enemy.height > bullet.y and enemy.x < bullet.x + bullet.width and enemy.x + enemy.width > bullet.x:
                    enemy.health -= player.damage
                    if enemy.health <= 0:
                        killEnemy(3, enemy)
                    removeBullet(bullet)
    for bullet in enemyBullets:
        if bullet.y + bullet.height > player.y and bullet.x + bullet.width > player.x and bullet.x < player.x + player.width:
            removeEnemyBullet(bullet)
            player.health -= 25

def refreshGameWindow():
    window.blit(bg, (0, 0))
    gameArea.fill((0, 0, 0))
    for bullet in bullets:
        if bullet.y - bullet.velocity < 0:
            removeBullet(bullet)
        else:
            bullet.y -= bullet.velocity
            bullet.draw()
    for bullet in enemyBullets:
        if bullet.y > gameHeight:
            removeEnemyBullet(bullet)
        else:
            bullet.y += bullet.velocity
            bullet.draw()
    for row in enemies:
        for enemy in row:
            enemy.draw()
    player.draw()
    pygame.draw.rect(gameArea, (255, 255, 255), (0, 0, gameWidth, gameHeight), 1)
    UI.draw()
    window.blit(gameArea, (1, spacingVertical))
    window.blit(UI.healthBar, (100, screenHeight - 35))
    colision()
    AI.AIControls()
    pygame.display.update()

def controls():
    pressedKeys = pygame.key.get_pressed()
    if pressedKeys[pygame.K_LEFT] and player.x - player.velocity > 0:
        player.x -= player.velocity
    if pressedKeys[pygame.K_RIGHT] and player.x + player.velocity + player.width < gameWidth:
        player.x += player.velocity
    if pressedKeys[pygame.K_z] and len(bullets) < player.maxBullets and time.time() - player.lastBullet > player.timeBetweenShots:
        player.lastBullet = time.time()
        bullets.append(projectile(player.x + player.width//2, player.y, player.bulletsVelocity, (255, 255, 255)))

UI = UI()
font = pygame.font.SysFont("Arial", 30)
player = player(gameWidth//2, gameHeight - 55, 50, 50)
enemies = [[],[],[],[]]
AI = AI()
bullets = []
enemyBullets = []
importImages()
generateEnemies()

while process:
    pygame.time.delay(refreshRate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            process = False
    controls()
    refreshGameWindow()
pygame.quit()