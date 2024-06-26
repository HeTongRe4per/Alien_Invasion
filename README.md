
# 飞机大战游戏

本项目是一个简单的飞机大战游戏，使用Python和Pygame开发。

## 使用

### 源码安装

确保已经安装了Python和Pygame。运行以下命令安装依赖项：

1.  克隆本仓库

```commandline
git clone https://github.com/HeTongRe4per/Alien_Invasion.git
```

2. 安装Pygame库（如果尚未安装）。

```commandline
pip install pygame
```

### 源码运行

1. 进入项目目录。

```commandline
cd Alien_Invasion
```

2. 运行主程序。

```commandline
python main.py
```

### 直接运行

- 前往本仓库`[Release](https://github.com/HeTongRe4per/Alien_Invasion/releases)`下载`.zip`文件
- 解压缩，运行文件夹中`main.exe`

## 游戏截图

<p float="left">
    <img src="https://github.com/HeTongRe4per/imgurl/blob/main/Alien_Invasion/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-06-26%20142941.png?raw=true" width="265" />
    <img src="https://github.com/HeTongRe4per/imgurl/blob/main/Alien_Invasion/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-06-26%20142958.png?raw=true" width="265" />
    <img src="https://github.com/HeTongRe4per/imgurl/blob/main/Alien_Invasion/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-06-26%20143121.png?raw=true" width="265" /> 
</p>

## 操作方式

- 使用键盘上的方向键控制飞机的移动
- 空格键发射子弹。

## 游戏特性

- 玩家飞机可以左右移动，并能发射子弹击败敌人。
-敌人飞机随时间自动生成，并发射子弹攻击玩家。
- 分数根据击败敌人数量累计。
- 生命机制：游戏开始有3条生命，碰撞敌人或被敌人子弹击中会减少生命。
- 游戏结束：生命值归零时游戏结束，屏幕中央显示"Game Over"。

## 依赖项

- Python 3.x
- Pygame

## 文件结构

```
project/
│
├── main.py             # 游戏主程序
├── player.py           # 玩家飞机类
├── enemy.py            # 敌人飞机类
├── bullet.py           # 玩家子弹类
├── enemy_bullet.py     # 敌人子弹类
├── game_functions.py   # 游戏功能函数
├── settings.py         # 游戏设置和常量
├── images/             # 图片资源目录
│   ├── background.bmp
│   ├── player.bmp
│   ├── enemy.bmp
│   └── bullet.bmp
│
└── README.md           # 项目说明文件
```
