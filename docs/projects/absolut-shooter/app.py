# Import all necessary packages
import pygame
import sys
import time
import random


def play_sound(file_path, repeat, channel):
    pygame.mixer.init()
    pygame.mixer.set_num_channels(100)
    pygame.mixer.Channel(channel).play(
        pygame.mixer.Sound(file_path), loops=repeat)


# Initialize Pygame
pygame.init()
play_sound("./assets/music/starwars.mp3", -1, 0)

# Constants
WIDTH, HEIGHT = 1000, 800
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BOSS_SPAWN = 100
BACKGROUND = pygame.transform.scale(pygame.image.load(
    "./assets/images/backgrounds/game_bg.gif"), (WIDTH, HEIGHT))
FRAMES = [
    pygame.transform.scale(pygame.image.load(
        "./assets/images/backgrounds/frames/frame_00.gif"), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/backgrounds/frames/frame_01.gif"), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/backgrounds/frames/frame_02.gif"), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/backgrounds/frames/frame_03.gif"), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/backgrounds/frames/frame_04.gif"), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/backgrounds/frames/frame_05.gif"), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/backgrounds/frames/frame_06.gif"), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/backgrounds/frames/frame_07.gif"), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/backgrounds/frames/frame_08.gif"), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/backgrounds/frames/frame_09.gif"), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/backgrounds/frames/frame_10.gif"), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/backgrounds/frames/frame_11.gif"), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/backgrounds/frames/frame_12.gif"), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/backgrounds/frames/frame_13.gif"), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/backgrounds/frames/frame_14.gif"), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/backgrounds/frames/frame_15.gif"), (WIDTH, HEIGHT))
]
# Game states
START_MENU = 0
PLAYING = 1
PAUSED = 2
GAME_OVER = 3

# Initialize the game state
game_state = START_MENU

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Absolut Shooter")

# variables
clock = pygame.time.Clock()
start_time = time.time()
enemy_spawn_rate = 5
mine_spawn_rate = 2
pause_start_time = 0
elapsed_time = 0
player_speed = 5
boss_images = [
    pygame.image.load("./assets/images/sprites/boss1.png").convert_alpha(),
    pygame.image.load("./assets/images/sprites/boss2.png").convert_alpha(),
    pygame.image.load("./assets/images/sprites/boss3.png").convert_alpha()
]
enemy_img = [
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/enemy1.png").convert_alpha(), (40, 60)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/enemy2.png").convert_alpha(), (40, 60)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/enemy3.png").convert_alpha(), (40, 60)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/enemy4.png").convert_alpha(), (40, 60))
]
bullet_img = [
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/bullets/bean.png").convert_alpha(), (15, 19)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/bullets/plasma.png").convert_alpha(), (15, 19))
]
explosion_img = [
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/explosion/1.png").convert_alpha(), (60, 60)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/explosion/2.png").convert_alpha(), (60, 60)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/explosion/3.png").convert_alpha(), (60, 60)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/explosion/4.png").convert_alpha(), (60, 60)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/explosion/5.png").convert_alpha(), (60, 60)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/explosion/6.png").convert_alpha(), (60, 60)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/explosion/7.png").convert_alpha(), (60, 60)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/explosion/8.png").convert_alpha(), (60, 60)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/explosion/9.png").convert_alpha(), (60, 60))
]
explosion_img2 = [
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/explosion/1.png").convert_alpha(), (400, 400)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/explosion/2.png").convert_alpha(), (400, 400)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/explosion/3.png").convert_alpha(), (400, 400)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/explosion/4.png").convert_alpha(), (400, 400)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/explosion/5.png").convert_alpha(), (400, 400)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/explosion/6.png").convert_alpha(), (400, 400)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/explosion/7.png").convert_alpha(), (400, 400)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/explosion/8.png").convert_alpha(), (400, 400)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/explosion/9.png").convert_alpha(), (400, 400))
]
laser_img = [
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/laser/frame_0.gif").convert_alpha(), (40, HEIGHT+200)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/laser/frame_1.gif").convert_alpha(), (40, HEIGHT+200)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/laser/frame_2.gif").convert_alpha(), (40, HEIGHT+200)),
    pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/laser/frame_3.gif").convert_alpha(), (40, HEIGHT+200)),
]
frame = 0
laser_frame = 0

