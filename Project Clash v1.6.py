"""
Created by Jerry Li
May 29,2018
This program is an original game inspired by the Naruto: Clash of Ninja series. 
It's a simple brawler on a 2d plane and it uses the pygame module and clashSprites 
module where all the sprites for the game are initialized. The random module is
also used in this game. Naruto and Sasuke have a go at each other and are
limited to only physical attacks and shurikens. The win condition is when
one player wins 2 rounds before the other. This game features a menu that can
take you to the controls screen or begin the game. The player sprites are also
completely animated and features Naruto bgm and classic sound effects. Enjoy!
version v1.6
"""

import pygame, clashSprites, random
pygame.init()

def gamePlay(screen, scores, numRound, randNum):
    """
    This function defines the main game loop and everything else that makes
    the game work. It returns the variables quitGame and winner which will
    tell the main() function if the player wishes to quit the game and which
    player has won the round.
    """
    # Entities
    background = clashSprites.Background(screen, randNum)
    
    # initialize sprites
    # labels
    healthBarP1 = clashSprites.HealthBar(screen, 1)
    healthBarP2 = clashSprites.HealthBar(screen, 2)
    chakraBarP1 = clashSprites.ChakraBar(screen, 1)
    chakraBarP2 = clashSprites.ChakraBar(screen, 2)
    roundLabel = clashSprites.RoundLabel(screen, numRound)
    player1Wins = clashSprites.PlayerWinsLabel(screen, 1, scores[0])
    player2Wins = clashSprites.PlayerWinsLabel(screen, 2, scores[1])
    
    # player and hitbox sprites
    player1 = clashSprites.Naruto(screen, 1)
    player2 = clashSprites.Sasuke(screen, 2)
    hitboxP1 = clashSprites.Hitbox()
    hitboxP2 = clashSprites.Hitbox()
    
    # sprite groups
    hitboxes = pygame.sprite.Group(hitboxP1, hitboxP2)
    hitSprites = pygame.sprite.Group()
    underSprites = pygame.sprite.OrderedUpdates(background)
    otherSprites = pygame.sprite.OrderedUpdates(healthBarP1, healthBarP2, \
                  chakraBarP1, chakraBarP2, roundLabel, player1Wins, player2Wins)
    playerSprites = pygame.sprite.OrderedUpdates(player1, player2)
    allSprites = pygame.sprite.OrderedUpdates(underSprites, playerSprites, otherSprites)
    
    # Sound effects
    hit = pygame.mixer.Sound("./Sounds/Hit.wav")
    hit.set_volume(0.4)   
    throw = pygame.mixer.Sound("./Sounds/Throw.wav")
    throw.set_volume(0.6)   
    punch = pygame.mixer.Sound("./Sounds/Punch.wav")
    punch.set_volume(0.6)
    
    # ACTION
     
    # Assign
    clock = pygame.time.Clock()
    keepGoing = True
    quitGame = False
    winner = 0
    
    #P1 uses wasd to move while P2 uses arrow keys to move
    keysP1 = {119:"up" , 115:"down", 97:"left", 100:"right"}
    keysP2 = {273:"up", 274:"down", 276:"left", 275:"right"}
    
    # player status
    # for changing order of players blit on top of each other
    onTopP1 = True
    canPunchP1 = True
    canPunchP2 = True
    canThrowP1 = True
    canThrowP2 = True
    timer1 = 0
    timer2 = 0
    timer3 = 0
    timer4 = 0
    timer5 = 0
    timer6 = 0
    timer7 = 0
    
    # Loop
    while keepGoing:
     
        # Time
        clock.tick(60)
     
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                quitGame = True
                
            elif event.type == pygame.KEYDOWN:
                # player movement
                if event.key in keysP1:
                    #False for KEYDOWN and True for KEYUP
                    #if player1.getMoveStatus():
                    player1.changeDirection(keysP1[event.key], False)
                elif event.key in keysP2:
                    #if player2.getMoveStatus():
                    player2.changeDirection(keysP2[event.key], False)
                
                # punch detection - getFallStatus() returns whether the player has fallen
                elif event.key == pygame.K_f:
                    if canPunchP1 and player1.getMove() and player1.getFallStatus() == False:
                        player1.stayStill(True)
                        player1.punch(True)
                        punch.play(0)
                        # punch sprite handled in timer
                       
                        canPunchP1 = False
                        
                elif event.key == pygame.K_k:
                    if canPunchP2 and player2.getMove() and player2.getFallStatus() == False:
                        player2.stayStill(True)
                        player2.punch(True)
                        punch.play(0)
                        
                        canPunchP2 = False
                
                # throw detection
                elif event.key == pygame.K_g:
                    if canThrowP1 and player1.getMove() and player1.getFallStatus() == False:
                        canThrowP1 = False
                        player1.stayStill(True)
                        player1.throw(True)
                        throw.play(0)
                        shuriken = clashSprites.Shuriken(screen, 1, player1.rect.center, \
                                                         player1.getOrientation())
                        hitSprites.add(shuriken)
                        allSprites.add(shuriken)
                        
                elif event.key == pygame.K_l:
                    if canThrowP2 and player2.getMove() and player2.getFallStatus() == False:
                        canThrowP2 = False
                        player2.stayStill(True)
                        player2.throw(True)
                        throw.play(0)
                        shuriken = clashSprites.Shuriken(screen, 2, player2.rect.center, \
                                                         player2.getOrientation())
                        hitSprites.add(shuriken)
                        allSprites.add(shuriken)
                        
            elif event.type == pygame.KEYUP:
                # player movement
                if event.key in keysP1:
                    player1.changeDirection(keysP1[event.key], True)
                elif event.key in keysP2:
                    player2.changeDirection(keysP2[event.key], True)
        
        # collision detection between projectiles, fists and players
        hitList1 = pygame.sprite.spritecollide(hitboxP1 , hitSprites, False)
        if hitList1:
            hitSprite = hitList1[0]
            if hitSprite.getPlayer() == 2:
                if player1.getFallStatus() == False and winner == 0:
                    hit.play(0)
                    healthBarP1.losePoints(1, hitSprite.getDamage())
                    hitSprite.kill()
                    if healthBarP1.getPoints() > 0:
                        player1.flinch(True)
                        player1.stayStill(True)
            
        hitList2 = pygame.sprite.spritecollide(hitboxP2 , hitSprites, False)
        if hitList2:
            hitSprite = hitList2[0]
            if hitSprite.getPlayer() == 1:
                if player2.getFallStatus() == False and winner == 0:
                    hit.play(0)
                    healthBarP2.losePoints(2, hitSprite.getDamage())
                    hitSprite.kill()    
                    if healthBarP2.getPoints() > 0:
                        player2.flinch(True)
                        player2.stayStill(True)
                    
        # timers to keep track of attacks and time between them
        # punch timers
        if canPunchP1 == False:
            timer1 += 1
            if timer1 == 10 and player1.getFlinchStatus() == False:
                punchP1 = clashSprites.Punch(1, player1.rect.center, player1.getOrientation())
                hitSprites.add(punchP1)
                allSprites.add(punchP1)                
            # if the player has fallen, don't make the player able to move
            if timer1 == 32 and player1.getFallStatus() == False:
                player1.stayStill(False)
                player1.punch(False)
            elif timer1 == 40:
                canPunchP1 = True
                timer1 = 0
            
        if canPunchP2 == False:
            timer2 += 1
            if timer2 == 10 and player2.getFlinchStatus() == False:
                punchP2 = clashSprites.Punch(2, player2.rect.center, player2.getOrientation())
                hitSprites.add(punchP2)
                allSprites.add(punchP2)                
            if timer2 == 32 and player2.getFallStatus() == False:
                player2.stayStill(False)
                player2.punch(False)
            elif timer2 == 40:
                canPunchP2 = True
                timer2 = 0
        
        # shuriken timers
        if canThrowP1 == False:
            timer3 += 1
            if timer3 == 20 and player1.getFallStatus() == False:
                player1.stayStill(False)
                player1.throw(False)
            if timer3 == 30:
                canThrowP1 = True
                timer3 = 0
                
        if canThrowP2 == False:
            timer4 += 1
            if timer4 == 20 and player2.getFallStatus() == False:
                player2.stayStill(False)
                player2.throw(False)
            if timer4 == 30:
                canThrowP2 = True
                timer4 = 0
        
        # flinching timers
        if player1.getFlinchStatus():
            timer5 += 1
            if timer5 == 17:
                player1.stayStill(False)
                player1.flinch(False)
                timer5 = 0
                
        if player2.getFlinchStatus():
            timer6 += 1
            if timer6 == 17:
                player2.stayStill(False)
                player2.flinch(False)
                timer6 = 0
                
        # CHECKING PLAYER STATUS
        
        # display which player is closer to the front of the screen and update 
        # the ordered they're displayed in
        if player1.rect.bottom < player2.rect.bottom and onTopP1 == False:
            playerSprites = pygame.sprite.OrderedUpdates(player1, player2)
            # preventing crashing if the displayWinner sprite has not been initialized
            if timer7 > 0:
                allSprites = pygame.sprite.OrderedUpdates(underSprites, \
                            playerSprites, hitSprites, otherSprites, displayWinner)
            else:
                allSprites = pygame.sprite.OrderedUpdates(underSprites, \
                                        playerSprites, hitSprites, otherSprites)                
            onTopP1 = True
            
        if player1.rect.bottom > player2.rect.bottom and onTopP1:
            playerSprites = pygame.sprite.OrderedUpdates(player2, player1)  
            if timer7 > 0:
                allSprites = pygame.sprite.OrderedUpdates(underSprites, \
                            playerSprites, hitSprites, otherSprites, displayWinner)
            else:
                allSprites = pygame.sprite.OrderedUpdates(underSprites, \
                                        playerSprites, hitSprites, otherSprites)
            onTopP1 = False
            
        # check which player is on which side of the screen and change their orientations
        if (player1.rect.centerx > player2.rect.centerx):
            player1.changeOrientation("left")
            player2.changeOrientation("right")
        elif (player1.rect.centerx < player2.rect.centerx):
            player1.changeOrientation("right")
            player2.changeOrientation("left")
            
        # CHECK FOR WINNER AND DISPLAY WHO WON
        
        # if both players have 0 health at the same time it's a draw(VERY UNLIKELY)
        # if the winner hasn't been decided yet, check player health
        if timer7 == 0:
            if (healthBarP1.getPoints() <= 0) and (healthBarP2.getPoints() <= 0):
                winner = -1
                player1.fallDown(True)
                player1.stayStill(True)
                player2.fallDown(True)
                player2.stayStill(True)
        
                displayWinner = clashSprites.DisplayWinner(screen, 0)
                allSprites.add(displayWinner)
        
            elif healthBarP1.getPoints() <= 0:
                winner = 2
                player1.fallDown(True)
                player1.stayStill(True)
                
                displayWinner = clashSprites.DisplayWinner(screen, 2)
                allSprites.add(displayWinner)
            
            elif healthBarP2.getPoints() <= 0:
                winner = 1
                player2.fallDown(True)
                player2.stayStill(True)
                
                displayWinner = clashSprites.DisplayWinner(screen, 1)
                allSprites.add(displayWinner)
            
        # timer to delay the end of the round
        if winner:
            timer7 += 1
            if timer7 == 60 * 3:
                keepGoing = False
                displayWinner.kill()
            
        # Refresh screen
        #hitboxes.clear(screen, background.image)
        allSprites.clear(screen, background.image)
        allSprites.update()
        hitboxP1.update(player1.rect.center)
        hitboxP2.update(player2.rect.center)
        allSprites.draw(screen)
        #hitboxes.draw(screen)
        
        pygame.display.flip()
    
    return winner, quitGame

