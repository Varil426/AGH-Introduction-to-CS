import pygame
import time
import random
import json
pygame.init()

with open('settings.json') as f:
    settings = json.load(f)

version = settings["settings"]["version"]
refreshRate = settings["settings"]["refreshRate"]
process = True

screenWidth = settings["settings"]["screenWidth"]
screenHeight = settings["settings"]["screenHeight"]
spacingVertical = settings["settings"]["spacingVertical"]
spacingHorizontal = settings["settings"]["spacingHorizontal"]

gameWidth = screenWidth - spacingHorizontal
gameHeight = screenHeight - spacingVertical * 2
gameArea = pygame.Surface((gameWidth, gameHeight))

pygame.display.set_caption("Space Invaders " + version)
window = pygame.display.set_mode((screenWidth, screenHeight))
music = pygame.mixer.music.load("assets/sounds/music.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.25)

class UI(object):
    def __init__(self):
        self.healthBarLength = gameWidth - 100
        self.healthBar = pygame.Surface((self.healthBarLength, 20))
        self.textSpacing = 30
        self.win = False
        self.pause = False
        self.death = False
        self.getScore = False
        self.name = []
        self.hitbox = False
    def draw(self):
        window.blit(Assets.font.render("Health", False, (255,255,255)), (20, screenHeight - 40))
        pygame.draw.rect(self.healthBar, (0, 0, 0), (0, 0, self.healthBarLength, 20))
        pygame.draw.rect(self.healthBar, (255, 255, 255), (0, 0, self.healthBarLength, 20), 1)
        pygame.draw.rect(self.healthBar, (255, 255, 255), (0, 0, int(self.healthBarLength * player.health/100), 20))
        window.blit(Assets.font.render("Stage: " + str(Menu.stage + 1), False, (255,255,255)), (20, 10))
        window.blit(Assets.font.render("Player 1", False, (255,255,255)), (gameWidth + 20, spacingVertical))
        window.blit(Assets.font.render("Score: " + str(player.score), False, (255,255,255)), (gameWidth + 20, spacingVertical + 1*self.textSpacing))
        window.blit(Assets.font.render("Damage: " + str(player.damage), False, (255,255,255)), (gameWidth + 20, spacingVertical + 2*self.textSpacing))
        window.blit(Assets.font.render("Bullets Speed: " + str(player.bulletsVelocity), False, (255,255,255)), (gameWidth + 20, spacingVertical + 3*self.textSpacing))
        window.blit(Assets.font.render("Time Between Shots: " + str(player.timeBetweenShots), False, (255,255,255)), (gameWidth + 20, spacingVertical + 4*self.textSpacing))
    def score(self):
        self.name.clear()
        while True:
            pressedkeys = pygame.key.get_pressed()
            event = pygame.event.poll()
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if len(key) == 1 and len(self.name) <= 20:
                    if pressedkeys[pygame.K_LSHIFT] or pressedkeys[pygame.K_RSHIFT]:
                        key = key.upper()
                    self.name.append(key)
                if key == "backspace" and len(self.name) > 0:
                    self.name.pop(len(self.name) - 1)
                if key == "return":
                    break
            pygame.draw.rect(gameArea, (255, 255, 255), (gameWidth//2 - 250, gameHeight//2 + 30, 500, 200))
            pygame.draw.rect(gameArea, (255, 0, 0), (gameWidth//2 - 250, gameHeight//2 + 30, 500, 200), 5)
            text = Assets.font.render("Name:", False, (0, 0, 0))
            gameArea.blit(text, (gameWidth//2 - text.get_width()//2, gameHeight//2 + 40))
            gameArea.blit(Assets.font.render(''.join(self.name), False, (0, 0, 0)), (gameWidth//2 - 250 + 5, gameHeight//2 + 80))
            window.blit(gameArea, (1, spacingVertical))
            pygame.display.update()
        self.getScore == False
        Menu.mode = 0
        if len(settings["scores"]) < 10:
            settings["scores"].append([''.join(self.name), player.score])
        elif player.score > settings["scores"][len(settings["scores"])-1][1]:
            settings["scores"][len(settings["scores"])-1][0] = ''.join(self.name)
            settings["scores"][len(settings["scores"])-1][1] = player.score
        for i in range(0, len(settings["scores"])):
            for j in range(0, len(settings["scores"]) - i - 1):
                if settings["scores"][j][1] < settings["scores"][j+1][1]:
                    settings["scores"][j][1], settings["scores"][j+1][1] = settings["scores"][j+1][1], settings["scores"][j][1]
                    settings["scores"][j][0], settings["scores"][j+1][0] = settings["scores"][j+1][0], settings["scores"][j][0]
        self.death = False

class Assets(object):
    def __init__(self):
        self.bg = pygame.image.load('assets/img/bg.jpg')
        self.font = pygame.font.Font("assets/font.ttf", 30)
        self.enemies = [pygame.image.load('assets/img/enemy1.png'),
            pygame.image.load('assets/img/enemy1.png'),
            pygame.image.load('assets/img/enemy2.png'),
            pygame.image.load('assets/img/enemy3.png'),
            pygame.image.load('assets/img/enemy4.png')
        ]
        self.player = pygame.image.load('assets/img/player.png')

class MenuButton(object):
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.width = 200
        self.height = 50
        self.text = text
        self.color = (0,0,0)
        self.textColor = (255,255,255)

class Menu(object):
    def __init__(self):
        self.selected = 0
        self.buttons = [MenuButton(200, 125, "New Game"), MenuButton(220, 200, "Continue"), MenuButton(240, 275, "Endless Mode"), MenuButton(260, 350, "Endless CO-OP"), MenuButton(280, 425, "Highest Scores"), MenuButton(300, 500, "Exit")]
        self.lastChange = 0
        self.mode = settings["settings"]["mode"]
        self.gameMode = 0
        self.stage = 0
        self.scores = False
        self.scoreboard = pygame.Surface((500, 50*11))
    def draw(self):
        window.blit(Assets.bg, (0, 0))
        for i in range(0, len(self.buttons)):
            if self.selected == i:
                pygame.draw.rect(window, (255, 255, 255), (self.buttons[i].x, self.buttons[i].y, self.buttons[i].width, self.buttons[i].height))
                window.blit(Assets.font.render(self.buttons[i].text, False, (0,0,0)), (self.buttons[i].x + 10, self.buttons[i].y + 12))
            else:
                pygame.draw.rect(window, self.buttons[i].color, (self.buttons[i].x, self.buttons[i].y, self.buttons[i].width, self.buttons[i].height))
                window.blit(Assets.font.render(self.buttons[i].text, False, self.buttons[i].textColor), (self.buttons[i].x + 10, self.buttons[i].y + 12))
        if self.scores:
            pygame.draw.rect(self.scoreboard, (255, 255, 255), (0,0,self.scoreboard.get_width(),50))
            self.scoreboard.blit(Assets.font.render("Highest Scores:", False, (0,0,0)), (10, 10))
            counter = 1
            for score in settings["scores"]:
                pygame.draw.rect(self.scoreboard, (255, 255, 255), (0,50*counter,self.scoreboard.get_width(),50),1)
                self.scoreboard.blit(Assets.font.render(score[0], False, (255,255,255)), (10, 50*counter+10))
                points = Assets.font.render(str(score[1]), False, (255,255,255))
                self.scoreboard.blit(points, (self.scoreboard.get_width() - 10 - points.get_width(), 50*counter+10))
                counter += 1
            pygame.draw.rect(self.scoreboard, (255, 255, 255), (1,1,self.scoreboard.get_width()-1,self.scoreboard.get_height()-1), 1)
            window.blit(self.scoreboard, (675, spacingVertical))
        pygame.draw.rect(window, (255,255,255), (20, screenHeight - 75, 210, 50))
        window.blit(Assets.font.render("Press Z to select", False, (0,0,0)), (25, screenHeight - 65))
    def controls(self):
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[pygame.K_UP] and self.selected > 0 and time.time() - self.lastChange > 0.25:
            self.selected -= 1
            self.lastChange = time.time()
        if pressedKeys[pygame.K_DOWN] and self.selected < len(self.buttons) - 1 and time.time() - self.lastChange > 0.25:
            self.selected += 1
            self.lastChange = time.time()
        if pressedKeys[pygame.K_z] and time.time() - self.lastChange > 0.25:
            if self.selected == 0:
                self.mode = 1
                self.gameMode = 0
                self.stage = 0
                settings["save"]["stage"] = self.stage
                settings["save"]["score"] = 0
                generateStage(self.gameMode,self.stage)
            elif self.selected == 1:
                self.mode = 1
                self.gameMode = 0
                self.stage = settings["save"]["stage"]
                generateStage(self.gameMode,self.stage)
                player.score = settings["save"]["score"]
                score(player)
            elif self.selected == 2:
                self.mode = 1
                self.gameMode = 1
                self.stage = 0
                generateStage(self.gameMode,self.stage)
                player.score = 0
                score(player)
            elif self.selected == 4:
                self.scores = not self.scores
            elif self.selected == 5:
                global process
                process = False
            self.lastChange = time.time()

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
        self.score = 0
        self.previousScore = 0
    def draw(self):
        if UI.hitbox:
            pygame.draw.rect(gameArea, (255, 0, 0), (self.x, self.y, self.width, self.height))
        gameArea.blit(Assets.player, (self.x, self.y))

class enemy(object):
    def __init__(self, type, x, y, width, height, health, color, score):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.bulletVelocity = 10
        self.color = color
        self.type = type
        self.score = score
    def draw(self):
        if UI.hitbox:
            pygame.draw.rect(gameArea, self.color, (self.x, self.y, self.width, self.height))
        gameArea.blit(Assets.enemies[self.type], (self.x, self.y))

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

class stone(object):
    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.color = (255, 255, 255)
    def draw(self):
        pygame.draw.rect(gameArea, self.color, (self.x, self.y, self.width, self.height))

class AI(object):
    def __init__(self):
        self.enemiesDirection = 1
        self.numberOfEnemies = 0
        self.enemiesMinVelocity = 5
        self.maxBonusVelocity = 3
        self.enemiesVelocity = self.enemiesMinVelocity
        self.counter = 1
        self.lastShot = 0
        self.movingForward = 0
        self.forwardVelocity = 5
        self.forwardStep = 5
    def AIControls(self):
        if self.numberOfEnemies > 0:
            if self.enemiesDirection > 0:
                index = len(enemies) - 1
                if enemies[index][0].x + self.enemiesVelocity * self.enemiesDirection > gameWidth - enemies[index][0].width:
                    self.enemiesDirection = -1
                    self.movingForward += self.forwardStep
            else:
                if enemies[0][0].x + self.enemiesVelocity * self.enemiesDirection < 0:
                    self.enemiesDirection = 1
                    self.movingForward += self.forwardStep
            for column in enemies:
                for enemy in column:
                    enemy.x += self.enemiesVelocity * self.enemiesDirection
                    if self.movingForward > 0:
                        enemy.y += self.forwardVelocity
            if self.movingForward > 0:
                self.movingForward -= self.forwardVelocity
            if time.time() - self.lastShot > self.counter:
                column = random.randrange(0, len(enemies))
                selected = enemies[column][len(enemies[column]) - 1]
                if selected.type == 3:
                    enemyBullets.append(projectile(selected.x, selected.y + selected.height, selected.bulletVelocity, (255, 0, 0)))
                    enemyBullets.append(projectile(selected.x + selected.width - 10, selected.y + selected.height, selected.bulletVelocity, (255, 0, 0)))
                else:
                    enemyBullets.append(projectile(selected.x + selected.width//2 - 5, selected.y + selected.height, selected.bulletVelocity, (255, 0, 0)))
                self.lastShot = time.time()

def generateEnemy(type, positionX, positionY):
    if type == 2:
        return enemy(type, positionX, positionY, 50, 50, 50, (255, 0, 255), 50)
    elif type == 3:
        return enemy(type, positionX, positionY, 50, 50, 100, (0, 0, 255), 100)
    elif type == 4:
        return enemy(type, positionX, positionY, 250, 250, 1000, (0, 0, 255), 1000)
    else:
        return enemy(type, positionX, positionY, 50, 50, 25, (0, 255, 0), 25)

def generateStage(gameMode, stage):
    if (gameMode == 0 and stage == 0) or (gameMode == 1 and stage == 0):
        player.health = 100
        player.score = 0
    enemies.clear()
    bullets.clear()
    stones.clear()
    enemyBullets.clear()
    startingHeight = 20
    stepVertical = 75
    startingWidth = 75
    stepHorizontal = 100
    AI.numberOfEnemies = 0
    stoneWidth = 50
    stoneHeight = 50
    if gameMode == 0:
        columns = len(settings["stage"][stage]["enemies"])
        for i in range(0, columns):
            enemies.append([])
            for j in range(0, len(settings["stage"][stage]["enemies"][i])):
                if settings["stage"][stage]["enemies"][i][j] != 0:
                    enemies[i].append(generateEnemy(settings["stage"][stage]["enemies"][i][j], startingWidth + i*stepHorizontal, startingHeight + stepVertical*j))
                    AI.numberOfEnemies += 1
        numberOfStones = settings["stage"][stage]["stones"]
        for i in range(0, numberOfStones):
            startingPoint = int((gameWidth/numberOfStones)/2 - stoneWidth * 1.5 + gameWidth/numberOfStones * i)
            for k in range(0, 2):
                for j in range(0, 3):
                    stones.append(stone(startingPoint + stoneWidth * j, gameHeight - 200 + stoneHeight * k, stoneWidth, stoneHeight, 100))
    else:
        columns = random.randrange(1,5)*2
        rolledEnemies = []
        for i in range(0, columns//2):
            rolledEnemies.append([])
            enemiesInColumns = random.randrange(1, 6)
            for j in range(0, enemiesInColumns):
                enemy = random.randrange(0,100)
                if enemy < 20 and len(rolledEnemies[i])>0:
                    enemy = 0
                elif enemy < 40:
                    enemy = 2
                elif enemy < 55:
                    enemy = 3
                else:
                    enemy = 1
                rolledEnemies[i].append(enemy)
        for i in range(0, columns//2):
            rolledEnemies.append(rolledEnemies[columns//2 - 1 - i])
        for i in range(0, columns):
            enemies.append([])
            for j in range(0, len(rolledEnemies[i])):
                if rolledEnemies[i][j] != 0:
                    enemies[i].append(generateEnemy(rolledEnemies[i][j], startingWidth + i*stepHorizontal, startingHeight + stepVertical*j))
                    AI.numberOfEnemies += 1
        numberOfStones = random.randrange(0,100)
        if (numberOfStones < 40):
            numberOfStones = 0
        elif (numberOfStones < 70):
            numberOfStones = 1
        elif (numberOfStones < 85):
            numberOfStones = 2
        else:
            numberOfStones = 3
        for i in range(0, numberOfStones):
            startingPoint = int((gameWidth/numberOfStones)/2 - stoneWidth * 1.5 + gameWidth/numberOfStones * i)
            for k in range(0, 2):
                for j in range(0, 3):
                    stones.append(stone(startingPoint + stoneWidth * j, gameHeight - 200 + stoneHeight * k, stoneWidth, stoneHeight, 100))
    if (AI.numberOfEnemies > 0):
        bonus = AI.maxBonusVelocity // (AI.numberOfEnemies/10)
        if bonus > AI.maxBonusVelocity:
            bonus = AI.maxBonusVelocity
        AI.enemiesVelocity = AI.enemiesMinVelocity + bonus

def killEnemy(index, enemy):
    enemies[index].pop(enemies[index].index(enemy))
    player.score += enemy.score
    score(player)
    if not enemies[index]:
        enemies.pop(index)
    AI.numberOfEnemies -= 1
    if AI.numberOfEnemies > 0:
        bonus = AI.maxBonusVelocity // (AI.numberOfEnemies/10)
        if bonus > AI.maxBonusVelocity:
            bonus = AI.maxBonusVelocity
        AI.enemiesVelocity = AI.enemiesMinVelocity + bonus

def removeBullet(bullet):
    bullets.pop(bullets.index(bullet))

def removeEnemyBullet(bullet):
    enemyBullets.pop(enemyBullets.index(bullet))

def removeStone(stone):
    stones.pop(stones.index(stone))

def colisionDetection(object1, object2):
    colisionX = False
    colisionY = False
    if object1.x > object2.x:
        object1, object2 = object2, object1
    if object1.x < object2.x and object1.x + object1.width > object2.x:
        colisionX = True
    if object1.y > object2.y:
        object1, object2 = object2, object1
    if object1.y < object2.y and object1.y + object1.height > object2.y:
        colisionY = True
    if colisionX and colisionY:
        return True
    else:
        return False

def colision():
    startingHeight = 20
    stepVertical = 100
    for bullet in bullets:
        for column in enemies:
            for enemy in column:
                if colisionDetection(enemy, bullet):
                    enemy.health -= player.damage
                    if enemy.health <= 0:
                        killEnemy(enemies.index(column), enemy)
                    removeBullet(bullet)
    for bullet in enemyBullets:
        if colisionDetection(player, bullet):
            removeEnemyBullet(bullet)
            player.health -= 25
    for bullet in bullets:
        for enemyBullet in enemyBullets:
            if colisionDetection(bullet, enemyBullet):
                removeBullet(bullet)
                removeEnemyBullet(enemyBullet)
    for stone in stones:
        for bullet in bullets:
            if colisionDetection(bullet, stone):
                stone.health -= player.damage
                removeBullet(bullet)
                if stone.health <= 0:
                    removeStone(stone)
        for bullet in enemyBullets:
            if colisionDetection(bullet, stone):
                stone.health -= 25
                removeEnemyBullet(bullet)
                if stone.health <= 0:
                    removeStone(stone)
    for column in enemies:
        for enemy in column:
            for stone in stones:
                if colisionDetection(enemy, stone):
                    removeStone(stone)
            if colisionDetection(player, enemy):
                player.health = 0
            if enemy.y > gameHeight:
                player.health = 0

def gameState():
    if player.health <= 0:
        UI.death = True
        UI.getScore = True
    if AI.numberOfEnemies <= 0:
        Menu.stage += 1
        if Menu.gameMode == 0:
            if Menu.stage < len(settings["stage"]):
                settings["save"]["stage"] = Menu.stage
                settings["save"]["score"] = player.score
                generateStage(Menu.gameMode, Menu.stage)
            else:
                settings["save"]["stage"] = 0
                settings["save"]["score"] = 0
                UI.win = True
        else:
            generateStage(Menu.gameMode, Menu.stage)

def score(player):
    for i in range(player.previousScore + 1, player.score + 1):
        if i % 1000 == 0:
            player.health += 25
            if player.health > 100:
                player.health = 100
    if player.score < 3000:
        if player.score >= 500 and player.score < 1000:
            player.timeBetweenShots = 0.4
        elif player.score >= 1000 and player.score < 1500:
            player.timeBetweenShots = 0.4
            player.bulletsVelocity = 20
            player.damage = 30
        elif player.score >= 1500 and player.score < 2000:
            player.timeBetweenShots = 0.3
            player.bulletsVelocity = 20
            player.damage = 30
        elif player.score >= 2000 and player.score < 2500:
            player.timeBetweenShots = 0.3
            player.bulletsVelocity = 25
            player.damage = 40
        elif player.score >= 2500 and player.score < 3000:
            player.timeBetweenShots = 0.25
            player.bulletsVelocity = 25
            player.damage = 40
    else:
        player.timeBetweenShots = 0.25
        player.bulletsVelocity = 30
        player.damage = 50
    player.previousScore = player.score



def refreshGameWindow():
    if not UI.win and not UI.pause and not UI.death:
        window.blit(Assets.bg, (0, 0))
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
        for stone in stones:
            stone.draw()
        player.draw()
        UI.draw()
        window.blit(UI.healthBar, (100, screenHeight - 35))
        colision()
        AI.AIControls()
        gameState()
    else:
        if UI.win:
            pygame.draw.rect(gameArea, (255, 255, 255), (gameWidth//2-183, gameHeight//2-25,366,50))
            gameArea.blit(Assets.font.render("You have defeated the invader", False, (0,0,0)), (gameWidth//2-183+5, gameHeight//2-25+15))
            UI.getScore = True
        if UI.pause:
            pygame.draw.rect(gameArea, (255, 255, 255), (gameWidth//2-50, gameHeight//2-25,100,50))
            gameArea.blit(Assets.font.render("PAUSE", False, (0,0,0)), (gameWidth//2-50+13, gameHeight//2-25+15))
        if UI.death:
            pygame.draw.rect(gameArea, (255, 0, 0), (0, gameHeight//2-25,gameWidth,50))
            gameArea.blit(Assets.font.render("You died", False, (0,0,0)), (gameWidth//2-50+10, gameHeight//2-25+15))
        if UI.getScore:
            UI.score()
    pygame.draw.rect(gameArea, (255, 255, 255), (0, 0, gameWidth, gameHeight), 1)
    window.blit(gameArea, (1, spacingVertical))

def controls():
    pressedKeys = pygame.key.get_pressed()
    if not UI.pause:
        if pressedKeys[pygame.K_LEFT] and player.x - player.velocity > 0:
            player.x -= player.velocity
        if pressedKeys[pygame.K_RIGHT] and player.x + player.velocity + player.width < gameWidth:
            player.x += player.velocity
        if pressedKeys[pygame.K_z] and len(bullets) < player.maxBullets and time.time() - player.lastBullet > player.timeBetweenShots:
            player.lastBullet = time.time()
            bullets.append(projectile(player.x + player.width//2 - 5, player.y, player.bulletsVelocity, (255, 255, 255)))
    if pressedKeys[pygame.K_ESCAPE]:
        if time.time() - Menu.lastChange > 0.25:
            Menu.lastChange = time.time()
            UI.pause = not UI.pause

def save():
    with open('settings.json', 'w') as f:
        json.dump(settings, f)

Assets = Assets()
UI = UI()
Menu = Menu()
player = player(gameWidth//2, gameHeight - 55, 50, 50)
AI = AI()
enemies = []
bullets = []
enemyBullets = []
stones = []

while process:
    pygame.time.delay(refreshRate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            process = False
    if Menu.mode == 0:
        Menu.controls()
        Menu.draw()
    elif Menu.mode == 1:
        controls()
        refreshGameWindow()
    pygame.display.update()
save()
pygame.quit()