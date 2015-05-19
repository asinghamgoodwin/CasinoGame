import pygame, sys
from pygame.locals import *
import random
import itertools

pygame.init()

# set up the window
window = pygame.display.set_mode((1080, 696))
pygame.display.set_caption('Casino v2')

# set up the colors
BLACK =(0, 0, 0)
WHITE = (255, 255, 255)
RED = (205, 0, 0)
GREEN =(0, 150, 0)
BLUE =(0, 0, 205)
BEIGE = (255, 255, 204)
YELLOW = (255, 255, 0)

#load all of the card images
c1 = pygame.image.load('cardImages/c1.png')
s1 = pygame.image.load('cardImages/s1.png')
h1 = pygame.image.load('cardImages/h1.png')
d1 = pygame.image.load('cardImages/d1.png')
c2 = pygame.image.load('cardImages/c2.png')
s2 = pygame.image.load('cardImages/s2.png')
h2 = pygame.image.load('cardImages/h2.png')
d2 = pygame.image.load('cardImages/d2.png')
c3 = pygame.image.load('cardImages/c3.png')
s3 = pygame.image.load('cardImages/s3.png')
h3 = pygame.image.load('cardImages/h3.png')
d3 = pygame.image.load('cardImages/d3.png')
c4 = pygame.image.load('cardImages/c4.png')
s4 = pygame.image.load('cardImages/s4.png')
h4 = pygame.image.load('cardImages/h4.png')
d4 = pygame.image.load('cardImages/d4.png')
c5 = pygame.image.load('cardImages/c5.png')
s5 = pygame.image.load('cardImages/s5.png')
h5 = pygame.image.load('cardImages/h5.png')
d5 = pygame.image.load('cardImages/d5.png')
c6 = pygame.image.load('cardImages/c6.png')
s6 = pygame.image.load('cardImages/s6.png')
h6 = pygame.image.load('cardImages/h6.png')
d6 = pygame.image.load('cardImages/d6.png')
c7 = pygame.image.load('cardImages/c7.png')
s7 = pygame.image.load('cardImages/s7.png')
h7 = pygame.image.load('cardImages/h7.png')
d7 = pygame.image.load('cardImages/d7.png')
c8 = pygame.image.load('cardImages/c8.png')
s8 = pygame.image.load('cardImages/s8.png')
h8 = pygame.image.load('cardImages/h8.png')
d8 = pygame.image.load('cardImages/d8.png')
c9 = pygame.image.load('cardImages/c9.png')
s9 = pygame.image.load('cardImages/s9.png')
h9 = pygame.image.load('cardImages/h9.png')
d9 = pygame.image.load('cardImages/d9.png')
c10 = pygame.image.load('cardImages/c10.png')
s10 = pygame.image.load('cardImages/s10.png')
h10 = pygame.image.load('cardImages/h10.png')
d10 = pygame.image.load('cardImages/d10.png')
c11 = pygame.image.load('cardImages/c11.png')
s11 = pygame.image.load('cardImages/s11.png')
h11 = pygame.image.load('cardImages/h11.png')
d11 = pygame.image.load('cardImages/d11.png')
c12 = pygame.image.load('cardImages/c12.png')
s12 = pygame.image.load('cardImages/s12.png')
h12 = pygame.image.load('cardImages/h12.png')
d12 = pygame.image.load('cardImages/d12.png')
c13 = pygame.image.load('cardImages/c13.png')
s13 = pygame.image.load('cardImages/s13.png')
h13 = pygame.image.load('cardImages/h13.png')
d13 = pygame.image.load('cardImages/d13.png')
back = pygame.image.load('cardImages/back.png')

cardImageNames = {'c1': c1, 's1': s1, 'h1': h1, 'd1': d1, 'c2': c2, 's2': s2, 'h2': h2, 'd2': d2,
                  'c3': c3, 's3': s3, 'h3': h3, 'd3': d3, 'c4': c4, 's4': s4, 'h4': h4, 'd4': d4,
                  'c5': c5, 's5': s5, 'h5': h5, 'd5': d5, 'c6': c6, 's6': s6, 'h6': h6, 'd6': d6,
                  'c7': c7, 's7': s7, 'h7': h7, 'd7': d7, 'c8': c8, 's8': s8, 'h8': h8, 'd8': d8,
                  'c9': c9, 's9': s9, 'h9': h9, 'd9': d9, 'c10': c10, 's10': s10, 'h10': h10, 'd10': d10,
                  'c11': c11, 's11': s11, 'h11': h11, 'd11': d11, 'c12': c12, 's12': s12, 'h12': h12, 'd12': d12,
                  'c13': c13, 's13': s13, 'h13': h13, 'd13': d13}


