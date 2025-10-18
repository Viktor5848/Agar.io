from pygame import *
init()
from random import randint
window=display.set_mode((1380,710))
display.set_caption("Agar.io")

window.fill((1, 0, 19))
clock=time.Clock()

main_player=[500,500,50]
players=[]

class food:
    def __init__(self,x,y,r,c):
        self.x=x
        self.y=y
        self.radius=r
        self.color=c
        draw.circle(window,self.color,(self.x,self.y),self.radius)
def check_collision(x1,y1,r1,x2,y2,r2):
    distance=((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return distance < r1 + r2
foods=[food(randint(0,1380),randint(0,710),randint(5,15),(randint(0,255),randint(0,255),randint(0,255)))]
for i in range(100):
    foods.append(food(randint(0,1380),randint(0,710),randint(5,15),(randint(0,255),randint(0,255),randint(0,255))))

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
    
    window.fill((1, 0, 19))
    draw.circle(window, (255, 0, 0), (main_player[0], main_player[1]), main_player[2])
    
    keys = key.get_pressed()
    if keys[K_w]:
        main_player[1] -= 12
    if keys[K_s]:
        main_player[1] += 12
    if keys[K_a]:
        main_player[0] -= 12
    if keys[K_d]:
        main_player[0] += 12

    display.update()
    clock.tick(60)


    