### ------- Computer Player (how to know which move to make) -------- ###

import itertools
from CasinoLogic import multiplesCheck

##TO DO##
#-Allow the computer to build
#-Have the computer think ahead, like throwing a 4 if you have another 4 to take it with
#-Have the computer be smart about LAST (ex. holding on to face cards until the end)


def cardsValue(cardList): #counts up how valuable a list of cards would be if you took it
    points = 0
    for card in cardList:
        points += 0.111 #just for being a card  -->  3/27 because 27 cards gets you 3 points
        if card.suit == "s":
            points += 0.143 # --> 1/7 because 7 spades gets you 1 point
            if card.rank == 2:
                points += 1
        elif card.suit == "d" and card.rank == 10: #the big casino
            points += 2
        if card.rank == 1: #the little casino
            points += 1
    return points

def discardValue(card): #if you're trying to decide what card to discard, use this to find out what a card's value is, and then minimize over it
    return cardsValue([card])

def getComputerMove(player, table):
    '''this function returns a tuple with (0) the type of move followed by (1) a tuple with:
        (0) the card to be played from the hand
        (1) the list of cards from the table to play
        (2) what build, if any, is involved'''
    
    discardChoices = player.hand[:] #you could discard any card in your hand
    takeChoices = {} #this will get populated with different possibilites for what to take
    #buildChoices = []
    buildRank = 0
    
    allCardCombinations = []
    for i in range(1,len(table.availableCards())+1):
        allCardCombinations += list(itertools.combinations(table.availableCards(),i))
        
    takePossible = False #if this stays False, we'll discard

    for card in player.hand: #here we go through each card in the hand to see what cards from the table it could take
        takeChoices[card] = []
        cardCanTake = False
        for combination in allCardCombinations:
            if multiplesCheck(card.rank, list(combination)): #if that combination would be a legal move to take with a card of this rank
                takeChoices[card].append(list(combination)) #put it in the list
                takePossible = True #which means we can take (don't have to discard)...
                cardCanTake = True #...and more specifically: that card from the hand can take
                
        if card.rank in table.builds.keys(): #if the card from the hand is the same rank as something currently being built
            cardCanTake = True #we could take it
            takePossible = True
            takeChoices[card].append([]) #put another move into the list of ways to take cards with this card
                                        #its empty for now because each possiblity will get the build added to it
                                        #so there will be one take choice that is just taking the build
            for combo in takeChoices[card]:
                combo += table.builds[card.rank]

        if cardCanTake == False:
            del takeChoices[card] #we can get rid of the blank dictionary entry if it turns out that card couldn't actually take anything
    
    if takePossible == False:
        return ("Discard", (min(discardChoices, key=discardValue), [],0)) #discard the least valuable card

    else:
        flattenedTakeChoices = []
        for Hcard in takeChoices.keys(): #of all the cards you can take with,
            for combo in takeChoices[Hcard]: #for each set of table cards that was takeable,
                flattenedTakeChoices.append([Hcard]+combo) #make a new list that has all of those table cards plus the card from your hand
                                                            #because this is the entire set that will get added to our pile, so we want to maximize those points 
        move = max(flattenedTakeChoices, key=cardsValue)
        if move[0].rank in table.builds.keys():
            buildRank = move[0].rank
        return ("Take", (move[0], [i for i in move if i in table.availableCards()], buildRank)) #move[0] is the card from the hand
                                                                                                #the list comprehension makes sure to leave out the build cards