#this is the top left corner coordinates of each card spot#
cardLocations = {"mh1": (24*15, 24*24), "mh2": (24*19, 24*24), "mh3": (24*23,24*24), "mh4": (24*27,24*24),

                 "yh1": (24*15, 24), "yh2": (24*19, 24), "yh3": (24*23,24), "yh4": (24*27,24),

                 "t1": (24*19,24*12), "t2": (24*15,24*12), "t3": (24*11,24*12), "t4": (24*7,24*12),
                 "t5": (24*21,24*7), "t6": (24*17,24*7), "t7": (24*13,24*7), "t8": (24*9,24*7),"t9": (24*5,24*7),
                 "t10": (24*21,24*17), "t11": (24*17,24*17), "t12": (24*13,24*17), "t13": (24*9,24*17), "t14": (24*5,24*17),

                 "bA1": (24*25,24*9), "bA2": (24*25,24*10), "bA3": (24*25,24*11), "bA4": (24*25,24*12), "bA5": (24*25,24*13),
                 "bA6": (24*25,24*14), "bA7": (24*25,24*15), "bA8": (24*25,24*16), "bA9": (24*25,24*17), "bA10": (24*25,24*18),

                 "bB1": (24*29,24*9), "bB2": (24*29,24*10), "bB3": (24*29,24*11), "bB4": (24*29,24*12), "bB5": (24*29,24*13),
                 "bB6": (24*29,24*14), "bB7": (24*29,24*15), "bB8": (24*29,24*16), "bB9": (24*29,24*17), "bB10": (24*29,24*18),

                 "bC1": (24*33,24*9), "bC2": (24*33,24*10), "bC3": (24*33,24*11), "bC4": (24*33,24*12), "bC5": (24*33,24*13),
                 "bC6": (24*33,24*14), "bC7": (24*33,24*15), "bC8": (24*33,24*16), "bC9": (24*33,24*17), "bC10": (24*33,24*18),

                 "bD1": (24*37,24*9), "bD2": (24*37,24*10), "bD3": (24*37,24*11), "bD4": (24*37,24*12), "bD5": (24*37,24*13),
                 "bD6": (24*37,24*14), "bD7": (24*37,24*15), "bD8": (24*37,24*16), "bD9": (24*37,24*17), "bD10": (24*37,24*18)}


locationOrder = ["mh1","mh2","mh3","mh4","yh1","yh2","yh3","yh4",
                 "t1","t2","t3","t4","t5","t6","t7","t8","t9","t10","t11","t12","t13","t14",
                 "bA1","bA2","bA3","bA4","bA5","bA6","bA7","bA8","bA9","bA10",
                 "bB1","bB2","bB3","bB4","bB5","bB6","bB7","bB8","bB9","bB10",
                 "bC1","bC2","bC3","bC4","bC5","bC6","bC7","bC8","bC9","bC10",
                 "bD1","bD2","bD3","bD4","bD5","bD6","bD7","bD8","bD9","bD10"]


#each cardSpot object is one of the 61 spots that a card could be in on the board. they contain info on what card is in that spot, etc.
class cardSpot():
    def __init__(self, name, side="Front"):
        self.name = name #string to describe the spot
        self.location = cardLocations[name]
        self.side = side
        self.card = None
        self.selected = False

    def assignCard(self, card):
        self.card = card

    def removeCard(self):
        self.card = None
        self.selected = False

    def select(self):
        #only lets you select if its a face-up card that exists on the board
        if self.card != None and self.side != "Back":
            
            #if it is in my hand, selecting this card unselects the rest of them
            if self.name[0] == "m":
                for spot in cardSpots[:4]:
                    spot.selected = False
            elif self.name[0] == "b": #turning everything in the build selected at once
                if self.name[1] == "A":
                    i = 22
                elif self.name[1] == "B":
                    i = 32
                elif self.name[1] == "C":
                    i = 42
                elif self.name[1] == "D":
                    i = 52
                for spot in cardSpots[i:i+10]:
                    if spot.card != None:
                            spot.selected = True


        self.selected = True #select this one

    def unselect(self):
        self.selected = False
        if self.name[0] == "b": #turning everything in the build unselected at once
                if self.name[1] == "A":
                    i = 22
                elif self.name[1] == "B":
                    i = 32
                elif self.name[1] == "C":
                    i = 42
                elif self.name[1] == "D":
                    i = 52
                for spot in cardSpots[i:i+10]:
                    if spot.card != None:
                            spot.selected = False


#makes a list that contains all of the cardSpot objects. *this is a big, important list*
cardSpots = [cardSpot(name) for name in locationOrder]    
for i in range(4,8): #the other player's cards
    cardSpots[i].side = "Back"


def spotFromCoordinates(x, y):
    for spot in cardSpots:
        if (spot.location[0] < x < spot.location[0]+24*3) and (spot.location[1] < y < spot.location[1]+24*4):
            return spot
    return None


##-- functions that place cards on and off the table (partners with the move classes from the game logic) --##

#list of what rank is being built in each of the four spots
buildRankDict = {0: 0 , 1: 0, 2: 0, 3: 0} ### where do these get assigned? ###

def playCardUI(card):
    #find the card that was played from one of the two player's hands, remove it.
    #this happens every turn, regardless of the play, and is incorporated in the other functions
    for spot in cardSpots[:8]:
        if spot.card == card:
            spot.removeCard()

def dealToTableUI(initialDealList): #this would get called once at the beginning of each game
    for i in range(4):
          cardSpots[i+8].assignCard(initialDealList[i])

def discardUI(card):
    #this adds the discarded card onto the table in the first available spot, and takes the card out of your hand
    playCardUI(card)
    for spot in cardSpots[8:22]:
        if spot.card == None:
            spot.assignCard(card)
            break

