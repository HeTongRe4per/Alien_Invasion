import pygame
from bullet import Bullet
from enemy import Enemy

# 新增的Retry按钮类
class Button:
    def __init__(self, screen, text, x, y, width, height, inactive_color, active_color, action=None):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.action = action

    def draw(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            pygame.draw.rect(self.screen, self.active_color, (self.x, self.y, self.width, self.height))
            if click[0] == 1 and self.action is not None:
                self.action()
        else:
            pygame.draw.rect(self.screen, self.inactive_color, (self.x, self.y, self.width, self.height))

        font = pygame.font.SysFont('Comic Sans MS', 20)
        text = font.render(self.text, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        self.screen.blit(text, text_rect)


def check_events(player, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(player.screen, player))
    return True


def update_bullets(bullets):
    for bullet in bullets[:]:
        bullet.update()
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)


def update_enemies(enemies, enemy_bullets):
    for enemy in enemies[:]:
        enemy.update()
        if enemy.rect.top > enemy.screen.get_rect().bottom:
            enemies.remove(enemy)
        else:
            enemy.fire(enemy_bullets)


def update_enemy_bullets(enemy_bullets):
    for bullet in enemy_bullets[:]:
        bullet.update()
        if bullet.rect.top > bullet.screen.get_rect().bottom:
            enemy_bullets.remove(bullet)


def check_collisions(player, enemies, bullets, enemy_bullets, score, lives):
    player_rect = player.rect
    game_over = False

    for enemy in enemies[:]:
        if enemy.rect.colliderect(player_rect):
            lives -= 1
            enemies.remove(enemy)
            if lives <= 0:
                game_over = True

        for bullet in bullets[:]:
            if enemy.rect.colliderect(bullet.rect):
                score += 10  # 每击败一个敌人加10分
                enemies.remove(enemy)
                bullets.remove(bullet)
                break

    for bullet in enemy_bullets[:]:
        if bullet.rect.colliderect(player_rect):
            lives -= 1
            enemy_bullets.remove(bullet)
            if lives <= 0:
                game_over = True

    return score, lives, game_over


def update_screen(screen, player, bullets, enemies, enemy_bullets, background, score, font, lives, game_over, retry_button):
    screen.blit(background, (0, 0))
    player.blitme()
    for bullet in bullets:
        bullet.blitme()
    for enemy in enemies:
        enemy.blitme()
    for bullet in enemy_bullets:
        bullet.blitme()

    # 显示分数
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # 显示生命
    life_text = font.render(f"Life × {lives}", True, (0, 0, 0))
    screen.blit(life_text, (10, 50))

    # 显示游戏结束信息和Retry按钮
    if game_over:
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(screen.get_rect().centerx, screen.get_rect().centery - 50))
        screen.blit(game_over_text, text_rect)

        retry_button.draw()  # 绘制Retry按钮

    pygame.display.flip()