def displayMenu(screen, playMusic):
    """
    The displayMenu function displays the game menu and gives the player the 
    option of beginning the game or looking at the controls. This function 
    returns the quitGame, startGame, and showControls variables to the main()
    function to decide what option the player has selected.
    """
    menu = pygame.image.load( "./Menu/Game Menu.png" )
    menu = menu.convert()
    screen.blit(menu, (0,0))
    
    playButton = clashSprites.MenuButton(screen, (184, 355), "play")
    controlsButton = clashSprites.MenuButton(screen, (450, 345), "controls")
    helpButton = clashSprites.MenuButton(screen, (535, 146), "help")
    #buttons = pygame.sprite.Group(playButton, controlsButton, helpButton)
    
    # Music
    if playMusic:
        pygame.mixer.music.load("./Sounds/Naruto Theme.mp3")
        pygame.mixer.music.set_volume(0.1)       
        pygame.mixer.music.play(-1)
    
    # Assign
    clock = pygame.time.Clock()
    keepGoing = True
    quitGame = False
    startGame = False
    showControls = False
    
    while keepGoing:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                quitGame = True        
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # make a 1 x 1 pixel sprite where the player clicked
                clickSprite = clashSprites.Click(pygame.mouse.get_pos())
        
        # Events
        # handle exception if clickSprite has not been initiated
        try:
            if clickSprite.rect.colliderect(playButton.rect):
                keepGoing = False
                startGame = True
                
            elif clickSprite.rect.colliderect(controlsButton.rect):
                keepGoing = False
                showControls = True
        
        except UnboundLocalError:
            doNothing = "doNothing"
            
        # Display
        pygame.display.flip()
                         
    return quitGame, startGame, showControls                
                