def addToBuildUI(cardPlayed, cardList, rank):
    takeFromTableUI(cardPlayed, cardList)
    for rankSpot in buildRankDict.keys():
        if buildRankDict[rankSpot] == rank:
            if rankSpot == 0:
                j = 0
            elif rankSpot == 1:
                j = 10
            elif rankSpot == 2:
                j = 20
            elif rankSpot == 3:
                j = 30

    ##------------- not yet tested!! -------------------##
    toBePlaced = cardList+[cardPlayed]
    for spot in cardSpots[j+22:j+32]:
        if spot.card == None:
            spot.assignCard(toBePlaced.pop())
            if len(toBePlaced) == 0:
                break
    
def takeFromTableUI(cardPlayed, cardList): #this gets rid of the cards you took and your card (which go into your pile)
    playCardUI(cardPlayed)
    for card in cardList:
        for spot in cardSpots[8:]:
            if spot.card == card:
                spot.removeCard()

def takeBuildUI(rank): #sometimes this will get called at the same time as takeFromTableUI if you're taking lots of different stuff at once
    for i in range(4):
        if buildRankDict[i] == rank:
            if i == 0:
                j = 0
            elif i == 1:
                j = 10
            elif i == 2:
                j = 20
            elif i == 3:
                j = 30
    for spot in cardSpots[j+22:j+32]:
        spot.removeCard()


    
def populateHandsUI(player1, player2):
    #only to be called at the beginning of a hand when the two players get dealt
    #this puts the cards that are newly in player1 and 2's hands intothe cardSpots list

    #to determine whose hand to put the cards in
    for player in [player1, player2]:
        if player.side == "top":
            j = 4
        else:
            j = 0
            
        for i in range(4):
            cardSpots[j+i].assignCard(player.hand[i])
            if player.side == "top":
                cardSpots[j+i].side = "Back"

def selectLastCardsUI(player):
    for cardSpot in cardSpots[8:22]:
        if cardSpot != None:
            cardSpot.select()
    
    pygame.draw.rect(window, BLUE, (24*27, 24*11.5, 24*13, 24*5))
    insFont = pygame.font.Font('freesansbold.ttf', 22)
    ins1 = insFont.render(player.name+" was the", True, BEIGE, BLUE)
    ins1RectObj = ins1.get_rect()
    ins1RectObj.topleft = (24*28,24*12)
    window.blit(ins1, ins1RectObj)

    ins2 = insFont.render("last to take cards,", True, BEIGE, BLUE)
    ins2RectObj = ins2.get_rect()
    ins2RectObj.topleft = (24*28,24*13)
    window.blit(ins2, ins2RectObj)

    ins3 = insFont.render("and therefore wins", True, BEIGE, BLUE)
    ins3RectObj = ins3.get_rect()
    ins3RectObj.topleft = (24*28,24*14)
    window.blit(ins3, ins3RectObj)

    ins4 = insFont.render("all of the cards left.", True, BEIGE, BLUE)
    ins4RectObj = ins4.get_rect()
    ins4RectObj.topleft = (24*28,24*15)
    window.blit(ins4, ins4RectObj)



## drawing the cards into the screen ##

def paintCard(card, loc): #I named it paint just to not confuse this with drawing (as in taking) a card from a deck
    window.blit(cardImageNames[card.suit+str(card.rank)],loc)                


def paintAllCards():
    for spot in cardSpots:
        if spot.card != None:
            if spot.selected: ###make this better for builds###
                pygame.draw.rect(window, YELLOW, (spot.location[0]-6, spot.location[1]-6, 24*3+12, 24*4+12))
            if spot.side == "Back":
                window.blit(back, spot.location)
            else:
                paintCard(spot.card, spot.location)




######## stuff to draw onto the screen at different times (not the cards) ############

def buildNametags():
    for i in range(4):
        if buildRankDict[i] != 0:
            nametag = pygame.font.Font('freesansbold.ttf', 18)
            tag = nametag.render("Build: "+str(buildRankDict[i]), True, BEIGE, GREEN)
            tagRectObj = tag.get_rect()
            tagRectObj.topleft = ((24*(i*4+25)),24*8)
            window.blit(tag, tagRectObj)


def buildScore(player1, player2):
    #who is top and bottom
    if player1.side == "top":
        p1 = player1
        p2 = player2
    else:
        p1 = player2
        p2 = player1

    #write in their current total scores
    players = [p1, p2]
    scoreFont = pygame.font.Font('freesansbold.ttf', 22)
    for i in range(2):
        score = scoreFont.render(players[i].name+"'s Score: "+str(players[i].totalPoints), True, BLUE, GREEN)
        scoreRectObj = score.get_rect()
        scoreRectObj.topleft = (24*4,24*(i*1.5+1.5))
        window.blit(score, scoreRectObj)

    #add in who is the dealer this turn
    if p1.position == "dealer":
        d = 0
    else:
        d = 1

    dealerFont = pygame.font.Font('freesansbold.ttf', 13)
    dealer = dealerFont.render("(Dealer)", True, BLUE, GREEN)
    dealerRectObj = dealer.get_rect()
    dealerRectObj.topleft = (24*1.7,24*(d*1.5+1.7))
    window.blit(dealer, dealerRectObj)


