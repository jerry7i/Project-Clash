"""
Created by Jerry Li
May 4, 2018
This module contains all the sprites used in the Project Clash game. It uses
the pygame module as well as the random module to initialize the sprites. It
includes the character sprits, label sprites, invisible sprites for hit detection,
the background sprite, and health and chakra bar sprites.
v1.6
"""

import pygame, random

# menu and background sprites

class MenuButton(pygame.sprite.Sprite):
    """
    The MenuButton class inherites from the sprite class. This class defines the
    sprite for a botton on the menu. This sprite is not visible.
    """
    def __init__(self, screen, pos, name):
        """
        This initializer takes screen and a xy tupple as parameters
        to initialize the image and rect attributes.
        """
        # call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # set the image and rect attributes
        if name == "play":
            self.image = pygame.Surface((160, 160))
        elif name == "controls":
            self.image = pygame.Surface((185,190))
        elif name == "help":
            self.image = pygame.Surface((50,50))
            
        #self.image.fill((255,0,0))
        
        self.rect = self.image.get_rect()
        self.rect.center = (pos)
        
class Click(pygame.sprite.Sprite):
    """
    The Click class inherites from the sprite class. This class defines the sprite
    that appears at the location of the mouse and is used to detect user input.
    """
    def __init__(self, pos):
        """
        This initializer takes an xy coordinate tupple as parameters and it 
        initialize the image and rect attributes.
        """    
        # call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)    
        
        # initialize image and rect attributes
        self.image = pygame.Surface((1,1))
        
        self.rect = self.image.get_rect()
        self.rect.center = pos
        
class Background(pygame.sprite.Sprite):
    """
    The Background class inherites from the sprite class. This class defines the
    sprite for the background of the game.
    """
    def __init__(self, screen, randNum):
        """
        This initializer takes screen and a random integer as parameters and
        it initialize the image and rect attributes for the background.
        """
        # call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)    
        
        # initialize image and rect attributes
        # 3 different backgrounds
        self.image = pygame.image.load("./Backgrounds/Battleground" + str(randNum) + ".png").convert()
        
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = -200
    
# player and hitbox sprites

