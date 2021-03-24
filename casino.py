import random

# Card Value
# 1: Ace
# 2 - 10: 2 - 10
# 11: Jack
# 12: Queen
# 13: King
# Suits
# H: Hearts
# D: Diamonds
# C: Clubs
# S: Spades


class Cards:

    def __init__(self):
        self.cardsList = []
        for x in range(1, 14):
            card = x
            for i in range(4):
                if i == 0:
                    suit = 'H'
                elif i == 1:
                    suit = 'D'
                elif i == 2:
                    suit = 'C'
                elif i == 3:
                    suit = 'S'

                self.cardsList.append([card, suit])

        self.cardsList *= 4

    def getCards(self):
        return self.cardsList


class Dealer:

    def __init__(self, c):
        # 4 decks
        self.currentVal = 0
        self.cardsList = c
        self.cards = []

    def deal(self):
        row1 = random.randint(0, len(self.cardsList) - 1)
        randCard = self.cardsList[row1]
        self.cardsList.pop(row1)
        self.cards.append(randCard)

        row2 = random.randint(0, len(self.cardsList) - 1)
        randCard2 = self.cardsList[row2]
        self.cardsList.pop(row2)
        self.cards.append(randCard2)

        self.decision()
        return self.cards

    def decision(self):
        value = 0

        if self.cards[0][0] == 1 and self.cards[1][0] == 1:
            value = 2
        else:

            if self.cards[0][0] == 11 or self.cards[0][0] == 12 or self.cards[0][0] == 13:
                value += 10
            else:
                value += self.cards[0][0]

            if self.cards[1][0] == 11 or self.cards[1][0] == 12 or self.cards[1][0] == 13:
                value += 10
            else:
                value += self.cards[1][0]

        self.currentVal = value

        if value == 1 and (self.cards[0][0] == 1 or self.cards[1][0] == 1):
            self.currentVal = 21
            return self.currentVal
        elif value < 17:
            self.hit()
        else:
            return self.currentVal

    def hit(self):
        value = 0
        rand = random.randint(1, len(self.cardsList))
        card = self.cardsList[rand]
        self.cards.append(card)
        self.cardsList.pop(rand)

        if card[0] == 11 or card[0] == 12 or card[0] == 13:
            value = 10
        elif card[0] == 1 and self.currentVal == 10:
            value = 11
        elif card[0] == 1 and self.currentVal < 11:
            value = 11
        elif card[0] == 1 and self.currentVal == 20:
            value = 1
        else:
            value = card[0]

        self.currentVal += value

        if self.currentVal < 17:
            self.hit()
        elif self.currentVal > 21:
            return self.currentVal
        else:
            return self.currentVal

    def getScore(self):
        return self.currentVal

    def reset(self):
        self.cards = []
        self.currentVal = 0


class PLayer:

    def __init__(self, c):
        self.cardsList = c
        self.cards = []
        self.currentVal = 0

    def deal(self):
        row1 = random.randint(0, len(self.cardsList) - 1)
        randCard = self.cardsList[row1]
        self.cardsList.pop(row1)
        self.cards.append(randCard)

        row2 = random.randint(0, len(self.cardsList) - 1)
        randCard2 = self.cardsList[row2]
        self.cardsList.pop(row2)
        self.cards.append(randCard2)

        self.cardsList = self.cardsList
        value = 0

        if self.cards[0][0] == 11 or self.cards[0][0] == 12 or self.cards[0][0] == 13:
            value += 10
        else:
            value += self.cards[0][0]

        if self.cards[1][0] == 11 or self.cards[1][0] == 12 or self.cards[1][0] == 13:
            value += 10
        else:
            value += self.cards[1][0]

        self.currentVal = value

        if value == 11 and (self.cards[0][0] == 1 or self.cards[1][0] == 1):
            self.currentVal = 21

        return self.cards

    def hit(self):
        value = 0
        rand = random.randint(1,len(self.cardsList))
        card = self.cardsList[rand]
        self.cards.append(card)
        self.cardsList.pop(rand)

        if card[0] == 11 or card[0] == 12 or card[0] == 13:
            value = 10
        elif card[0] == 1 and self.currentVal == 10:
            value = 11
        elif card[0] == 1 and self.currentVal < 11:
            value = 11
        elif card[0] == 1 and self.currentVal == 20:
            value = 1
        else:
            value = card[0]

        self.currentVal += value
        if self.currentVal > 21 and self.cards.__contains__(1):
            if self.cards.count(1) == 1:
                if self.currentVal - 10 < 22:
                    self.currentVal = self.currentVal - 10

        return card

    def getScore(self):
        return self.currentVal


c = Cards()
deck = c.getCards()
d = Dealer(deck)
p = PLayer(deck)