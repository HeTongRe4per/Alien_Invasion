import pygame
import random
from settings import *
from player import Player
from enemy import Enemy
import game_functions as gf


def main():
    # 初始化Pygame
    pygame.init()

    # 设置窗口
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("飞机大战")

    # 加载背景图片
    background = pygame.image.load(background_image_path)

    # 创建玩家
    player = Player(screen)
    lives = initial_lives

    # 子弹列表
    bullets = []

    # 敌人列表
    enemies = []

    # 敌人子弹列表
    enemy_bullets = []

    # 分数
    score = 0
    font = pygame.font.SysFont('Comic Sans MS', 25)

    # Retry按钮
    retry_button = gf.Button(screen, "Retry", 200, 400, 100, 50, (0, 255, 0), (0, 200, 0), main)

    # 设置时钟
    clock = pygame.time.Clock()

    # 敌人生成控制变量
    enemy_spawn_thresholds = [100, 300, 1000, 2000]
    next_enemy_threshold_index = 0  # 初始为0，表示使用第一个阈值
    enemy_spawn_rate = 100

    # 游戏运行状态
    running = True
    game_over = False  # 新增游戏结束状态变量

    # 主循环
    while running:
        # 处理事件
        running = gf.check_events(player, bullets)

        # 更新玩家位置
        player.update()

        # 更新子弹位置
        gf.update_bullets(bullets)

        # 根据分数调整敌人生成频率和阈值
        if score >= enemy_spawn_thresholds[next_enemy_threshold_index] and next_enemy_threshold_index < len(
                enemy_spawn_thresholds) - 1:
            enemy_spawn_rate //= 2  # 敌人生成频率减半
            next_enemy_threshold_index += 1  # 更新阈值索引

        # 添加敌人
        if random.randint(1, enemy_spawn_rate) == 1:
            enemies.append(Enemy(screen))

        # 更新敌人位置并发射子弹
        gf.update_enemies(enemies, enemy_bullets)

        # 更新敌人子弹位置
        gf.update_enemy_bullets(enemy_bullets)

        # 检测碰撞并更新分数和生命
        score, lives, game_over = gf.check_collisions(player, enemies, bullets, enemy_bullets, score, lives)

        # 绘制场景
        gf.update_screen(screen, player, bullets, enemies, enemy_bullets, background, score, font, lives, game_over, retry_button)

        clock.tick(60)

        # 控制帧率
        clock.tick(60)

        # 如果游戏结束，等待用户点击Retry按钮再重新开始
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if retry_button.x + retry_button.width > event.pos[0] > retry_button.x and retry_button.y + retry_button.height > event.pos[1] > retry_button.y:
                        # 重新初始化游戏状态
                        lives = initial_lives
                        bullets.clear()
                        enemies.clear()
                        enemy_bullets.clear()
                        score = 0
                        game_over = False
                        break

    # 退出Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
