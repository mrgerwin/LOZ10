from pygame_functions7 import *
"""
1.7.1 Bug Fixes
Enemies don't glitch on turning
Enemies cannot leave scene
Enemies are taken out of enemies list when killed
Constants for screensize used instead of numbers for readability
"""


tile_size = 32
screen_width=tile_size*32
screen_height=tile_size*24

screenSize(screen_width,screen_height)
setAutoUpdate(False)
link = Player()
sword = Sword(link)

scene1 = Scene(link, "ZeldaMapTilesBrown.png", "map.txt", 6,8)
showBackground(scene1)

showSprite(link)
for enemy in scene1.Enemies:
    showSprite(enemy)

nextFrame = clock()
frame = 0

while True:
    if clock() >nextFrame:
        frame= (frame + 1)%2
        nextFrame += 80
        pause(10)
        
        for wall in scene1.Wall_Tiles:
            if touching(wall, link):
                link.speed = -link.speed
                link.move(frame)
                link.speed = - link.speed
        
        if keyPressed("down"):
            
            link.orientation =0
            link.move(frame)
        elif keyPressed("up"):
            link.orientation =1
            link.move(frame)
        elif keyPressed("right"):
            link.orientation =2
            link.move(frame)
        elif keyPressed("left"):
            link.orientation =3
            link.move(frame)
        elif keyPressed("space"):
            changeSpriteImage(link, link.orientation + 8)
        #Sword Swing Code
            sword.swing()
            for enemy in scene1.Enemies:
                if touching(sword, enemy):
                    if enemy.health == 1:
                        scene1.Enemies.remove(enemy)
                    enemy.hit()
        if not keyPressed("space") or keyPressed("left") or keyPressed("right") or keyPressed("up") or keyPressed("down"):
            hideSprite(sword)
        if keyPressed("h"):
            changeSpriteImage(link, frame+12)
        
        for enemy in scene1.Enemies:
            enemy.move(frame)            
            if touching(enemy, link):
                link.hit()
            for wall in scene1.Wall_Tiles:
                while touching(enemy, wall) or enemy.rect.x > screen_width or enemy.rect.y>screen_height or enemy.rect.x<0 or enemy.rect.y<0:
                    enemy.turn()
                    enemy.move(frame)
                    
        updateDisplay()

endWait()