class Naruto(pygame.sprite.Sprite):
    """
    The Naruto class inherits from the sprite class. This class defines the 
    sprite for the Naruto graphics.
    """
    def __init__(self, screen, player):
        """
        This initializer takes the screen and player as a parameter and uses 
        that to initialize the rect and image attributes. It also sets all the
        attributes that keep track of player animations, status, and movement.
        """
        # call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # define the image and rect attributes for the player
        # R means images facing right and L means images facing left
        self.__standingImagesR = []
        for imageNum in range(1,5):
            self.__standingImagesR.append(pygame.image.load("./Naruto/Standing"\
                                            + str(imageNum) + ".png").convert())
            
        self.__standingImagesL = []
        for imageNum in range(4):
            self.__standingImagesL.append(pygame.transform.flip \
                                          (self.__standingImagesR[imageNum], True, False))
        
        # seperate check for direction is done for walking images
        self.__walkingImages = []
        for imageNum in range(2,8):
            self.__walkingImages.append(pygame.image.load("./Naruto/Walking"\
                                            + str(imageNum) + ".png").convert())
        
        # flinching images 
        self.__flinchingImagesR = []
        for imageNum in range(1,3):
            self.__flinchingImagesR.append(pygame.image.load("./Naruto/Flinching" \
                                            + str(imageNum) + ".png").convert())
            
        self.__flinchingImagesL = []
        for imageNum in range(2):
            self.__flinchingImagesL.append(pygame.transform.flip \
                                         (self.__flinchingImagesR[imageNum], True, False))
        
        # falling images   
        self.__fallingImagesR = []
        for imageNum in range(1, 10):
            self.__fallingImagesR.append(pygame.image.load("./Naruto/Falling" \
                                            + str(imageNum) + ".png").convert())
            
        self.__fallingImagesL = []
        for imageNum in range(9):
            self.__fallingImagesL.append(pygame.transform.flip \
                                         (self.__fallingImagesR[imageNum], True, False))
        
        # attacking images
        self.__punchingImagesR = []
        for imageNum in range(1,4):
            self.__punchingImagesR.append(pygame.image.load("./Naruto/Punching"\
                                            + str(imageNum) + ".png").convert())
            
        self.__punchingImagesL = []
        for imageNum in range(3):
            self.__punchingImagesL.append(pygame.transform.flip \
                                          (self.__punchingImagesR[imageNum], True, False))        
            
        self.__headbuttImagesR = []
        for imageNum in range(1,5):
            self.__headbuttImagesR.append(pygame.image.load("./Naruto/Headbutting"\
                                            + str(imageNum) + ".png").convert())
            
        self.__headbuttImagesL = []
        for imageNum in range(4):
            self.__headbuttImagesL.append(pygame.transform.flip \
                                          (self.__headbuttImagesR[imageNum], True, False))        
            
        self.__strongPunchImagesR = []
        for imageNum in range(1,5):
            self.__strongPunchImagesR.append(pygame.image.load("./Naruto/StrongPunch" \
                                            + str(imageNum) + ".png").convert())
            
        self.__strongPunchImagesL = []
        for imageNum in range(4):
            self.__strongPunchImagesL.append(pygame.transform.flip \
                                          (self.__strongPunchImagesR[imageNum], True, False))        
            
        self.__throwingImagesR = []
        for imageNum in range(1,4):
            self.__throwingImagesR.append(pygame.image.load("./Naruto/Throwing" \
                                            + str(imageNum) + ".png").convert())      
            
        self.__throwingImagesL = []
        for imageNum in range(3):
            self.__throwingImagesL.append(pygame.transform.flip \
                                          (self.__throwingImagesR[imageNum], True, False))        
            
        self.image = self.__standingImagesR[0]
        
        # place the character on the correct side of the screen
        if player == 1:
            self.rect = self.image.get_rect()
            self.rect.center = (screen.get_width()/4, screen.get_height()/2 + 100)
            self.__facing = "right"
        else:
            self.rect = self.image.get_rect()
            self.rect.center = (screen.get_width() * 3/4, screen.get_height()/2 + 100)
            self.__facing = "left"
        
        # set direction and status attributes    
        self.__dy = 0
        self.__dx = 0
        self.__move = True
        self.__goUp = False
        self.__goDown = False
        self.__goRight = False
        self.__goLeft = False
        self.__punching = False
        self.__throwing = False
        self.__flinching = False
        self.__fallen = False
        self.__randAttack = 0
        self.__randFlinch = 0
        
        # list of images used to change the image attribute
        self.__standingImages = []
        self.__fallingImages = []
        self.__flinchingImages = []
        self.__punchingImages = []
        self.__strongPunchImages = []
        self.__headbuttImages = []
        self.__throwingImages = []
        
        # attributtes used to cycle through lists of images
        self.__standImageNum = 0
        self.__walkImageNum = 0
        self.__punchImageNum = 0
        self.__strongImageNum = 0
        self.__headbuttImageNum = 0
        self.__throwImageNum = 0
        self.__fallImageNum = 0
        
        # attributes used to control walking and duration of flinch
        self.__decreasing = False
        self.__timer = 0
        self.__screen = screen
        
    def changeDirection(self, direction, stop):
        """
        This method uses the parameters keyPress and stop (a boolean value) to
        change the player's direction and stop in any direction when needed.
        """
        # check the direction of the key that has been pressed
        if not stop:
            if direction == "up":
                self.__goUp = True
                self.__goDown = False
            elif direction == "down":
                self.__goDown = True
                self.__goUp = False
            elif direction == "left":
                self.__goLeft = True
                self.__goRight = False
            else:
                self.__goRight = True
                self.__goLeft = False
        
        # when stop is True, check the direction of the key that has been lifted
        else:
            if direction == "up":
                self.__goUp = False
            elif direction == "down":
                self.__goDown = False
            elif direction == "left":
                self.__goLeft = False
            else:
                self.__goRight = False
        
        # change direction based on direction variables
        if self.__goUp:
            self.__dy = -1
        elif self.__goDown:
            self.__dy = 1
        else:
            self.__dy = 0
        if self.__goLeft:
            self.__dx = -1
        elif self.__goRight:
            self.__dx = 1
        else:
            self.__dx = 0
            
        # reset variable for displaying images
        if stop == False:
            self.__walkImageNum = 0
            self.__decreasing = False
            
        if self.__dx == 0 and self.__dy == 0:
            self.__standImageNum = 0

    def punch(self, punch):
        """
        This method takes punch, a boolean value, as a parameter and changes the
        punching attribute using it. It also resets the attributes for 
        cycling through images and assigns a random value to the randAttack
        attribute.
        """
        self.__punching = punch
        
        if punch:
            self.__punchImageNum = 0
            self.__strongImageNum = 0
            self.__headbuttImageNum = 0        
            self.__randAttack = random.randrange(3)
            
    def throw(self, throw):
        """
        This method takes punch, a boolean value, as a parameter and changes the
        throwing attribute using it. It also resets the throwImageNum attribute
        to 0.
        """
        self.__throwing = throw
        self.__throwImageNum = 0
        
    def stayStill(self, stay):
        """
        This method keeps the player's rect from moving when stay = True 
        and allows the player to move when stay = False.
        """
        if stay:
            self.__move = False
        else:
            self.__move = True
            
    def flinch(self, flinch):
        """
        This method takes flinch, a boolean value, and changes the flinching
        attribute to the value of the flinch parameter. It also resets the timer
        attribute to 0 and assigns a random value to the randFlinch attribute.
        """        
        self.__flinching = flinch
        self.__timer = 0
        self.__randFlinch = random.randrange(2)
        
    def fallDown(self, fallen):
        """
        This method takes fallen, a boolean value, and changes the fallen
        attribute using the value of the fallen parameter
        """
        self.__fallen = fallen
        
    def changeOrientation(self, orientation):
        """
        This method takes orientation, a string value, and changes the facing
        attribute. It also changes the set of images the sprite will cycle 
        through depending on the direction they're facing and the status
        of the sprite.
        """
        if orientation == "right":
            self.__standingImages = self.__standingImagesR
            # set the images for an action at the beginning of a round when punchingImages is empty
            if not self.__punching or self.__punchingImages == []:
                self.__punchingImages = self.__punchingImagesR
                self.__strongPunchImages = self.__strongPunchImagesR
                self.__headbuttImages = self.__headbuttImagesR
                # only if the player isn't punching, change the facing attribute
                self.__facing = orientation
            if not self.__throwing or self.__throwingImages == []:
                self.__throwingImages = self.__throwingImagesR
            if not self.__fallen:
                self.__fallingImages = self.__fallingImagesR
            if not self.__flinching:
                self.__flinchingImages = self.__flinchingImagesR
                
        if orientation == "left":
            self.__standingImages = self.__standingImagesL
            if not self.__punching or self.__punchingImages == []:
                self.__punchingImages = self.__punchingImagesL
                self.__strongPunchImages = self.__strongPunchImagesL
                self.__headbuttImages = self.__headbuttImagesL
                
                self.__facing = orientation
            if not self.__throwing or self.__throwingImages == []:
                self.__throwingImages = self.__throwingImagesL   
            if not self.__fallen:
                self.__fallingImages = self.__fallingImagesL
            if not self.__flinching:
                self.__flinchingImages = self.__flinchingImagesL            
        
    def getPunching(self):
        """
        This method returns the punching attribute.
        """
        return self.__punching 
    
    def getThrowing(self):
        """
        This method returns the throwing attribute.
        """
        return self.__throwing
    
    def getFlinchStatus(self):
        """
        This method returns the flinching attribute.
        """
        return self.__flinching
        
    def getFallStatus(self):
        """
        This method returns the fallen attribute
        """
        return self.__fallen
    
    def getMoveStatus(self):
        """
        This method returns the move attribute.
        """
        return self.__move
    
    def getMove(self):
        """
        This method returns the move attribute.
        """
        return self.__move
    def getOrientation(self):
        """
        This method returns the facing attribute.
        """
        return self.__facing
    
    def update(self):
        """
        This method takes no parameters. It is automatically called to update
        the Player sprite on the screen and detect whether it has reached the 
        boundary on the screen. It also cycles through lists of images depending
        on the status of the character to animate its actions.
        """
        # if Naruto is standing still, ANIMATE HIM
        if (self.__dx == 0) and (self.__dy == 0) and self.__punching != True\
                                                 and self.__throwing != True\
                                                 and self.__fallen != True:
            
            # every 6 frames the image will change
            self.image = self.__standingImages[self.__standImageNum / 6]
            
            if self.__decreasing:
                self.__standImageNum -= 1
                if self.__standImageNum <= 0:
                    self.__decreasing = False
                    
            elif self.__decreasing == False:
                self.__standImageNum += 1
                # image moves every 6 frames so after 3 images start going back to the first
                if self.__standImageNum >= 6 * 3 + 5:
                    self.__decreasing = True  
                    
        if self.__move:
            # check if player has reached left or right of the screen
            if ((self.rect.centerx > 0) and (self.__dx < 0)) or \
               (self.rect.centerx < (self.__screen.get_width() - 30) and (self.__dx > 0)):
                
                # the player moves unless conditions change
                self.rect.left += self.__dx * 4
                
            if ((self.rect.centery > self.__screen.get_height()/2) and (self.__dy < 0)) or \
               (self.rect.bottom < self.__screen.get_height()) and ((self.__dy > 0)):
                
                self.rect.top += self.__dy * 4
            
            # WALKING ANIMATIONS
            if self.__dx != 0 or self.__dy != 0:
                
                # image is updated once every 5 frames
                self.image = self.__walkingImages[self.__walkImageNum / 5]
                if self.__facing == "left":
                    # flip image on x axis if facing left
                    self.image = pygame.transform.flip(self.image, True, False)
            
                # consider x direction before y direction
                if (self.__goLeft and self.__facing == "left") or \
                   (self.__goRight and self.__facing == "right"):
                    self.__walkImageNum += 1
                    # 6 images in 6 * 5 frames
                    if self.__walkImageNum >= 5 * 5:
                        self.__walkImageNum = 0
                    
                elif (self.__goRight and self.__facing == "left") or \
                     (self.__goLeft and self.__facing == "right"):
                    self.__walkImageNum -= 1
                    if self.__walkImageNum <= 0:
                        self.__walkImageNum = 5 * 5 
                        
                elif self.__dy > 0:
                    self.__walkImageNum += 1
                    if self.__walkImageNum >= 5 * 5:
                        self.__walkImageNum = 0
                        
                elif self.__dy < 0:
                    self.__walkImageNum -= 1
                    if self.__walkImageNum <= 0:
                        self.__walkImageNum = 5 * 5  
        
        # ANIMATE FALL    
        elif self.__fallen:
            self.image = self.__fallingImages[self.__fallImageNum / 10]
            
            if self.__fallImageNum != 8 * 10:
                self.__fallImageNum += 1
                
                if self.__fallImageNum % 5 == 0:
                    if self.__fallingImages == self.__fallingImagesR:
                        self.rect.left -= 5
                    else:
                        self.rect.left += 5                    
                
        # ANIMATE FLINCH
        elif self.__flinching:
            # changes the image to a random one of Naruto flinching
            self.image = self.__flinchingImages[self.__randFlinch]
            self.__timer += 1
            if self.__timer % 8 == 0:
                if self.__flinchingImages == self.__flinchingImagesR:
                    self.rect.left -= 3
                else:
                    self.rect.left += 3
            
        # ANIMATE PUNCH
        elif self.__punching:
            # three different attacks
            if self.__randAttack == 0:
                self.image = self.__punchingImages[self.__punchImageNum / 7]
                
                if self.__punchImageNum != 2 * 7:
                    self.__punchImageNum += 1
                    
            elif self.__randAttack == 1:
                self.image = self.__strongPunchImages[self.__strongImageNum / 7]
                
                if self.__strongImageNum != 3 * 7:
                    self.__strongImageNum += 1
                    
            elif self.__randAttack == 2:                
                self.image = self.__headbuttImages[self.__headbuttImageNum / 7]
                
                if self.__headbuttImageNum != 3 * 7:
                    self.__headbuttImageNum += 1            
        
        # ANIMATE THROW
        elif self.__throwing:
            self.image = self.__throwingImages[self.__throwImageNum / 5]
                
            if self.__throwImageNum != 2 * 5:
                self.__throwImageNum += 1
                
        # set transparent background
        self.image.set_colorkey((51,212,2))
                    
