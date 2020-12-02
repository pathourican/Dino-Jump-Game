# Patrick Hourican pjh4as CS1111

import pygame
import gamebox
import random

camera = gamebox.Camera(800,600)
dino = gamebox.from_color(200,200,"white",40,50)
ground = gamebox.from_color(400,600,"tan",800,200)
sky = gamebox.from_color(400,300,"blue",800,600)
dirt = gamebox.from_image(600,random.randint(500,550), "http://wiki.pixbits.com/images/3/35/Small_Rock.png")
dirt2 = gamebox.from_image(100,random.randint(500,550), "http://wiki.pixbits.com/images/3/35/Small_Rock.png")
cact_height = random.randint(100,125)
cact_width = random.randint(40,60)
cact= gamebox.from_color(900,475,"green",cact_width,cact_height)
cact2_height = random.randint(125,150)
cact2_width = random.randint(40,60)
cact2 = gamebox.from_color(1400,475,"green",cact2_width,cact2_height)

cloud = gamebox.from_image(100, random.randint(95,100), "http://www.i2clipart.com/cliparts/f/2/2/5/128045f22582cb2b04dc4441532b33fb8750ad.png")
cloud2 = gamebox.from_image(700, random.randint(95,100), "http://www.i2clipart.com/cliparts/f/2/2/5/128045f22582cb2b04dc4441532b33fb8750ad.png")

dino.yspeed = 0
score = 0
game_on = True

camera.clear('black')

def cactus_move():
    # Has each cactus move and relocate to a different space on he right edge of the screen
    # to continue in the cycle of moving across the screen.

    cact.x -= 7
    cact2.x -= 7

    if cact.x <= 0:
        cact.x = random.randint(1000,1200)
    if cact2.x <= 0:
        cact2.x = random.randint(1000, 1200)
    if cact.touches(cact2):
        cact2.x +=200
    if abs(cact.x-cact2.x) < 200:
        cact2.x += 200

def dirt_move():
    # Each dirt image moves across the screen and relocates to a random x location on the
    # right edge of the screen, while the y location is randomly change by a value between
    # -10 and 5.

    dirt.x -= 7
    dirt2.x -= 7

    if dirt.x <= 0:
        dirt.x += random.randint(1000, 1400)
        dirt.y = random.randint(515,550)
    if dirt2.x <= 0:
        dirt2.x += random.randint(1000, 1400)
        dirt2.y = random.randint(515,550)
    if dirt.touches(dirt2):
        dirt2.x += 200
    if abs(dirt.x-dirt2.x) < 100:
        dirt2.x += 200

def cloud_move():
    # The clouds each move at a slower speed than the other sprites, relocating from the left
    # edge to a random location on the right edge of the screen, and changing the y location
    # by a random value.

    cloud.x -= 1
    cloud2.x -= 1

    if cloud.x <= 0:
        cloud.x = random.randint(1000, 1200)
        cloud.y += random.randint(-10,5)
    if cloud2.x <= 0:
        cloud2.x = random.randint(1400, 1600)
        cloud2.y += random.randint(-10,5)
    if cloud.touches(cloud2):
        cloud2.x += 200
    if abs(cloud.x-cloud2.x) < 100:
        cloud2.x += 200

def dino_move(keys):
    # Dino jumps up at a constant speed when the space bar is pressed
    # and accelerates downward due to "gravity".

    dino.move_to_stop_overlapping(ground)

    if pygame.K_SPACE in keys and dino.touches(ground):
        dino.speedy = -25
    dino.speedy +=1
    dino.y += dino.speedy


def tick(keys):
    global score
    global game_on
    global cact
    global cact2
    global dirt
    global dirt2
    global cloud
    global cloud2
    global dino
    global ground
    global sky

    if game_on:
        score += 1
        display_score = gamebox.from_text(715, 25, "Score: " + str(score), 40, "white")



        cloud_move()
        dirt_move()
        cactus_move()
        dino_move(keys)

        camera.draw(sky)
        camera.draw(cloud)
        camera.draw(cloud2)
        camera.draw(cact)
        camera.draw(cact2)
        camera.draw(dino)
        camera.draw(ground)
        camera.draw(dirt)
        camera.draw(dirt2)
        camera.draw(display_score)
        camera.display()

    if dino.touches(cact):
        camera.draw(gamebox.from_text(400, 300, 'You Lose', 42, 'white', True))
        camera.display()
        game_on = False

    if dino.touches(cact2):
        camera.draw(gamebox.from_text(400, 300, 'You Lose', 42, 'white', True))
        camera.display()
        game_on = False

    if pygame.K_SPACE in keys and dino.touches(cact):
        game_on = True

        dino = gamebox.from_color(200, 200, "white", 40, 50)
        ground = gamebox.from_color(400, 600, "tan", 800, 200)
        sky = gamebox.from_color(400, 300, "blue", 800, 600)
        dirt = gamebox.from_image(600, random.randint(500, 550), "http://wiki.pixbits.com/images/3/35/Small_Rock.png")
        dirt2 = gamebox.from_image(100, random.randint(500, 550), "http://wiki.pixbits.com/images/3/35/Small_Rock.png")
        cact_height = random.randint(100, 125)
        cact_width = random.randint(40, 60)
        cact = gamebox.from_color(900, 475, "green", cact_width, cact_height)
        cact2_height = random.randint(125, 150)
        cact2_width = random.randint(40, 60)
        cact2 = gamebox.from_color(1400, 475, "green", cact2_width, cact2_height)

        cloud = gamebox.from_image(100, random.randint(95, 100),
                                   "http://www.i2clipart.com/cliparts/f/2/2/5/128045f22582cb2b04dc4441532b33fb8750ad.png")
        cloud2 = gamebox.from_image(700, random.randint(95, 100),
                                    "http://www.i2clipart.com/cliparts/f/2/2/5/128045f22582cb2b04dc4441532b33fb8750ad.png")

        score = 0

    if pygame.K_SPACE in keys and dino.touches(cact2):
        game_on = True

        dino = gamebox.from_color(200, 200, "white", 40, 50)
        ground = gamebox.from_color(400, 600, "tan", 800, 200)
        sky = gamebox.from_color(400, 300, "blue", 800, 600)
        dirt = gamebox.from_image(600, random.randint(500, 550), "http://wiki.pixbits.com/images/3/35/Small_Rock.png")
        dirt2 = gamebox.from_image(100, random.randint(500, 550), "http://wiki.pixbits.com/images/3/35/Small_Rock.png")
        cact_height = random.randint(100, 125)
        cact_width = random.randint(40, 60)
        cact = gamebox.from_color(900, 475, "green", cact_width, cact_height)
        cact2_height = random.randint(125, 150)
        cact2_width = random.randint(40, 60)
        cact2 = gamebox.from_color(1400, 475, "green", cact2_width, cact2_height)

        cloud = gamebox.from_image(100, random.randint(95, 100),
                                   "http://www.i2clipart.com/cliparts/f/2/2/5/128045f22582cb2b04dc4441532b33fb8750ad.png")
        cloud2 = gamebox.from_image(700, random.randint(95, 100),
                                    "http://www.i2clipart.com/cliparts/f/2/2/5/128045f22582cb2b04dc4441532b33fb8750ad.png")

        score = 0

gamebox.timer_loop(144,tick)