def buildFinalScore(player1, player2):
    pygame.draw.rect(window, BEIGE, (24*16, 24*10, 24*13, 24*7))
    #who is top and bottom
    if player1.side == "top":
        p1 = player1
        p2 = player2
    else:
        p1 = player2
        p2 = player1

    #write in their current total scores
    players = [p1, p2]
    scoreFont = pygame.font.Font('freesansbold.ttf', 30)
    for i in range(2):
        score = scoreFont.render(players[i].name+"'s Score: "+str(players[i].totalPoints), True, RED, BEIGE)
        scoreRectObj = score.get_rect()
        scoreRectObj.topleft = (24*16.5,24*(i*2+13))
        window.blit(score, scoreRectObj)

    if p1.totalPoints == p2.totalPoints:
        result = "It's a tie!"
    elif p1.totalPoints > p2.totalPoints:
        result = p1.name+" Wins!"
    else:
        result = p2.name+" Wins!"

    win = scoreFont.render(result, True, RED, BEIGE)
    winRectObj = score.get_rect()
    winRectObj.topleft = (24*16.5,24*11)
    window.blit(win, winRectObj)


def buildMoveType(moveType):
        moveTypeFont = pygame.font.Font('freesansbold.ttf', 18)
        moveTypeText = moveTypeFont.render(moveType, True, YELLOW, GREEN)
        moveTypeRect = moveTypeText.get_rect()
        moveTypeRect.center = (540, 552)      
        window.blit(moveTypeText, moveTypeRect)


def buildIllegalMove(illegalMove):
        if illegalMove == "badMath":
            warning = "That move is illegal, please try again"
        elif illegalMove == "noHandCard":
            warning = "Please play a card from your hand"
        elif illegalMove == "noTableCards":
            warning = "Please select cards from the table"
        elif illegalMove == "noMoveType":
            warning = "Please indicate the type of move"
        elif illegalMove == "noBuildRank":
            warning = "Please select a rank to build to"
        badFont = pygame.font.Font('freesansbold.ttf', 23)
        badText = badFont.render(warning, True, RED, GREEN)
        badRect = badText.get_rect()
        badRect.center = (540, 24*22)      
        window.blit(badText, badRect)

def buildLast():
        lastFont = pygame.font.Font('freesansbold.ttf', 30)
        lastText = lastFont.render("L A S T", True, YELLOW, GREEN)
        lastRect = lastText.get_rect()
        lastRect.center = (540, 24*6)      
        window.blit(lastText, lastRect)

def buildInstructions():
    pygame.draw.rect(window, RED, (24*1.7, 24*22.7, 24*11.6, 24*5.3))
    insFont = pygame.font.Font('freesansbold.ttf', 14)
    ins1 = insFont.render("Click on cards from the table and in", True, BEIGE, RED)
    ins1RectObj = ins1.get_rect()
    ins1RectObj.topleft = (24*2,24*23)
    window.blit(ins1, ins1RectObj)

    ins2 = insFont.render("your hand to select or unselect them.", True, BEIGE, RED)
    ins2RectObj = ins2.get_rect()
    ins2RectObj.topleft = (24*2,24*23.8)
    window.blit(ins2, ins2RectObj)

    ins3 = insFont.render("Type <d> to discard, <t> to take, and", True, BEIGE, RED)
    ins3RectObj = ins3.get_rect()
    ins3RectObj.topleft = (24*2,24*24.6)
    window.blit(ins3, ins3RectObj)

    ins4 = insFont.render("<b> to build. Once you are satisfied", True, BEIGE, RED)
    ins4RectObj = ins4.get_rect()
    ins4RectObj.topleft = (24*2,24*25.4)
    window.blit(ins4, ins4RectObj)

    ins5 = insFont.render("with your move type and selections,", True, BEIGE, RED)
    ins5RectObj = ins5.get_rect()
    ins5RectObj.topleft = (24*2,24*26.2)
    window.blit(ins5, ins5RectObj)

    ins6 = insFont.render("press Enter.", True, BEIGE, RED)
    ins6RectObj = ins6.get_rect()
    ins6RectObj.topleft = (24*2,24*27)
    window.blit(ins6, ins6RectObj)

def textForCard(card):
    if card.rank == 1:
        n = "Ace"
    elif card.rank == 11:
        n = "Jack"
    elif card.rank == 12:
        n = "Queen"
    elif card.rank == 13:
        n = "King"
    else:
        n = str(card.rank)

    if card.suit == "c":
        s = "Clubs"
    elif card.suit == "d":
        s = "Diamonds"
    elif card.suit == "h":
        s = "Hearts"
    else:
        s = "Spades"

    return n+" of "+s