class Sasuke(pygame.sprite.Sprite):
    """
    The Sasuke class inherits from the sprite class. This class defines the 
    sprite for the Sasuke graphics.
    """
    def __init__(self, screen, player):
        """
        This initializer takes the screen and player as a parameter and uses 
        that to initialize the rect and image attributes. It also sets all the
        attributes that keep track of player animations, status, and movement.
        """
        # call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # define the image and rect attributes for the player
        # R means images facing right and L means images facing left
        self.__standingImagesR = []
        for imageNum in range(1,5):
            self.__standingImagesR.append(pygame.image.load("./Sasuke/Standing"\
                                            + str(imageNum) + ".png").convert())
            
        self.__standingImagesL = []
        for imageNum in range(4):
            self.__standingImagesL.append(pygame.transform.flip \
                                          (self.__standingImagesR[imageNum], True, False))
        
        # seperate check for direction is done for walking images
        self.__walkingImages = []
        for imageNum in range(1,7):
            self.__walkingImages.append(pygame.image.load("./Sasuke/Walking"\
                                            + str(imageNum) + ".png").convert())
         
        self.__flinchingImagesR = []
        for imageNum in range(1,3):
            self.__flinchingImagesR.append(pygame.image.load("./Sasuke/Flinching" \
                                            + str(imageNum) + ".png").convert())
            
        self.__flinchingImagesL = []
        for imageNum in range(2):
            self.__flinchingImagesL.append(pygame.transform.flip \
                                         (self.__flinchingImagesR[imageNum], True, False))
            
        self.__fallingImagesR = []
        for imageNum in range(1, 11):
            self.__fallingImagesR.append(pygame.image.load("./Sasuke/Falling" \
                                            + str(imageNum) + ".png").convert())
            
        self.__fallingImagesL = []
        for imageNum in range(10):
            self.__fallingImagesL.append(pygame.transform.flip \
                                         (self.__fallingImagesR[imageNum], True, False))
       
        self.__punchingImagesR = []
        for imageNum in range(1,4):
            self.__punchingImagesR.append(pygame.image.load("./Sasuke/Punching"\
                                            + str(imageNum) + ".png").convert())
            
        self.__punchingImagesL = []
        for imageNum in range(3):
            self.__punchingImagesL.append(pygame.transform.flip \
                                          (self.__punchingImagesR[imageNum], True, False))        
            
        self.__kickingImagesR = []
        for imageNum in range(1,5):
            self.__kickingImagesR.append(pygame.image.load("./Sasuke/Kicking"\
                                            + str(imageNum) + ".png").convert())
            
        self.__kickingImagesL = []
        for imageNum in range(4):
            self.__kickingImagesL.append(pygame.transform.flip \
                                          (self.__kickingImagesR[imageNum], True, False))        
            
        self.__strongPunchImagesR = []
        for imageNum in range(1,6):
            self.__strongPunchImagesR.append(pygame.image.load("./Sasuke/StrongPunch" \
                                            + str(imageNum) + ".png").convert())
            
        self.__strongPunchImagesL = []
        for imageNum in range(5):
            self.__strongPunchImagesL.append(pygame.transform.flip \
                                          (self.__strongPunchImagesR[imageNum], True, False))        
            
        self.__throwingImagesR = []
        for imageNum in range(1,4):
            self.__throwingImagesR.append(pygame.image.load("./Sasuke/Throwing" \
                                            + str(imageNum) + ".png").convert())      
            
        self.__throwingImagesL = []
        for imageNum in range(3):
            self.__throwingImagesL.append(pygame.transform.flip \
                                          (self.__throwingImagesR[imageNum], True, False))        
            
        self.image = self.__standingImagesR[0]
        
        if player == 1:
            self.rect = self.image.get_rect()
            self.rect.center = (screen.get_width()/4, screen.get_height()/2 + 100)
            self.__facing = "right"
        else:
            self.rect = self.image.get_rect()
            self.rect.center = (screen.get_width() * 3/4, screen.get_height()/2 + 100)
            self.__facing = "left"
            
        self.__dy = 0
        self.__dx = 0
        self.__move = True
        self.__goUp = False
        self.__goDown = False
        self.__goRight = False
        self.__goLeft = False
        
        self.__punching = False
        self.__throwing = False
        self.__flinching = False
        self.__fallen = False
        self.__randAttack = 0
        self.__randFlinch = 0
        
        # used to change the image attribute
        self.__standingImages = []
        self.__fallingImages = []
        self.__flinchingImages = []
        self.__punchingImages = []
        self.__strongPunchImages = []
        self.__kickingImages = []
        self.__throwingImages = []
        
        # used to reset the image number for each set of images
        self.__standImageNum = 0
        self.__walkImageNum = 0
        self.__punchImageNum = 0
        self.__strongImageNum = 0
        self.__kickImageNum = 0
        self.__throwImageNum = 0
        self.__fallImageNum = 0
        
        # used to control walking
        self.__decreasing = False
        self.__timer = 0
        self.__screen = screen
        
    def changeDirection(self, direction, stop):
        """
        This method uses the parameters keyPress and stop (a boolean value) to
        change the player's direction and stop in any direction when needed.
        """
        # check the direction of the key that has been pressed
        if not stop:
            if direction == "up":
                self.__goUp = True
                self.__goDown = False
            elif direction == "down":
                self.__goDown = True
                self.__goUp = False
            elif direction == "left":
                self.__goLeft = True
                self.__goRight = False
            else:
                self.__goRight = True
                self.__goLeft = False
        
        # when stop is True, check the direction of the key that has been lifted
        else:
            if direction == "up":
                self.__goUp = False
            elif direction == "down":
                self.__goDown = False
            elif direction == "left":
                self.__goLeft = False
            else:
                self.__goRight = False
        
        # change direction based on direction variables
        if self.__goUp:
            self.__dy = -1
        elif self.__goDown:
            self.__dy = 1
        else:
            self.__dy = 0
        if self.__goLeft:
            self.__dx = -1
        elif self.__goRight:
            self.__dx = 1
        else:
            self.__dx = 0
            
        # reset variable for displaying images
        if stop == False:
            self.__walkImageNum = 0
            self.__decreasing = False
            
        if self.__dx == 0 and self.__dy == 0:
            self.__standImageNum = 0

    def punch(self, punch):
        """
        This method takes punch, a boolean value, as a parameter and changes the
        punching attribute using it. It also resets the variables for cycling
        through images and assigns a random number to the randAttack attribute.
        """
        self.__punching = punch
        
        if punch:
            self.__punchImageNum = 0
            self.__strongImageNum = 0
            self.__kickImageNum = 0        
            self.__randAttack = random.randrange(3)
            
    def throw(self, throw):
        """
        This method takes punch, a boolean value, as a parameter and changes the
        throwing attribute using it. It also resets the variables for cycling 
        through images for throwing.
        """
        self.__throwing = throw
        self.__throwImageNum = 0
        
    def stayStill(self, stay):
        """
        This method keeps the player's rect from moving when stay is True
        and allows movement when stay is False.
        """
        if stay:
            self.__move = False
        else:
            self.__move = True
            
    def flinch(self, flinch):
        """
        This method takes flinch, a boolean value, and changes the flinching
        attribute to the value of the fallen parameter. It also resets the timer
        and assigns a random number to the randFlinch attribute.
        """        
        self.__flinching = flinch
        self.__timer = 0
        self.__randFlinch = random.randrange(2)
        
    def fallDown(self, fallen):
        """
        This method takes fallen, a boolean value, and changes the fallen
        attribute using the value of the fallen parameter
        """
        self.__fallen = fallen
        
    def changeOrientation(self, orientation):
        """
        This method takes orientation, a string value, and changes the facing
        attribute. It also changes the set of images the sprite will cycle 
        through depending on the direction they're facing and the status
        of the sprite.
        """
        if orientation == "right":
            self.__standingImages = self.__standingImagesR
            if not self.__punching or self.__punchingImages == []:
                self.__punchingImages = self.__punchingImagesR
                self.__strongPunchImages = self.__strongPunchImagesR
                self.__kickingImages = self.__kickingImagesR
                # only when not punching, change facing attribute
                self.__facing = orientation
            if not self.__throwing or self.__throwingImages == []:
                self.__throwingImages = self.__throwingImagesR
            if not self.__fallen:
                self.__fallingImages = self.__fallingImagesR
            if not self.__flinching:
                self.__flinchingImages = self.__flinchingImagesR
                
        if orientation == "left":
            self.__standingImages = self.__standingImagesL
            if not self.__punching or self.__punchingImages == []:
                self.__punchingImages = self.__punchingImagesL
                self.__strongPunchImages = self.__strongPunchImagesL
                self.__kickingImages = self.__kickingImagesL
                
                self.__facing = orientation
            if not self.__throwing or self.__throwingImages == []:
                self.__throwingImages = self.__throwingImagesL   
            if not self.__fallen:
                self.__fallingImages = self.__fallingImagesL
            if not self.__flinching:
                self.__flinchingImages = self.__flinchingImagesL            
        
    def getPunching(self):
        """
        This method returns the punching attribute.
        """
        return self.__punching 
    
    def getThrowing(self):
        """
        This method returns the throwing attribute.
        """
        return self.__throwing
    
    def getFlinchStatus(self):
        """
        This method returns the flinching attribute.
        """
        return self.__flinching
        
    def getFallStatus(self):
        """
        This method returns the fallen attribute
        """
        return self.__fallen
    
    def getMoveStatus(self):
        """
        This method returns the move attribute.
        """
        return self.__move
    
    def getMove(self):
        """
        This method returns the move attribute.
        """
        return self.__move
    def getOrientation(self):
        """
        This method returns the facing attribute.
        """
        return self.__facing
    
    def update(self):
        """
        This method takes no parameters. It is automatically called to update
        the Player sprite on the screen and detect whether it has reached the 
        boundary on the screen. It also cycles through lists of images depending
        on the status of the character to animate its actions.
        """
        # if Sasuke is standing still, ANIMATE HIM
        if (self.__dx == 0) and (self.__dy == 0) and self.__punching != True\
                                                 and self.__throwing != True\
                                                 and self.__fallen != True:
            
            # every 6 frames the image will change
            self.image = self.__standingImages[self.__standImageNum / 6]
            
            if self.__decreasing:
                self.__standImageNum -= 1
                if self.__standImageNum <= 0:
                    self.__decreasing = False
                    
            elif self.__decreasing == False:
                self.__standImageNum += 1
                # image moves every 6 frames so after 3 images start going back to the first
                if self.__standImageNum >= 6 * 3 + 5:
                    self.__decreasing = True  
                    
        if self.__move:
            
            # check if player has reached left or right of the screen
            if ((self.rect.centerx > 0) and (self.__dx < 0)) or \
               (self.rect.centerx < (self.__screen.get_width()) and (self.__dx > 0)):
                
                # the player moves unless conditions change
                self.rect.left += self.__dx * 4
                
            if ((self.rect.centery > self.__screen.get_height()/2) and (self.__dy < 0)) or \
               (self.rect.bottom < self.__screen.get_height()) and ((self.__dy > 0)):
                
                self.rect.top += self.__dy * 4
            
            # WALKING ANIMATIONS
            if self.__dx != 0 or self.__dy != 0:
                
                # image is updated once every 5 frames
                self.image = self.__walkingImages[self.__walkImageNum / 5]
                if self.__facing == "left":
                    # flip image on x axis if facing left
                    self.image = pygame.transform.flip(self.image, True, False)
            
                # consider x direction before y direction
                if (self.__goLeft and self.__facing == "left") or \
                   (self.__goRight and self.__facing == "right"):
                    self.__walkImageNum += 1
                    # 6 images in 6 * 5 frames
                    if self.__walkImageNum >= 5 * 5:
                        self.__walkImageNum = 0
                    
                elif (self.__goRight and self.__facing == "left") or \
                     (self.__goLeft and self.__facing == "right"):
                    self.__walkImageNum -= 1
                    if self.__walkImageNum <= 0:
                        self.__walkImageNum = 5 * 5 
                        
                elif self.__dy > 0:
                    self.__walkImageNum += 1
                    if self.__walkImageNum >= 5 * 5:
                        self.__walkImageNum = 0
                        
                elif self.__dy < 0:
                    self.__walkImageNum -= 1
                    if self.__walkImageNum <= 0:
                        self.__walkImageNum = 5 * 5  
        
        # ANIMATE FALL    
        elif self.__fallen:
            self.image = self.__fallingImages[self.__fallImageNum / 10]
            
            if self.__fallImageNum != 9 * 10:
                self.__fallImageNum += 1
                
                if self.__fallImageNum % 5 == 0:
                    if self.__fallingImages == self.__fallingImagesR:
                        self.rect.left -= 5
                    else:
                        self.rect.left += 5                    
                
        # ANIMATE FLINCH
        elif self.__flinching:
            # changes the image to a random one of Sasuke flinching
            self.image = self.__flinchingImages[self.__randFlinch]
            self.__timer += 1
            if self.__timer % 8 == 0:
                if self.__flinchingImages == self.__flinchingImagesR:
                    self.rect.left -= 3
                else:
                    self.rect.left += 3
            
        # ANIMATE PUNCH
        elif self.__punching:
            # three different attacks
            if self.__randAttack == 0:
                self.image = self.__punchingImages[self.__punchImageNum / 7]
                
                if self.__punchImageNum != 2 * 7:
                    self.__punchImageNum += 1
                    
            elif self.__randAttack == 1:
                self.image = self.__strongPunchImages[self.__strongImageNum / 7]
                
                if self.__strongImageNum != 3 * 7:
                    self.__strongImageNum += 1
                    
            elif self.__randAttack == 2:                
                self.image = self.__kickingImages[self.__kickImageNum / 7]
                
                if self.__kickImageNum != 3 * 7:
                    self.__kickImageNum += 1            
        
        # ANIMATE THROW
        elif self.__throwing:
            self.image = self.__throwingImages[self.__throwImageNum / 5]
                
            if self.__throwImageNum != 2 * 5:
                self.__throwImageNum += 1
                
        # set transparent background
        self.image.set_colorkey((0,158,4))