# Fonts
FONT = pygame.font.SysFont("Algerian", 30)

# Classes


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(
            "./assets/images/sprites/spaceship.png").convert_alpha(), (40, 60))
        self.rect = self.image.get_rect()
        self.speed = player_speed
        self.rect.center = (WIDTH // 2, HEIGHT)
        self.health = 5
        self.max_health = 5
        self.score = 0
        self.bullets = pygame.sprite.Group()
        self.laser = pygame.sprite.Group()
        self.shoot_delay = 6
        self.shoot_timer = 0
        self.laser_cooldown = 0
        self.laser_duration = 0
        self.laser_max_duration = 120
        self.laser_delay = 3
        self.laser_current = 0

    def update(self):
        global game_state
        # Set's speed according to the current score
        self.speed = player_speed + (self.score // 100) / 2
        # Respond to user inputs
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if player.score > BOSS_SPAWN + 10:
            if self.laser_cooldown <= 0:
                if keys[pygame.K_SPACE]:
                    self.laser_duration += 1
                    if self.laser_duration <= self.laser_max_duration:
                        self.shoot_laser()
                    else:
                        self.laser_duration = 0
                        self.laser_cooldown = 600
            else:
                self.laser_cooldown -= 1
                if self.laser_duration > 0:
                    self.laser_duration -= 1

        # Keeps player inside screen
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))
        # Checks for bullet collisions with enemy
        bullet_enemy_collisions = pygame.sprite.groupcollide(
            self.bullets, enemies, True, False)
        for bullet, enemy_list in bullet_enemy_collisions.items():
            bullet.kill()
            for enemy in enemy_list:
                enemy.health -= 1
                if enemy.health <= 0:
                    self.score += 1
                    explosion = Explosion(
                        enemy.rect.centerx, enemy.rect.centery, 0)
                    play_sound("./assets/sounds/explosions/2.ogg",
                               0, round(random.randint(2, 7)))
                    all_sprites.add(explosion)
                    enemy.kill()
        # Checks for player collisions with enemies
        player_enemy_collisions = pygame.sprite.groupcollide(
            player_group, enemies, False, True)
        for player_list, enemy_list in player_enemy_collisions.items():
            for enemy in enemy_list:
                player_list.health -= enemy.health
                play_sound("./assets/sounds/shots/laser.ogg", 0, 1)
                self.score += 1
                explosion = Explosion(enemy.rect.centerx,
                                      enemy.rect.centery, 0)
                play_sound("./assets/sounds/explosions/2.ogg",
                           0, round(random.randint(2, 7)))
                all_sprites.add(explosion)
                enemy.kill()
                if player_list.health <= 0:
                    player_list.health = 0
                    player_list.kill()
                    game_state = GAME_OVER
        # Checks for player collisions with mines
        player_mine_collisions = pygame.sprite.groupcollide(
            player_group, mines, True, True)
        for player_list, mine_list in player_mine_collisions.items():
            for mine in mine_list:
                play_sound("./assets/sounds/explosions/1.ogg", 0, 1)
                mine.kill()
                player.health = 0
                game_state = GAME_OVER
        # Checks for player collisions with health packets
        player_healthpacket_collisions = pygame.sprite.groupcollide(
            player_group, health_packets, False, True)
        for player_list, powerup_list in player_healthpacket_collisions.items():
            for powerup in powerup_list:
                player.health += powerup.health
                if player.health >= player.max_health:
                    player.health = player.max_health
                powerup.kill()
                game_state = PLAYING
        # Checks for player bullet colliding with boss
        bullet_boss_collisions = pygame.sprite.groupcollide(
            self.bullets, bosses, True, False)
        for bullet, boss_list in bullet_boss_collisions.items():
            bullet.kill()
            for boss in boss_list:
                boss.health -= 1
                if boss.health <= 0:
                    self.health = self.max_health
                    self.score += 10
                    for sprite in boss.bullets:
                        sprite.kill()
                    explosion = Explosion(
                        boss.rect.centerx, boss.rect.centery, 1)
                    all_sprites.add(explosion)
                    play_sound("./assets/sounds/explosions/3.ogg", 0, 1)
                    boss.kill()
        # Checks for player colliding with boss
        player_boss_collisions = pygame.sprite.groupcollide(
            player_group, bosses, True, False)
        for player_list, boss_list in player_boss_collisions.items():
            for boss in boss_list:
                player.health = 0
                game_state = GAME_OVER
        # Checks for laser collisions with enemies
        laser_enemy_collisions = pygame.sprite.groupcollide(
            self.laser, enemies, False, True)
        for lasers, enemy_list in laser_enemy_collisions.items():
            for enemy in enemy_list:
                self.score += 1
                explosion = Explosion(enemy.rect.centerx,
                                      enemy.rect.centery, 0)
                play_sound("./assets/sounds/explosions/2.ogg",
                           0, round(random.randint(2, 7)))
                all_sprites.add(explosion)
                enemy.kill()
        # Checks for laser collisions with boss
        laser_boss_collisions = pygame.sprite.groupcollide(
            self.laser, bosses, False, False)
        for lasers, boss_list in laser_boss_collisions.items():
            if self.laser_current == self.laser_delay:
                self.laser_current = 0
                for boss in boss_list:
                    boss.health -= 1
                    if boss.health <= 0:
                        self.health = 5
                        self.score += 10
                        for sprite in boss.bullets:
                            sprite.kill()
                        explosion = Explosion(
                            boss.rect.centerx, boss.rect.centery, 1)
                        all_sprites.add(explosion)
                        play_sound("./assets/sounds/explosions/3.ogg", 0, 1)
                        boss.kill()
            else:
                self.laser_current += 1

    # bullets
        if self.shoot_timer > 0:
            self.shoot_timer -= 1
        if self.shoot_timer == 0:
            if self.score > BOSS_SPAWN + 10:
                if keys[pygame.K_SPACE]:
                    if self.laser_cooldown > 0:
                        self.shoot_bullet()
                else:
                    self.shoot_bullet()
            else:
                self.shoot_bullet()

    def shoot_bullet(self):
        speed = 7 + (self.score // 50) / 2
        new_bullet = Bullet(self.rect.centerx, self.rect.top, 0, speed, 0)
        all_sprites.add(new_bullet)
        self.bullets.add(new_bullet)
        self.shoot_timer = self.shoot_delay

    def shoot_laser(self):
        play_sound("./assets/sounds/SUIII.mp3", 0,
                   round(random.randint(7, 99)))
        if len(self.laser) <= 1:
            new_laser = Laser(self.rect.centerx, self.rect.top)
            all_sprites.add(new_laser)
            self.laser.add(new_laser)
        else:
            self.laser.update()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()

        self.type = random.randint(0, 3)
        self.image = enemy_img[self.type]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.health = 1
        if self.type == 2:
            self.health = 2
        self.speed = speed

    def update(self):
        # Move the enemies vertically
        self.rect.y += self.speed
        # If enemy outside screen, remove it
        if self.rect.y >= HEIGHT:
            self.kill()
            enemies.remove(self)


class Mine(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(
            "./assets/images/sprites/mine.png").convert_alpha(), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.health = 1
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= HEIGHT:
            self.kill()
            mines.remove(self)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, type, yspeed, xspeed):
        super().__init__()

        self.type = type
        self.image = bullet_img[type]
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.yspeed = yspeed
        self.xspeed = xspeed

    def update(self):
        self.rect.y -= self.yspeed
        self.rect.x += self.xspeed
        if self.rect.y <= 0:
            self.kill()
            all_sprites.remove(self)
            player.bullets.remove(self)


class Health_Packet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(
            "./assets/images/sprites/health.png").convert_alpha(), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.health = 2
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= HEIGHT:
            self.kill()
            health_packets.remove(self)


class Boss(pygame.sprite.Sprite):
    boss_state = ["spawning", "active", "dead"]
    boss_direction = ["right", "left"]
    boss_direction = [0]
    boss_bar_width = 0

    def __init__(self, x, y, health, speed):
        super().__init__()
        if player.score < BOSS_SPAWN * 5:
            self.type = 0
        elif player.score < BOSS_SPAWN * 10:
            self.type = 1
        elif player.score < BOSS_SPAWN * 15:
            self.type = 2
        else:
            self.type = round(random.randint(0, 2))
        self.boss_width, self.boss_height = boss_images[self.type].get_size()
        self.image = pygame.transform.scale(
            boss_images[self.type], (self.boss_width*0.4, self.boss_height*0.4))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x-170, y)
        self.health = health
        self.speed = speed
        self.boss_state = [0]
        self.bullets = pygame.sprite.Group()
        self.shoot_delay = 30
        self.shoot_timer = 0
        self.initial_health = self.health
        self.boss_bar = 295

    def update(self):
        global game_state
        if self.boss_state == [0]:
            self.rect.y += self.speed
        if self.rect.y >= 90:
            self.boss_state = [1]
        if self.boss_state == [1]:
            if self.boss_direction == [0]:
                self.rect.x += self.speed
                if self.rect.x > 700:
                    self.boss_direction = [1]
            if self.boss_direction == [1]:
                self.rect.x -= self.speed
                if self.rect.x < -100:
                    self.boss_direction = [0]
        if self.shoot_timer > 0:
            self.shoot_timer -= 1
        if self.shoot_timer == 0:
            play_sound("./assets/sounds/shots/bullet.ogg", 0, 1)
            self.shoot_bullet()
        # Checks for boss bullets collisions with player
        bullets_player_collisions = pygame.sprite.groupcollide(
            self.bullets, player_group, True, False)
        for bullet, player_list in bullets_player_collisions.items():
            bullet.kill()
            player.health -= 1
            play_sound("./assets/sounds/shots/laser.ogg", 0, 1)
            if player.health <= 0:
                player.health = 0
                game_state = GAME_OVER

        if self.health != 0:
            self.boss_bar = (295 * (self.health / self.initial_health))

        boss_health_bar_border = pygame.Rect(WIDTH/2 - 155, 50, 305, 30)
        boss_health = pygame.Rect(WIDTH/2 - 150, 55, self.boss_bar, 20)

        pygame.draw.rect(screen, "grey", boss_health_bar_border)
        pygame.draw.rect(screen, "dark red", boss_health)

    def shoot_bullet(self):
        speed = -6
        xspeed = random.randint(-3, 3)
        new_bullet1 = Bullet(self.rect.left+150,
                             self.rect.bottom, 1, speed, xspeed)
        new_bullet2 = Bullet(self.rect.right-150,
                             self.rect.bottom, 1, speed, -xspeed)
        all_sprites.add(new_bullet1, new_bullet2)
        self.bullets.add(new_bullet1, new_bullet2)
        self.shoot_timer = self.shoot_delay


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.type = type
        if type == 0:
            self.images = explosion_img
        elif type == 1:
            self.images = explosion_img2
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_speed = 0.1  # Adjust the animation speed as needed
        self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed * 1000:
            self.last_update = now
            self.index += 1
            if self.index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.index]


