from pygame import *
from random import randint

init()
WIDTH, HEIGHT = 1380, 710
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Agar.io")

clock = time.Clock()

BG_COLOR = (1, 0, 19)

# головний гравець
main_player = {"x": 0, "y": 0, "radius": 50, "color": (255, 0, 0)}

class Food:
    def __init__(self, x, y, r, c):
        self.x = x
        self.y = y
        self.radius = r
        self.color = c

    def draw(self, surface, offset_x, offset_y, scale):
        draw.circle(surface, self.color, 
                    (int((self.x - offset_x) * scale + WIDTH//2), 
                     int((self.y - offset_y) * scale + HEIGHT//2)), 
                    max(1, int(self.radius * scale)))

# створюємо багато їжі
foods = [Food(randint(-2000, 2000), randint(-2000, 2000), randint(5, 15), 
              (randint(0,255), randint(0,255), randint(0,255))) for _ in range(500)]

SPEED = 12

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    keys = key.get_pressed()
    dx = dy = 0
    if keys[K_w]:
        dy = -SPEED
    if keys[K_s]:
        dy = SPEED
    if keys[K_a]:
        dx = -SPEED
    if keys[K_d]:
        dx = SPEED

    main_player["x"] += dx
    main_player["y"] += dy

    # масштабування без обмежень
    scale = 50 / main_player["radius"]  

    window.fill(BG_COLOR)

    # малюємо їжу з масштабом
    for f in foods:
        f.draw(window, main_player["x"], main_player["y"], scale)

    # перевірка поглинання їжі
    for f in foods[:]:
        dist_sq = (f.x - main_player["x"])**2 + (f.y - main_player["y"])**2
        if dist_sq <= (f.radius + main_player["radius"])**2:
            main_player["radius"] += f.radius * 0.3
            foods.remove(f)
            foods.append(Food(randint(-2000, 2000), randint(-2000, 2000), randint(5, 15), 
                              (randint(0,255), randint(0,255), randint(0,255))))

    # малюємо головного гравця з масштабом
    draw.circle(window, main_player["color"], (WIDTH//2, HEIGHT//2), int(main_player["radius"] * scale))

    display.update()
    clock.tick(60)