class Hitbox(pygame.sprite.Sprite):
    """
    The Hitbox class inherites from the sprite class. This class defines the 
    sprite for the hitbox of a player. This sprite will not be visible.
    """
    def __init__(self):
        """
        This initializor takes no parameters and it initializes the image and
        rect attributes.
        """
        # call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32,32))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        
    def update(self, playerPos):
        """
        This method is automatically called to update the rect attribute
        """
        self.rect.center = (playerPos[0] , playerPos[1] + 5)

# player attacks and stat sprites

class Punch(pygame.sprite.Sprite):
    """
    The Punch class inherites from the sprite class. This class defines the 
    sprite for the hitbox of a punch thrown by the player. This sprite will not
    be visible.
    """
    def __init__(self, player, playerPos, direction):
        """
        This initializer takes the player # and a tupple containing the position
        of the punch as parameters and uses them to initialize the image, rect,
        and screen attributes.
        """
        # call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        # set image and rect attributes
        punchPos = (playerPos[0] , playerPos[1])
        
        self.image = pygame.Surface((35, 15))
        self.image.convert()
        # visualized when needed
        self.image.fill((255,0,0))
        self.image.set_colorkey((255,0,0))
        
        self.rect = self.image.get_rect()
        self.rect.center = punchPos
        self.__player = player
        self.__direction = direction
        self.__timer = 0
        self.__damage = 5
        
    def getDamage(self):
        """
        This method returns the damage attribute
        """
        return self.__damage
    
    def getPlayer(self):
        """
        This method returns the player attribute. It represents the player
        who threw the punch.
        """
        return self.__player
    
    def update(self):
        """
        This method is automatically called to reposition the sprite and kill
        it when necessary.
        """        
        if self.__direction == "right":
            self.rect.left += 7
        else:
            self.rect.left -= 7
            
        self.__timer += 1
        
        if self.__timer == 9:
            self.kill()
            