class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = laser_img
        self.image = self.images[laser_frame]
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.animation_speed = 0.1
        self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        global laser_frame
        laser_frame += 1
        if laser_frame >= len(self.images):
            laser_frame = 0
        if now - self.last_update > self.animation_speed * 1000:
            self.last_update = now
            if laser_frame < len(self.images):
                laser_frame = 0
                self.image = self.images[laser_frame]
            else:
                self.image = self.images[laser_frame]
        if self.rect.centerx != player.rect.centerx:
            self.kill()
        if self.rect.centery != player.rect.top:
            self.kill()


# all sprite groups excluding player.bullets
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
enemies = pygame.sprite.Group()
mines = pygame.sprite.Group()
health_packets = pygame.sprite.Group()
bosses = pygame.sprite.Group()

# draw text functions


def draw_text(text, color, x, y):
    text_surface = FONT.render(text, True, color)
    screen.blit(text_surface, (x, y))


def draw_text_bigger(text, color, x, y):
    font = pygame.font.SysFont("Algerian", 40)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Game state draw screens


def start_menu():
    global frame
    # Animate background
    if frame <= 15:
        screen.blit(FRAMES[frame], (0, 0))
        frame += 1
    else:
        frame = 0
        screen.blit(FRAMES[frame], (0, 0))
    start_message = pygame.transform.scale(pygame.image.load(
        "./assets/images/sprites/cristiano-ronaldo.png"), (300, 600))
    screen.blit(start_message, (WIDTH // 2 -
                start_message.get_width() // 2, HEIGHT // 2-300))
    start_button = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 - 55, 150, 50)
    quit_button = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 + 5, 150, 50)
    # Draw rectangles
    pygame.draw.rect(screen, "sky blue", start_button)
    pygame.draw.rect(screen, "red", quit_button)

    # Draw texts inside rectangles
    draw_text("Start", BLACK, WIDTH // 2 - 50, HEIGHT // 2 - 50)
    draw_text("Quit", WHITE, WIDTH // 2 - 30, HEIGHT // 2 + 10)


def play_game():
    global frame
    # Animate background
    if frame <= 15:
        screen.blit(FRAMES[frame], (0, 0))
        frame += 1
    else:
        frame = 0
        screen.blit(FRAMES[frame], (0, 0))
    # Updates all sprites (See def update in the classes)
    all_sprites.update()
    all_sprites.draw(screen)
    # Spawns enemies
    if random.randint(1, 100) < enemy_spawn_rate + player.score // 25:
        if enemies.__len__() <= 40 and bosses.__len__() == 0:
            enemy_speed = 6 + (player.score // 100)/2
            new_enemy = Enemy(random.randint(0, WIDTH - 40), -60, enemy_speed)
            all_sprites.add(new_enemy)
            enemies.add(new_enemy)
    # Spawns mines
    if random.randint(1, 1000) < mine_spawn_rate + player.score // 50:
        if mines.__len__() <= 3:
            new_mine = Mine(random.randint(0, WIDTH - 40), -40, 2)
            all_sprites.add(new_mine)
            mines.add(new_mine)
    # Spawns power ups
    if random.randint(1, 2000) < mine_spawn_rate:
        if health_packets.__len__() <= 2:
            new_power_up = Health_Packet(random.randint(0, WIDTH - 40), -40, 3)
            all_sprites.add(new_power_up)
            health_packets.add(new_power_up)
    # Spawn bosses
    array = [0, 1, 2, 3, 4, 5]
    if array.count(player.score) == 0 and player.score % BOSS_SPAWN >= 0 and player.score % BOSS_SPAWN <= 5 and bosses.__len__() == 0:
        new_boss = Boss(WIDTH / 2, - 500, player.score, 3)
        all_sprites.add(new_boss)
        bosses.add(new_boss)
    # Displays stats
    draw_text(f"Time: {round(elapsed_time)}s", WHITE, 10, 10)
    draw_text(f"Lives: {player.health}", WHITE, WIDTH - 130, 10)
    draw_text(f"Score: {player.score}", WHITE, WIDTH // 2 - 70, 10)
    draw_text(f"Wave {(player.score - 10) // (BOSS_SPAWN) + 1}", WHITE, 10, 50)
    if (player.score >= BOSS_SPAWN + 10):
        draw_text(
            f"Laser Cooldown: {player.laser_cooldown//60}s", WHITE, WIDTH - 320, 50)


def pause_menu():
    # screen.blit(BACKGROUND, (0,0))
    # Paused text
    draw_text_bigger("Paused", WHITE, WIDTH // 2 - 70, HEIGHT // 2 - 50)
    # Buttons
    resume_button = pygame.Rect(WIDTH // 2 - 70, HEIGHT // 2, 150, 50)
    restart_button = pygame.Rect(WIDTH // 2 - 70, HEIGHT // 2 + 60, 150, 50)
    home_button = pygame.Rect(WIDTH // 2 - 70, HEIGHT // 2 + 120, 150, 50)
    quit_button = pygame.Rect(WIDTH // 2 - 70, HEIGHT // 2 + 180, 150, 50)
    # Draw the buttons
    pygame.draw.rect(screen, "sky blue", resume_button)
    pygame.draw.rect(screen, "sky blue", restart_button)
    pygame.draw.rect(screen, "sky blue", home_button)
    pygame.draw.rect(screen, "red", quit_button)
    # Add text to buttons
    draw_text("Resume", BLACK, WIDTH // 2 - 50, HEIGHT // 2 + 10)
    draw_text("Restart", BLACK, WIDTH // 2 - 60, HEIGHT // 2 + 70)
    draw_text("Home", BLACK, WIDTH // 2 - 35, HEIGHT // 2 + 130)
    draw_text("Quit", WHITE, WIDTH // 2 - 25, HEIGHT // 2 + 190)


def game_over_menu():
    # screen.blit(BACKGROUND, (0,0))
    # Game over texts
    draw_text("Game Over", "red", WIDTH // 2 - 75, HEIGHT // 2 - 55)
    draw_text(f"Score: {player.score}", WHITE,
              WIDTH // 2 - 65, HEIGHT // 2 + 5)
    # Buttons
    restart_button = pygame.Rect(WIDTH // 2 - 70, HEIGHT // 2 + 65, 150, 50)
    home_button = pygame.Rect(WIDTH // 2 - 70, HEIGHT // 2 + 125, 150, 50)
    quit_button = pygame.Rect(WIDTH // 2 - 70, HEIGHT // 2 + 185, 150, 50)
    # Draw buttons
    pygame.draw.rect(screen, "sky blue", restart_button)
    pygame.draw.rect(screen, "sky blue", home_button)
    pygame.draw.rect(screen, "red", quit_button)
    # Button text
    draw_text("Restart", BLACK, WIDTH // 2 - 60, HEIGHT // 2 + 75)
    draw_text("Home", BLACK, WIDTH // 2 - 35, HEIGHT // 2 + 135)
    draw_text("Quit", WHITE, WIDTH // 2 - 25, HEIGHT // 2 + 195)


while True:
    # All events
    for event in pygame.event.get():
        # Close window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Listen for mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Response towards clicking a button on start menu
            if game_state == START_MENU:
                start_button = pygame.Rect(
                    WIDTH // 2 - 75, HEIGHT // 2 - 55, 150, 50)
                quit_button = pygame.Rect(
                    WIDTH // 2 - 75, HEIGHT // 2 + 5, 150, 50)
                if start_button.collidepoint(mouse_x, mouse_y):
                    start_time = time.time()
                    game_state = PLAYING

                    play_sound("./assets/sounds/SUIII.mp3", 0, 1)
                if quit_button.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit()
            # Response towards clicking a button on pause menu
            if game_state == PAUSED:
                resume_button = pygame.Rect(
                    WIDTH // 2 - 70, HEIGHT // 2, 150, 50)
                restart_button = pygame.Rect(
                    WIDTH // 2 - 70, HEIGHT // 2 + 60, 150, 50)
                home_button = pygame.Rect(
                    WIDTH // 2 - 70, HEIGHT // 2 + 120, 150, 50)
                quit_button = pygame.Rect(
                    WIDTH // 2 - 70, HEIGHT // 2 + 180, 150, 50)
                if resume_button.collidepoint(mouse_x, mouse_y):
                    start_time += time.time() - pause_start_time
                    game_state = PLAYING
                if restart_button.collidepoint(mouse_x, mouse_y):
                    start_time = time.time()
                    pause_start_time = 0
                    elapsed_time = 0
                    player_speed = 5
                    game_state = PLAYING
                    play_sound("./assets/sounds/SUIII.mp3", 0, 1)
                    for sprite in all_sprites:
                        sprite.kill()
                    player.__init__()
                    all_sprites.add(player)
                    player_group.add(player)
                if home_button.collidepoint(mouse_x, mouse_y):
                    pause_start_time = 0
                    elapsed_time = 0
                    player_speed = 5
                    game_state = START_MENU
                    for sprite in all_sprites:
                        sprite.kill()
                    player.__init__()
                    all_sprites.add(player)
                    player_group.add(player)
                if quit_button.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit()
            # Response towards clicking a button on game over menu
            if game_state == GAME_OVER:
                restart_button = pygame.Rect(
                    WIDTH // 2 - 70, HEIGHT // 2 + 65, 150, 50)
                home_button = pygame.Rect(
                    WIDTH // 2 - 70, HEIGHT // 2 + 125, 150, 50)
                quit_button = pygame.Rect(
                    WIDTH // 2 - 70, HEIGHT // 2 + 185, 150, 50)
                if restart_button.collidepoint(mouse_x, mouse_y):
                    start_time = time.time()
                    pause_start_time = 0
                    elapsed_time = 0
                    player_speed = 5
                    game_state = PLAYING
                    play_sound("./assets/sounds/SUIII.mp3", 0, 1)
                    for sprite in all_sprites:
                        sprite.kill()
                    player.__init__()
                    all_sprites.add(player)
                    player_group.add(player)
                if home_button.collidepoint(mouse_x, mouse_y):
                    pause_start_time = 0
                    elapsed_time = 0
                    player_speed = 5
                    game_state = START_MENU
                    for sprite in all_sprites:
                        sprite.kill()
                    player.__init__()
                    all_sprites.add(player)
                    player_group.add(player)
                if quit_button.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit()
        # listen for keyboard input
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # If paused, play
            if game_state == PAUSED:
                start_time += time.time() - pause_start_time
                game_state = PLAYING
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if game_state == PLAYING:
                pause_start_time = time.time()
                game_state = PAUSED
            elif game_state == PAUSED:
                pygame.quit()
                sys.exit()
            elif game_state == START_MENU:
                pygame.quit()
                sys.exit()
            elif game_state == GAME_OVER:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            if game_state == START_MENU:
                start_time = time.time()
                game_state = PLAYING
            if game_state == PAUSED:
                start_time += time.time() - pause_start_time
                game_state = PLAYING
            if game_state == GAME_OVER:
                start_time = time.time()
                pause_start_time = 0
                elapsed_time = 0
                player_speed = 5
                game_state = PLAYING
                play_sound("./assets/sounds/SUIII.mp3", 0, 1)
                for sprite in all_sprites:
                    sprite.kill()
                player.__init__()
                all_sprites.add(player)
                player_group.add(player)
    # Update game state
    if game_state == START_MENU:
        start_menu()
    elif game_state == PLAYING:
        elapsed_time = time.time() - start_time
        play_game()
    elif game_state == PAUSED:
        pause_menu()
    elif game_state == GAME_OVER:
        game_over_menu()

    pygame.display.flip()
    clock.tick(FPS)