def displayControls(screen):
    """
    The displayControls function displays the game instructions and returns quitGame
    to tell the main function whether the player wants to exit the game. This
    function returns quitGame, a boolean value which will tell the main 
    function whether the player wishes to quit the game.
    """
    # Entities
    controls = pygame.image.load( "./Menu/Project Clash Controls.png" )
    controls = controls.convert()
    screen.blit(controls, (0,0))
    
    # ACTION
    
    # Assign
    clock = pygame.time.Clock()
    keepGoing = True
    quitGame = False
    
    while keepGoing:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                quitGame = True        
                
            elif event.type == pygame.KEYDOWN:
                keepGoing = False
                
        # display        
        pygame.display.flip()        
    
    return quitGame
    
def displayRound(screen, scores, numRound):
    """
    The displayRound function is called before the first round and in between
    each one to display the player scores and which round the fight is in. It 
    returns the quitGame, which indicates whether the player wishes to quit the
    game, and randNum attribute for keeping the background consistent in the
    gamePlay function.
    """
    # Entities
    # random background each round
    randNum = random.randrange(1, 4)    
    background = clashSprites.Background(screen, randNum)
    
    # label sprites
    player1Wins = clashSprites.PlayerWinsLabel(screen, 1, scores[0])
    player2Wins = clashSprites.PlayerWinsLabel(screen, 2, scores[1])
    roundLabel = clashSprites.DisplayRound(screen, numRound)
    pressKey = clashSprites.DisplayPressKey(screen)
    
    # player sprites
    player1 = clashSprites.Naruto(screen, 1)
    player2 = clashSprites.Sasuke(screen, 2)
    
    # sprite groups
    underSprites = pygame.sprite.OrderedUpdates(background)
    playerSprites = pygame.sprite.OrderedUpdates(player1, player2)
    otherSprites = pygame.sprite.OrderedUpdates(player1Wins, player2Wins, roundLabel)
    allSprites = pygame.sprite.OrderedUpdates(underSprites, playerSprites, otherSprites)
    
    # ACTION
     
    # Assign
    clock = pygame.time.Clock()
    keepGoing = True
    quitGame = False
    startTimer = False
    startTimer2 = True
    timer = 0
    timer2 = 0

    #P1 uses wasd to move while P2 uses arrow keys to move
    keysP1 = {119:"up" , 115:"down", 97:"left", 100:"right"}
    keysP2 = {273:"up", 274:"down", 276:"left", 275:"right"}
    
    onTopP1 = True
    # in order to call the changeOrientation function at beg. of game
    faceRightP1 = False
    
    # Loop
    while keepGoing:
     
        # Time
        clock.tick(60)
     
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                quitGame = True
                
            elif event.type == pygame.KEYDOWN:
                # player movement
                if event.key in keysP1:
                    #False for KEYDOWN and True for KEYUP
                    player1.changeDirection(keysP1[event.key], False)
                elif event.key in keysP2:
                    player2.changeDirection(keysP2[event.key], False)
                
                # if the player presses any key, the countdown begins    
                else:
                    if startTimer != True and startTimer2 != True:
                        roundLabel.kill()
                        pressKey.kill()
                        countDown = clashSprites.CountDown(screen)
                        allSprites.add(countDown)
                        startTimer = True
                    
            elif event.type == pygame.KEYUP:
                # player movement
                if event.key in keysP1:
                    player1.changeDirection(keysP1[event.key], True)
                elif event.key in keysP2:
                    player2.changeDirection(keysP2[event.key], True)
        
        # display which player is closer to the front of the screen
        if player1.rect.bottom < player2.rect.bottom and onTopP1 == False:
            playerSprites = pygame.sprite.OrderedUpdates(player1, player2)
            # preventing crashes and glitches with displaying the countdown
            try:
                allSprites = pygame.sprite.LayeredUpdates(underSprites, \
                                playerSprites, otherSprites, countDown)
            except UnboundLocalError:
                allSprites = pygame.sprite.LayeredUpdates(underSprites, 
                                playerSprites, otherSprites)
                                                          
            onTopP1 = True
            
        elif player1.rect.bottom > player2.rect.bottom and onTopP1:
            playerSprites = pygame.sprite.OrderedUpdates(player2, player1) 
            try:
                allSprites = pygame.sprite.LayeredUpdates(underSprites, \
                                playerSprites, otherSprites, countDown)
            except UnboundLocalError:
                allSprites = pygame.sprite.LayeredUpdates(underSprites, \
                                playerSprites, otherSprites)
            
            onTopP1 = False
            
        # check which player is on which side of the screen and change their orientations
        if (player1.rect.centerx > player2.rect.centerx) and faceRightP1:
            player1.changeOrientation("left")
            player2.changeOrientation("right")
            faceRightP1 = False
        elif (player1.rect.centerx < player2.rect.centerx) and not faceRightP1:
            player1.changeOrientation("right")
            player2.changeOrientation("left")
            faceRightP1 = True
        
        # times the countdown    
        if startTimer:
            timer += 1
            if timer == 210:
                keepGoing = False
        
        # times when the pressKey lable will be displayed        
        if startTimer2:
            timer2 += 1
            if timer2 == 90:
                otherSprites.add(pressKey)
                allSprites = pygame.sprite.OrderedUpdates(underSprites, playerSprites, otherSprites)
                startTimer2 = False
                
        # Refresh screen
        allSprites.clear(screen, background.image)
        allSprites.update()
        allSprites.draw(screen)
     
        pygame.display.flip()
        
    return quitGame, randNum