def buildComputerMove(tup,moveType):
    if moveType == "Discard":
        first = "The computer discarded:"
        second = textForCard(tup[0])
    else:
        first = "The computer took:"
        second = ""
        for card in tup[1]:
            second += textForCard(card)+", "
        if tup[2] > 0:
            second += "the built "+str(tup[2])+"s"
        third = "With the:"
        fourth = textForCard(tup[0])
        
    pygame.draw.rect(window, BEIGE, (24*31, 24*1, 24*11, 24*6))
    insFont = pygame.font.Font('freesansbold.ttf', 18)
    ins1 = insFont.render(first, True, RED, BEIGE)
    ins1RectObj = ins1.get_rect()
    ins1RectObj.center = (24*37,24*2)
    window.blit(ins1, ins1RectObj)

    ins2 = insFont.render(second, True, RED, BEIGE)
    ins2RectObj = ins2.get_rect()
    ins2RectObj.center = (24*37,24*3)
    window.blit(ins2, ins2RectObj)

    if moveType != "Discard":
        ins3 = insFont.render(third, True, RED, BEIGE)
        ins3RectObj = ins3.get_rect()
        ins3RectObj.center = (24*37,24*5)
        window.blit(ins3, ins3RectObj)

        ins4 = insFont.render(fourth, True, RED, BEIGE)
        ins4RectObj = ins4.get_rect()
        ins4RectObj.center = (24*37,24*6)
        window.blit(ins4, ins4RectObj)


buildChoicesDict = {}

def buildBuildChoices(player):
    x = rankChoices4Build(player)[:]
    x.sort()
    i = 0
    for rank in x:
        buildChoicesDict[i] = rank
        i += 1

    buildTypeFont = pygame.font.Font('freesansbold.ttf', 23)

    buildTypeFont0 = pygame.font.Font('freesansbold.ttf', 20)
    buildTypeText0 = buildTypeFont0.render("What do you want to build to?", True, BEIGE, GREEN)
    buildTypeRect0 = buildTypeText0.get_rect()
    buildTypeRect0.topleft = (24*31.5,24*23.5)       
    window.blit(buildTypeText0, buildTypeRect0)

    if len(buildChoicesDict) > 0:
        pygame.draw.rect(window, GREEN, (24*33, 24*25, 24*1.3, 24*1))
        buildTypeText = buildTypeFont.render(str(buildChoicesDict[0]), True, BEIGE, GREEN)
        buildTypeRect = buildTypeText.get_rect()
        buildTypeRect.midtop = (24*33.6,24*25)       
        window.blit(buildTypeText, buildTypeRect)

    if len(buildChoicesDict) > 1:
        pygame.draw.rect(window, GREEN, (24*35, 24*25, 24*1.3, 24*1))
        buildTypeText1 = buildTypeFont.render(str(buildChoicesDict[1]), True, BEIGE, GREEN)
        buildTypeRect1 = buildTypeText1.get_rect()
        buildTypeRect1.midtop = (24*35.6,24*25)       
        window.blit(buildTypeText1, buildTypeRect1)

    if len(buildChoicesDict) > 2:
        pygame.draw.rect(window, GREEN, (24*37, 24*25, 24*1.3, 24*1))
        buildTypeText2 = buildTypeFont.render(str(buildChoicesDict[2]), True, BEIGE, GREEN)
        buildTypeRect2 = buildTypeText2.get_rect()
        buildTypeRect2.midtop = (24*37.6,24*25)       
        window.blit(buildTypeText2, buildTypeRect2)

    if len(buildChoicesDict) > 3:
        pygame.draw.rect(window, GREEN, (24*39, 24*25, 24*1.3, 24*1))
        buildTypeText3 = buildTypeFont.render(str(buildChoicesDict[3]), True, BEIGE, GREEN)
        buildTypeRect3 = buildTypeText3.get_rect()
        buildTypeRect3.midtop = (24*39.6,24*25)       
        window.blit(buildTypeText3, buildTypeRect3)

def selectBuildChoice(rank):
    for key in buildChoicesDict.keys():
        if buildChoicesDict[key] == rank:
            pygame.draw.rect(window, YELLOW, (24*(33+key*2)-6, 24*25-6, 24*1.3+12, 24*1+12))


### Interactive Logic  ###

def getMoveAndCard():
    for spot in cardSpots[:4]:
        if spot.selected:
            return (moveType, spot.card)
    return (moveType, None)


def getTableCards():
    selectedTableCards = []
    for spot in cardSpots[8:22]:
        if spot.selected:
            selectedTableCards.append(spot.card)
    return selectedTableCards


def getSelectedBuildRank(): 
    if cardSpots[22].selected:
        return buildRankDict[0]
    elif cardSpots[32].selected:
        return buildRankDict[1]
    elif cardSpots[42].selected:
        return buildRankDict[2]
    elif cardSpots[52].selected:
        return buildRankDict[3]
    else:
        return 0


buildChoicesSpots = {0: (24*33,24*25), 1: (24*35,24*25), 2: (24*37,24*25), 3: (24*39,24*25)}

def buildFromCoordinates(x, y):
    for build in buildChoicesSpots.keys():
        if (buildChoicesSpots[build][0] < x < buildChoicesSpots[build][0]+24*2) and (buildChoicesSpots[build][1] < y < buildChoicesSpots[build][0]+24):
            return build
    return None




############   GAME LOGIC  ##############


class Card():
        def __init__(self, rank, suit):
                self.rank = rank
                self.suit = suit
                if rank > 9:
                        self.faceCard = True
                else:
                        self.faceCard = False


suits = ["c","s","h","d"]
                
