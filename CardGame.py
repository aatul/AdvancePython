import random


class Player:
    global Deck

    def __init__(self, name):
        self.PlayerDeck = Deck
        random.shuffle(self.PlayerDeck)
        self.Hand = self.PlayerDeck[0:5]
        self.Wins = []
        self.Name = name

    def Reset(self):
        self.PlayerDeck = Deck
        random.shuffle(self.PlayerDeck)
        self.Hand = self.PlayerDeck[0:5]
        self.Wins = []

    def CheckWin(self):
        for i in range(len(self.Wins)):
            if len(self.Wins[i]) == 3:
                print(self.Name + " Wins!")
    
    def PrintHand(self):
        for i in self.Hand:
            print("[" + i.Type + ", " + str(i.Power) + ", " + i.Colour + "]")


class Card:
    def __init__(self, type, power, colour):
        self.Type = type
        self.Power = power
        self.Colour = colour


# Checks a card vs the players current winning cards and creates groups of potential round winning sets
def AddToWins(card, player):
    if len(player.Wins) == 0:
        player.Wins += [[card]]
        return
    for i in range(len(player.Wins)):
        for k in range(len(player.Wins[i])):
            if card[0] != player.Wins[i][k][0] and card[1] != player.Wins[i][k][1]:
                player.Wins[i] += [card]
            else:
                player.Wins += [[card]]
    player.CheckWin()


# Returns Winning Card or False if tie
def Battle(c1, c2):
    if c1.type == c2.type:
        if c1.power > c2.power:
            return c1
        if c1.power < c2.power:
            return c2
        if c1.power == c2.power:
            return False
    if (c1.type == "F" and c2.type == "S") or (c1.type == "W" and c2.type == "F") or (c1.type == "S" and c2.type == "W"):
        return c1
    else:
        return c2


Deck = [Card("F", 3, "Blue"), Card("F", 6, "Purple"),
        Card("F", 2, "Yellow"), Card("S", 3, "Orange"),
        Card("S", 2, "Red"), Card("S", 7, "Yellow"),
        Card("W", 5, "Blue"), Card("W", 2, "Green"),
        Card("W", 4, "Purple")]


player = Player("Nathan")
AI = Player("AI")

player.PrintHand()
AI.PrintHand()