class Shuriken(pygame.sprite.Sprite):
    """
    The Shuriken class inherites from the sprite class. This class defines the 
    sprite for a Shuriken thrown by the player.
    """
    def __init__(self, screen, player, playerPos, direction):
        """
        This initializer takes the screen, the player #, and a tupple containing
        the position of the player as parameters and uses them to initialize 
        the image, rect, and screen attributes.
        """
        # call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # set image and rect attributes
        self.image = pygame.image.load("./Projectiles/Kunai.png")
        if direction == "right":
            shurikenPos = (playerPos[0] + 8 , playerPos[1] + 6)
        else:
            shurikenPos = (playerPos[0] - 8 , playerPos[1] + 6)
            self.image = pygame.transform.flip(self.image, True, False)
        
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = shurikenPos
        
        self.__player = player
        self.__direction = direction
        self.__screen = screen
        self.__damage = 2
        
    def getDamage(self):
        """
        This method returns the damage attribute.
        """
        return self.__damage
        
    def getPlayer(self):
        """
        This method returns the player attribute. It represents the player
        who fired this projectile.
        """
        return self.__player
    
    def update(self):
        """
        This method is automatically called to reposition the sprite and kill
        it when necessary.
        """
    
        if self.__direction == "right":
            self.rect.left += 7
        else:
            self.rect.left -= 7
        
        if (self.rect.center[0] > self.__screen.get_width() + 50) or\
           (self.rect.center[0] < -50):
            self.kill()
            