class Deck():
        def __init__(self):
                self.remaining = []
                for s in suits:
                        for i in range(1, 14):
                                self.remaining.append(Card(i, s))
                self.played = []

        def shuffle(self):
                random.shuffle(self.remaining)

        def draw(self):
                if self.count() == 0:
                        return "Sorry, your deck is empty, there are no cards to be drawn."
                drawnCard = self.remaining.pop()
                self.played.append(drawnCard)
                return drawnCard

        def count(self):
                return len(self.remaining)


class Player():
        #life="computer" or "human", positon="dealer" or "player", side="top" or "bottom"
        def __init__(self, name, life, position, side):
                self.name = name
                self.life = life
                self.side = side
                self.position = position
                if self.position == 'dealer':
                        self.turn = False
                else:
                        self.turn = True
                self.hand = []
                self.currentBuilds = []
                self.pile = []
                self.totalPoints = 0    


        #to calculate points at the end of a round
        def calculatePoints(self):
                points = 0

                #most cards#
                if len(self.pile) > 26:
                        points += 3
                elif len(self.pile) == 26:
                        points += 1.5

                #most spades#
                spadeCount = 0
                for card in self.pile:
                        if card.suit == "s":
                                spadeCount += 1
                if spadeCount > 6:
                        points += 1

                #Aces, big casino, little casino
                for card in self.pile:
                        if card.rank == 1:
                                points += 1
                        elif card.rank == 2 and card.suit == "s":
                                points += 1
                        elif card.rank == 10 and card.suit == "d":
                                points += 2

                return points


class Table():
        def __init__(self):
                self.allCards = []
                self.builds = {} #format: key: 7, value: [card, card, card]

        def availableCards(self):
                captured = []
                for builds in self.builds.values():
                        captured += builds

                availableCards = []
                for card in self.allCards:
                        if card not in captured:
                                availableCards.append(card)
                
                return availableCards   

        def removeCard(self, card):
                self.allCards.remove(card)
                
        def removeBuild(self, rank):
                if rank in self.builds.keys():
                        for card in self.builds[rank]:
                            #print textForCard(card)
                            self.allCards.remove(card)
                del self.builds[rank]
                


## Move classes & subclasses ## - 3 types of moves: Discard, Take, Build


def takeLastCards(currentTable, player):
    for card in currentTable.allCards:
        player.pile.append(card)
    for card in currentTable.allCards:
        currentTable.removeCard(card)


def multiplesCheck(rank, cards): #this checks if a set of cards could be legaly taken by a card of rank "rank"
        #no set can be bigger than how many cards there are or how high the rank is
        if rank > 10: #face cards can only take other cards of the same rank (but as many as they want)
            for card in cards:
                if card.rank != rank:
                    return False
            return True

        maxLen = min(rank, len(cards))
        size = 1
        cardsLeft = cards[:]
        setsDone = []
        while len(cardsLeft) >= size:
                #print cardsLeft
                #print "size = "+str(size)
                possibilities = list(itertools.combinations(cardsLeft, size))
                #print "possibilities - "+str(possibilities)
                found = False
                for choice in possibilities:
                        group = list(choice) #wtf was happening??
                        groupRanks = [card.rank for card in group]
                        if sum(groupRanks) == rank:
                                setsDone.append(group)
                                for i in range(len(group)):
                                        #print "group - "+str(group)
                                        #print group[i]
                                        cardsLeft.remove(group[i])
                                found = True
                                size = 1
                                break
                if found == False:
                    size +=1

                
        if len(cardsLeft) == 0:
                return True
        else:
                return False




class Move():
        def __init__(self, currentTable, cardPlayed, player, player2, tableCards=[], buildRank=0):
                self.currentTable = currentTable
                self.cardPlayed = cardPlayed
                self.player = player
                self.player2 = player2
                self.tableCards = tableCards #this is a list of all of the cards
                        #to be involved in the move that are already on the table,
                        #it would be empty on a discard move
                        #cards in a build on the table are figured out elsewhere based on the build's rank
                self.buildRank = buildRank

class Discard(Move):
        def execute(self):
                self.currentTable.allCards.append(self.cardPlayed)
                self.player.hand.remove(self.cardPlayed)

        def legal(self):
                if len(self.player.currentBuilds) == 0:
                        return True
                return False

class TakeCards(Move):
        def execute(self):
                for card in self.tableCards:
                        #print textForCard(card)
                        self.currentTable.allCards.remove(card)
                        self.player.pile.append(card)

                self.player.hand.remove(self.cardPlayed)
                self.player.pile.append(self.cardPlayed)
                
                if self.buildRank != 0:
                    for card in self.currentTable.builds[self.buildRank]:
                            self.player.pile.append(card)
                    if self.buildRank in self.player.currentBuilds:
                        self.player.currentBuilds.remove(self.buildRank)
                    else:
                        self.player2.currentBuilds.remove(self.buildRank)
                    self.currentTable.removeBuild(self.buildRank)   

        def legal(self):
            if self.buildRank > 0:
                buildCardsTaken = self.currentTable.builds[self.buildRank]
            else:
                buildCardsTaken = []
            return multiplesCheck(self.cardPlayed.rank, self.tableCards+[self.cardPlayed]+buildCardsTaken)


