import pygame
# from . import pygame_functions

pygame.init()

#SOUND SETUP
music = pygame.mixer.music.load('AM_Assets/35_Lost_Woods.mp3')
# music volume control between 0 and 1
pygame.mixer.music.set_volume(.2)
# play music on infinite loop
pygame.mixer.music.play(-1)

screen_width = 928
screen_height = 593
win = pygame.display.set_mode((screen_width, screen_height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
clock = pygame.time.Clock()

pygame.display.set_caption("Arrow_Man")

# load in the background images
bg = [pygame.image.load('AM_Assets/Layer_0000_9.png').convert_alpha(), pygame.image.load('AM_Assets/Layer_0001_8.png').convert_alpha(),
      pygame.image.load('AM_Assets/Layer_0002_7.png').convert_alpha(),
      pygame.image.load('AM_Assets/Layer_0003_6.png').convert_alpha(), pygame.image.load('AM_Assets/Layer_0004_Lights.png').convert_alpha(),
      pygame.image.load('AM_Assets/Layer_0005_5.png').convert_alpha(),
      pygame.image.load('AM_Assets/Layer_0006_4.png').convert_alpha(), pygame.image.load('AM_Assets/Layer_0007_Lights.png').convert_alpha(),
      pygame.image.load('AM_Assets/Layer_0008_3.png').convert_alpha(),
      pygame.image.load('AM_Assets/Layer_0009_2.png').convert_alpha(), pygame.image.load('AM_Assets/Layer_0010_1.png').convert_alpha()]

bga = [0,0,0,0,0,0,0,0,0,0,0]
bgx = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(11):
    bgx[i] = bg[i].get_width()

bgb = [928,928,928,928,928,928,928,928,928,928,928]


bg0a = 0
bg0b = bg[0].get_width()
bg1a = 0
bg1b = bg[1].get_width()
bg2a = 0
bg2b = bg[2].get_width()
bg3a = 0
bg3b = bg[3].get_width()
bg4a = 0
bg4b = bg[4].get_width()
bg5a = 0
bg5b = bg[5].get_width()
bg6a = 0
bg6b = bg[6].get_width()
bg7a = 0
bg7b = bg[7].get_width()
bg8a = 0
bg8b = bg[8].get_width()
bg9a = 0
bg9b = bg[9].get_width()
bg10a = 0
bg10b = bg[10].get_width()


class player(object):
    walkRight = [pygame.image.load('AM_Assets/R0.png'), pygame.image.load('AM_Assets/R1.png'),
                 pygame.image.load('AM_Assets/R2.png'),
                 pygame.image.load('AM_Assets/R3.png'), pygame.image.load('AM_Assets/R4.png'),
                 pygame.image.load('AM_Assets/R5.png'),
                 pygame.image.load('AM_Assets/R6.png'), pygame.image.load('AM_Assets/R7.png')]

    walkLeft = [pygame.image.load('AM_Assets/L0.png'), pygame.image.load('AM_Assets/L1.png'),
                 pygame.image.load('AM_Assets/L2.png'),
                 pygame.image.load('AM_Assets/L3.png'), pygame.image.load('AM_Assets/L4.png'),
                 pygame.image.load('AM_Assets/L5.png'),
                 pygame.image.load('AM_Assets/L6.png'), pygame.image.load('AM_Assets/L7.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x - 5, self.y, 32, 47)

    def draw(self, win):
        if self.walkCount + 1 >= 25:
            self.walkCount = 0
            #add this line so link doesn't dissapear for one frame
            link.draw(win)
        else:
            if not self.standing:
                if self.left:
                    #print a resized version of link walking left
                    win.blit(pygame.transform.scale(self.walkLeft[self.walkCount // 3],(32,47)), (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    # print a resized version of link walking right
                    win.blit(pygame.transform.scale(self.walkRight[self.walkCount // 3],(32,47)), (self.x, self.y))
                    self.walkCount += 1
            else:
                if self.right:
                    #print a resized version of link standing right
                    win.blit(pygame.transform.scale(self.walkRight[self.walkCount // 3], (32, 47)), (self.x, self.y))
                else:
                    #print a resized version of link standing left
                    win.blit(pygame.transform.scale(self.walkLeft[self.walkCount // 3],(32,47)), (self.x, self.y))
            self.hitbox = (self.x - 5, self.y, 45, 52)
            # this line will enable the hitbox
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):

        self.isHit = True
        self.isJump = False
        self.jumpCount = 10
        self.x = 50
        self.y = 240
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        # text = font1.render('-10', 1, (255,0,0))
        # win.blit(text, ((screen_width/2 - (text.get_width()/2)),210))
        # pygame.display.update()
        # reset the jump count on being hit

        # add a delay so that the message stays on the screen
        i = 0
        while i < 100:
            pygame.time.delay(10)
            i += 1
            # add this block of code so you can still quit the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 100
                    pygame.quit()



def redrawGameWindow():

    for x in reversed(range(11)):
        win.blit(bg[x], (int(bga[x]), -200))
        win.blit(bg[x], (int(bgb[x]), -200))

    link.draw(win)

    pygame.display.update()


#instantiate the player
link = player(400, 490, 32, 47)
#link = player(0, 100, 32, 47)



run = True
while run:

    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #set the movement keybindings
    keys = pygame.key.get_pressed()
    move_left = keys[pygame.K_a]
    move_right = keys[pygame.K_d]
    jump = keys[pygame.K_w]

    if move_left: #and link.x > link.vel:

        scroll_counter = 11
        for i in (range(11)):


            if bga[i] +scroll_counter >= int((bg[i].get_width())):
                bga[i] = int((bg[i].get_width() * -1))
            if bgb[i] +scroll_counter >= int((bg[i].get_width())):
                bgb[i] = int((bg[i].get_width() * -1))
            bga[i] += scroll_counter
            bgb[i] += scroll_counter

            if i == 0:
                print("this is bga of 0", " LEFT ", bga[i], "scroll counter =", scroll_counter)
                print("this is bgb of 0", " LEFT ", bgb[i], "scroll counter =", scroll_counter)
            scroll_counter -= 1


        #link.x -= link.vel
        link.left = True
        link.right = False
        link.standing = False

    elif move_right: #and link.x < screen_width - link.width - link.vel:

        scroll_counter = 11
        for i in range(11):



            if bga[i] - scroll_counter <= int((bg[i].get_width()) * -1):
                bga[i] = int(bg[i].get_width())
            if bgb[i] - scroll_counter <= int((bg[i].get_width()) * -1):
                bgb[i] = int(bg[i].get_width())
            bga[i] -= scroll_counter
            bgb[i] -= scroll_counter

            if i == 0:
                print("this is bga of 0", " RIGHT ", bga[i], "scroll counter =", scroll_counter)
                print("this is bgb of 0", " RIGHT ", bgb[i], "scroll counter =", scroll_counter)
            scroll_counter -= 1



        """
        bg0a -= 6.4
        bg0b -= 6.4
        bg1a -= 5.8
        bg1b -= 5.8
        bg2a -= 5.2
        bg2b -= 5.2
        bg3a -= 4.6
        bg3b -= 4.6
        bg4a -= 4.0
        bg4b -= 4.0
        bg5a -= 3.4
        bg5b -= 3.4
        bg6a -= 2.8
        bg6b -= 2.8
        bg7a -= 2.2
        bg7b -= 2.2
        bg8a -= 1.6
        bg8b -= 1.6
        bg9a -= 1.2
        bg9b -= 1.2
        bg10a -= 1
        bg10b -= 1
        if bg0a < (bg[0].get_width()-5) * -1:
            bg0a = bg[0].get_width()
        if bg0b < (bg[0].get_width()-5) * -1:
            bg0b = bg[0].get_width()

        if bg1a < (bg[1].get_width()-5) * -1:
            bg1a = bg[1].get_width()
        if bg1b < (bg[1].get_width()-5) * -1:
            bg1b = bg[1].get_width()

        if bg2a < (bg[2].get_width()-5) * -1:
            bg2a = bg[2].get_width()
        if bg2b < (bg[2].get_width()-5) * -1:
            bg2b = bg[2].get_width()

        if bg3a < (bg[3].get_width()-5) * -1:
            bg3a = bg[3].get_width()
        if bg3b < (bg[3].get_width()-5) * -1:
            bg3b = bg[3].get_width()

        if bg4a < (bg[4].get_width()-5) * -1:
            bg4a = bg[4].get_width()
        if bg4b < (bg[4].get_width()-5) * -1:
            bg4b = bg[4].get_width()

        if bg5a < (bg[5].get_width()-5) * -1:
            bg5a = bg[5].get_width()
        if bg5b < (bg[5].get_width()-5) * -1:
            bg5b = bg[5].get_width()

        if bg6a < (bg[6].get_width()-5) * -1:
            bg6a = bg[6].get_width()
        if bg6b < (bg[6].get_width()-5) * -1:
            bg6b = bg[6].get_width()

        if bg7a < (bg[7].get_width()-5) * -1:
            bg7a = bg[7].get_width()
        if bg7b < (bg[7].get_width()-5) * -1:
            bg7b = bg[7].get_width()

        if bg8a < (bg[8].get_width()-5) * -1:
            bg8a = bg[8].get_width()
        if bg8b < (bg[8].get_width()-5) * -1:
            bg8b = bg[8].get_width()

        if bg9a < (bg[9].get_width()-5) * -1:
            bg9a = bg[9].get_width()
        if bg9b < (bg[9].get_width()-5) * -1:
            bg9b = bg[9].get_width()

        if bg10a < (bg[10].get_width()-5) * -1:
            bg10a = bg[10].get_width()
        if bg10b < (bg[10].get_width()-5) * -1:
            bg10b = bg[10].get_width()
        """


        #link.x += link.vel
        link.left = False
        link.right = True
        link.standing = False
    else:
        link.standing = True
        link.walkCount = 0

    if not link.isJump:
        # if up and y > vel:
        #    y -= vel
        # if down and y < screen_width - height - vel:
        #    y += vel
        if jump:
            # megaman.left = False
            # megaman.right = False
            link.isJump = True
            link.walkCount = 0

    else:
        # else if you are jumping do the following
        # set the negative so that the character comes back down from the jump
        if link.jumpCount >= -10:
            neg = 1
            if link.jumpCount < 0:
                neg = -1
            # set the y coordinate during the jump
            link.y -= (link.jumpCount ** 2) / 6 * neg
            link.jumpCount -= 1
        else:
            link.isJump = False
            link.jumpCount = 10


    # set game to run at 27 fps
    redrawGameWindow()

pygame.quit()