class PointsBar(pygame.sprite.Sprite):
    """
    The PointsBar class inherits from the sprite class. This class defines the 
    sprite for a rectangle that is proportionate to a number of points.
    """
    def __init__(self, screen, maxPoints, color):
        """
        This initializer takes the screen, # of points, and color to
        initialize the image, color, and screen attributes.
        """
        # call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        # set image attribute (rect attribute set in subclass)
        # each point is displayed 5 pixels wide and 10 pixels tall
        self.image = pygame.Surface((maxPoints * 5, 10))
        self.image.convert()
        self.image.fill(color)
        self.image.set_colorkey((0,0,0))
            
        self.__color = color
        self.__screen = screen
        self.__points = maxPoints
        self.__maxPoints = maxPoints
        
    def losePoints(self, player, pointsLost):
        """
        This function decreases the size of the visible PointsBar based on the 
        value of pointsLost.
        """
        if player == 1:
            # get the coordinate of the end of the bar for player 1
            barEnd = self.__points * 5 - pointsLost * 5
            # draw missing health from the end of the new bar to the end of the old bar
            pygame.draw.rect(self.image, (0,0,0), ((barEnd, 0), \
                                                   (pointsLost * 5, 10)), 0)
            self.__points -= pointsLost
            
        else:
            self.__points -= pointsLost
            
            # draw from the left of the old bar to the left of the new bar
            pygame.draw.rect(self.image, (0,0,0), ((0,0), \
                            (self.__maxPoints *5 - self.__points * 5, 10)), 0)
        
    def resetBar(self):
        """
        This function resets the points attribute and image to represent the
        initial # of points from when it was initialized.
        """
        self.__points = self.__maxPoints
        self.image.fill(self.__color)
                         
    def getPoints(self):
        """
        This function returns the value of the points attribute
        """
        return self.__points
    