def main():
    """
    The main function defines the mainline logic for the game. It keeps track
    of rounds and each of the players' scores.
    """
    # Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Project Clash v1.6") 
    
    # Assign key variables
    scoreP1 = 0
    scoreP2 = 0
    winner = 0
    numRound = 0
    quitGame = False
    playMusic = True
    
    # loop that calls the main game function and screens that display in between
    # and after
    # also keeps track of score and round#
    while quitGame == False:
        if numRound == 0:
            quitGame, startGame, showControls = displayMenu(screen, playMusic)
            playMusic = False
            if quitGame:
                break
        
        if showControls:
            quitGame = displayControls(screen)
            showControls = False
            if quitGame:
                break
            
        if startGame:
            numRound += 1
            quitGame, randNum = displayRound(screen, (scoreP1, scoreP2), numRound)
            if quitGame:
                break
        
            # call the main game function
            winner, quitGame = gamePlay(screen, (scoreP1, scoreP2), numRound, randNum)
        
        # if it's a draw, neither player gets a point
        if winner == 1:
            scoreP1 += 1
        elif winner == 2:
            scoreP2 += 1
        
        if scoreP1 == 2 or scoreP2 == 2:
            # display the ultimate winner
            if scoreP1 > scoreP2:
                displayWinner = clashSprites.GameOver(screen, 1)
            else:
                displayWinner = clashSprites.GameOver(screen, 2)
            
            winnerSprite = pygame.sprite.Group(displayWinner)
            winnerSprite.draw(screen)
            pygame.display.flip()
            pygame.time.delay(3000) 
            
            # reset all key variables
            startGame = False
            scoreP1 = 0
            scoreP2 = 0
            winner = 0
            numRound = 0
            playMusic = True
            
    pygame.quit()
    
# Call the main function
main()











