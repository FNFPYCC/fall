from ursina import *
from blocks import Voxel
from player import Player
from config import VERSION
import random

app = Ursina()

# Вывод версии игры
print(f"Starting Cosmic Voxel Game version {VERSION}")

# Генерация парящих островов
for island in range(5):  # 5 островов
    center = Vec3(random.randint(-10, 10), random.randint(0, 5), random.randint(-10, 10))
    for x in range(-2, 3):
        for y in range(-1, 2):
            for z in range(-2, 3):
                if random.random() > 0.3:  # Случайное размещение блоков
                    Voxel(position=center + Vec3(x, y, z), block_id=random.choice(["crystal", "neon"]))

# Создание игрока
player = Player()

# Освещение для эффекта свечения
Scene().ambient_color = color.rgba(0.2, 0.2, 0.3, 1)

app.run()