class HealthBar(PointsBar):
    """
    The HealthBar sprite inherites from the PointsBar sprite. It defines the
    sprite for a player's health bar
    """
    def __init__(self, screen, player):
        """
        This initializer takes the screen and player as parameters and uses
        them to initialize the rect attributes.
        """
        # call the parent __init__() method
        PointsBar.__init__(self, screen, 50, (255,0,0))
        
        # set the rect values based on the player
        self.rect = self.image.get_rect()
        if player == 1:
            self.rect.top = 25
            self.rect.left = 40
        else:
            self.rect.top = 25
            self.rect.right = screen.get_width() - 40
            
class ChakraBar(PointsBar):
    """
    The ChakraBar sprite inherties from the PointsBar sprite. It defines the 
    sprite for a player's chakra/mana bar.
    """
    def __init__(self, screen, player):
        """
        This initializer takes the screen and player as parameters and uses
        them to initialize the rect attributes.
        """
        # call the parent __init__() method
        PointsBar.__init__(self, screen, 40, (100,100,200))
        
        # set the rect values based on the player
        self.rect = self.image.get_rect()
        if player == 1:
            self.rect.top = 35
            self.rect.left = 40
        else:
            self.rect.top = 35
            self.rect.right = screen.get_width() - 40
        
# Label sprites        