class Build(Move):                               
        def legal(self):
            return multiplesCheck(self.buildRank, self.tableCards+[self.cardPlayed])


        def execute(self):
                if self.buildRank not in self.player.currentBuilds: #for if its a new build
                    self.player.currentBuilds.append(self.buildRank) #add it to the player's list of current builds
                    self.currentTable.builds[self.buildRank] = [] #start the build in the table object

                self.currentTable.builds[self.buildRank] += self.tableCards[:]+[self.cardPlayed]
                self.currentTable.allCards.append(self.cardPlayed)              
                self.player.hand.remove(self.cardPlayed)
                


def rankChoices4Build(player):
    choices = set()
    for card in player.hand:
        #if card != cardPlayed:  #implement this somehow later!
        if card.rank < 11:
            choices.add(card.rank)
    return list(choices)
    
        
################  COMPUTER STRATEGY  #################   

###NEEDS FIXNG!!!!!!!###

def cardsValue(cardList): #just the opposite of this for discards
    points = 0
    for card in cardList:
        points += 0.111 #just for being a card  -->  3/27 because 27 cards gets you 3 points
        if card.suit == "s":
            points += 0.143 # --> 1/7 because 7 spades gets you 1 point
            if card.rank == 2:
                points += 1
        elif card.suit == "d" and card.rank == 10:
            points += 2
        if card.rank == 1:
            points += 1
    return points

def discardValue(card):
    return cardsValue([card])

def getComputerMove(player, table):
    discardChoices = player.hand[:]
    takeChoices = {}
    #buildChoices = []
    buildRank = 0
    
    allCardCombinations = []
    for i in range(1,len(table.availableCards())+1):
        allCardCombinations += list(itertools.combinations(table.availableCards(),i))
        
    takePossible = False

    for card in player.hand:
        takeChoices[card] = []
        cardCanTake = False
        for combination in allCardCombinations:
            if multiplesCheck(card.rank, list(combination)):
                takeChoices[card].append(list(combination))
                takePossible = True
                cardCanTake = True
                
        if card.rank in table.builds.keys():
            cardCanTake = True
            takePossible = True
            takeChoices[card].append([])
            for combo in takeChoices[card]:
                combo += table.builds[card.rank]

        if cardCanTake == False:
            del takeChoices[card]
    
    if takePossible == False:
        return ("Discard", (min(discardChoices, key=discardValue), [],0))

    else:
        flattenedTakeChoices = []
        for Hcard in takeChoices.keys():
            for combo in takeChoices[Hcard]:
                flattenedTakeChoices.append([Hcard]+combo)
        move = max(flattenedTakeChoices, key=cardsValue)
        if move[0].rank in table.builds.keys():
            buildRank = move[0].rank
        return ("Take", (move[0], [i for i in move if i in table.availableCards()], buildRank))




############  GAME PLAY & MAIN LOOP  #############

## Global Variables (is that what I mean?) ##

gameState = "prep"  #"prep", "gettingMove", "gameOver"
gameNumber = 0 #0-3
handNumber = 0 #0-5
turnNumber = 0 #0-7
firstTime = True
                
deck = Deck()
deck.shuffle()
table = Table()

player1 = Player("Alicia", "human", "player", "bottom")
player2 = Player("Computer", "computer", "dealer", "top")

moveType = None
showBuildChoices = False

computerMoveType = None
computerMove = None
tup = None

buildRank = 0
illegalMove = False

p1Last = 0
p2Last = 0


##--##--##--##
    

while True: # main game loop
    #print gameState
        
    if gameState == "waitGM":
        gameState = "gettingMove"
    elif gameState == "waitP":
        gameState= "prep"
    elif gameState == "waitGO":
        pygame.time.wait(4000)
        gameState = "gameOver"
    elif gameState == "waitCM":
        gameState = "computerMove"
    elif gameState == "displayCM":
        pygame.time.wait(1000)
        if turnNumber == 7:
            gameState = "waitP"
            turnNumber = 0
            if handNumber == 5:
                gameState = "last"
            else:
                handNumber += 1
        else:
            turnNumber += 1
            gameState = "waitGM"
    elif gameState == "waitCM2":
        gameState = "displayCM"

    
    if gameState == "prep":
        if handNumber == 0:
            for i in range(4):
                table.allCards.append(deck.draw())

            dealToTableUI(table.allCards)

        #on all 6 hands, deal 4 cards to each player
        for i in range(4):
            player1.hand.append(deck.draw())
            player2.hand.append(deck.draw())

        populateHandsUI(player1, player2)
        
        gameState = "waitGM"
       