class RoundLabel(pygame.sprite.Sprite):
    """
    The RoundLable class inherites from the sprite class. It defines the sprite for
    a label that shows the number of the current round during a fight.
    """
    def __init__(self, screen, numRound):
        """
        This initializer takes the screen and numRound as parameters to 
        initialize the font, image, and rect attributes.
        """
        # call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # set image and rect attributes
        self.__font = pygame.font.Font("./Fonts/njnaruto.ttf", 40)
        self.__message = "Round %d" % numRound
        self.image = self.__font.render(self.__message, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()/2, 90)

class PlayerWinsLabel(pygame.sprite.Sprite):
    """
    The PlayerWinsLabel class inherites from the sprite class. It defines the sprite 
    for a label that shows the number of rounds a player has won.
    """
    def __init__(self, screen, player, roundsWon):
        """
        This initializer takes the screen, player #, and the number of rounds won
        as parameters to initialize the font, image, and rect attributes.
        """
        # call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # set image and rect attributes
        self.__font = pygame.font.Font("./Fonts/electroharmonix.ttf", 25)
        self.__message = "P" + str(player) + " Score: %d" % roundsWon
        self.image = self.__font.render(self.__message, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        if player == 1:
            self.rect.center = (100, 70)
        else:
            self.rect.center = (screen.get_width() - 100, 70)
            
class DisplayWinner(pygame.sprite.Sprite):
    """
    The PlayerWins class inherites from the sprite class. It defines the sprite 
    for a label that shows the winner of a ROUND.
    """
    def __init__(self, screen, winner):
        """
        This initializer takes the screen, and player # as parameters to 
        initialize the font, image, and rect attributes.
        """
        # call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # set image and rect attributes
        self.__font = pygame.font.Font("./Fonts/edosz.ttf", 40)
        if winner:
            self.__message = "Player %d wins!" % winner
        else:
            self.__message = "Draw!"
            
        self.image = self.__font.render(self.__message, 1, (255, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = ((screen.get_width()/2, screen.get_height()/2))
            
class DisplayRound(pygame.sprite.Sprite):
    """
    The DisplayRound class inherites from the sprite class. It defines the sprite for
    a label that displays the number of the current round between rounds.
    """
    def __init__(self, screen, numRound):
        """
        This initializer takes the screen and numRound as parameters to 
        initialize the font, image, and rect attributes.
        """
        # call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # set image and rect attributes
        self.__font = pygame.font.Font("./Fonts/edosz.ttf", 150)
        self.__message = "Round %d" % numRound
        self.image = self.__font.render(self.__message, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()/2, screen.get_height()/2 - 80)
        
class DisplayPressKey(pygame.sprite.Sprite):
    """
    The DisplayPressKey inherites from the sprite class. It defines the sprite for
    a label that tells the user to press any key.
    """
    def __init__(self, screen):
        # call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # set image and rect attributes
        self.__font = pygame.font.Font("./Fonts/edosz.ttf", 30)
        self.__message = "Press any key"
        self.image = self.__font.render(self.__message, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()/2, screen.get_height()/2)    
        
class CountDown(pygame.sprite.Sprite):
    """
    The DisplayRound class inherites from the sprite class. It defines the sprite
    for a label that counts down from three and displays a message to inform
    players that the round has begun.
    """
    def __init__(self, screen):
        """
        This initializer takes the screen as a parameter to initialize the font,
        count, frameCount, message, and screen attributes.
        """
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Load the custom font and initialize the message
        self.__font = pygame.font.Font("./Fonts/edosz.ttf", 200)
        self.__count = 3
        self.__frameCount = 0
        
        self.__message = str(self.__count)
        self.__screen = screen
    
    def update(self):
        """
        This method is called to display the message attribute and keep track
        of time for the countdown.
        """
        #if self.__startCount:
        self.__frameCount += 1
        
        # update is called 60 times in a second
        if (self.__frameCount % 60 == 0):  # and (self.__frameCount != 0):
            self.__count -= 1
            self.__message = str(self.__count)
            
            if self.__count == 0:
                self.__message = "FIGHT"
            
        self.image = self.__font.render(self.__message, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (self.__screen.get_width()/2, self.__screen.get_height()/2)    
            
class GameOver(pygame.sprite.Sprite):
    """
    The GameOver class inherits from the sprite class. This class defines the
    lable that displays the winner when the game finishes.
    """
    def __init__(self, screen, winner):
        """
        This initializer takes screen as a parameter and uses it to initialize
        the screen and rect attributes. It also initializes font, and message
        attributes.
        """
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Load the custom font and initialize the message, image, and rect attributes
        self.__font = pygame.font.Font("./Fonts/njnaruto.ttf", 60)
        self.__message = "CHAMPION : Player %d" % winner
        self.image = self.__font.render(self.__message, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()/2, screen.get_height()/2)
        