#----------- drawing stuff onto the screen -------------#

    window.fill(GREEN)
    buildScore(player1, player2)
    buildInstructions()
    
    if firstTime == False:
        buildComputerMove(tup, computerMoveType)
    
    if turnNumber % 2 == 0 and gameState == "gettingMove":
        if moveType != None:
            buildMoveType(moveType)
        if illegalMove != False:
            buildIllegalMove(illegalMove)

    if moveType == "Build":
        if buildRank > 0:
            selectBuildChoice(buildRank)
            selectBuildChoice(buildRank)
        buildBuildChoices(player1)

    if handNumber == 5:
        buildLast()

    if gameState == "last":
        #print "cards on the table: "+str(len(table.allCards))
        if p1Last > p2Last: #I tried to do this by saying lastPlayer = player1 or 2, but the score didn't get added
            selectLastCardsUI(player1)
            takeLastCards(table, player1)
        else:
            selectLastCardsUI(player2)
            takeLastCards(table, player2)
        gameState = "waitGO"

    if gameState == "gameOver":
        player1.totalPoints += player1.calculatePoints()
        player1.pile = []
        player2.totalPoints += player2.calculatePoints()
        player2.pile = []
        buildFinalScore(player1, player2)

        
    else:
        buildNametags()
        paintAllCards()


    if gameState == "displayCM": #here is when we actually execute the move
        if computerMoveType == "Discard":
            computerMove = Discard(table, tup[0], player2, player1)
            discardUI(tup[0])
        else:
            computerMove = TakeCards(table, tup[0], player2, player1, tup[1], tup[2])
            takeFromTableUI(tup[0], tup[1]) #hand card, table card list
            if tup[2] > 0:
                takeBuildUI(tup[2])
                for i in range(4): #reset this build spot to have nothing in it.
                    if buildRankDict[i] == tup[2]:
                        buildRankDict[i] = 0


            if handNumber == 5:
                p2Last = turnNumber
                    
        computerMove.execute()
        for spot in cardSpots:
            spot.unselect()

    if  turnNumber % 2 != 0 and gameState == "computerMove":
            #this is the other player's turn. For now it'll be a computer
            computerMoveType, tup = getComputerMove(player2, table)

            toSelect = [tup[0]]+tup[1]
            if tup[2] > 0:
                toSelect += table.builds[tup[2]]
            for spot in cardSpots:
                if spot.card in toSelect:
                    spot.select()
                if spot.card == tup[0]:
                    spot.side = "Front"
                
            firstTime = False
            gameState = "waitCM2"



#----------- going through the mouse clicks and key presses -------------#    
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()



        if gameState == "gettingMove" and turnNumber % 2 == 0:
            if (event.type == KEYDOWN and event.key == K_d):
                moveType = "Discard"
                illegalMove = False
            elif (event.type == KEYDOWN and event.key == K_t):
                moveType = "Take"
                illegalMove = False
            elif (event.type == KEYDOWN and event.key == K_b):
                moveType = "Build"
                showBuildChoices = True
                illegalMove = False



            elif (event.type == KEYUP and (event.key == K_KP_ENTER or event.key == K_RETURN)):                
                moveType, cardPlayed = getMoveAndCard()
                if cardPlayed == None:
                    illegalMove = "noHandCard"

                else:
                    if moveType == "Discard":
                        move = Discard(table, cardPlayed, player1, player2)

                    elif moveType == "Take":
                        tableCardList = getTableCards()
                        buildTaken = getSelectedBuildRank()          

                        if tableCardList == [] and buildTaken == 0: #if they didn't select any cards to take
                            illegalMove = "noTableCards"
                        else:
                            move = TakeCards(table, cardPlayed, player1, player2, tableCardList, buildTaken)
                            
                            if handNumber == 5:
                                p1Last = turnNumber

                    elif moveType == "Build":
                        tableCardList = getTableCards()
##
##                        if tableCardList == []: #if they didn't select any cards to take
##                            illegalMove = "noTableCards"
                        if True:
                            if buildRank == 0:
                                illegalMove = "noBuildRank"
                            else:
                                move = Build(table, cardPlayed, player1, player2, tableCardList, buildRank)

                                if handNumber == 5:
                                    p1Last = turnNumber                    
                        
                    if moveType != None and illegalMove == False:
                        if move.legal():
                            if moveType == "Discard":
                                discardUI(cardPlayed)
                            elif moveType == "Take":
                                takeFromTableUI(cardPlayed, tableCardList)
                                if buildTaken > 0:
                                    takeBuildUI(buildTaken)
                                    for i in range(4): #reset this build spot to have nothing in it.
                                        if buildRankDict[i] == buildTaken:
                                            buildRankDict[i] = 0
                            elif moveType == "Build":
                                if buildRank not in buildRankDict.values(): #create the build in the dictionary if its new
                                    for i in range(4): 
                                        if buildRankDict[i] == 0:
                                            buildRankDict[i] = buildRank
                                            break
                                addToBuildUI(cardPlayed, tableCardList, buildRank)
                                buildRank = 0
                                buildChoicesDict = {}

                            move.execute()
                            turnNumber += 1
                            gameState = "waitCM"
                            
                        else:
                            illegalMove = "badMath"
                            
                    if moveType == None:
                        illegalMove = "noMoveType"
                for spot in cardSpots:
                    spot.unselect()
                moveType = None
                        
            
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                spot = spotFromCoordinates(mousex, mousey)
                if spot != None:
                    if spot.card != None:
                            illegalMove = False
                            if spot.selected == True:
                                spot.unselect()
                            else:
                                spot.select()
                else:
                    buildChoiceSpot = buildFromCoordinates(mousex, mousey)
                    if buildChoiceSpot != None:
                        if buildChoicesDict[buildChoiceSpot] != None:
                            buildRank = buildChoicesDict[buildChoiceSpot]
                        
    pygame.display.update()

