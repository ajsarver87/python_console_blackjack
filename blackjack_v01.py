import random

# initialize the one deck
suits = ['D', 'H', 'S', 'C']
numbers = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
full_deck = []

for suit in suits:
    for number in numbers:
        card = suit + number
        full_deck.append(card)

value_lookup_dictionary = {}

for card in full_deck:
    temp_value = 0
    if card[1] == '2':
        temp_value = 2
    elif card[1] == '3':
        temp_value = 3
    elif card[1] == '4':
        temp_value = 4
    elif card[1] == '5':
        temp_value = 5
    elif card[1] == '6':
        temp_value = 6
    elif card[1] == '7':
        temp_value = 7
    elif card[1] == '8':
        temp_value = 8
    elif card[1] == '9':
        temp_value = 9
    elif card[1] in ['J','Q','K','T']:
        temp_value = 10
    elif card[1] == 'A':
        temp_value = 11
    else:
        temp_value = 10

    value_lookup_dictionary[card] = temp_value

#Player Class
class Player:
    def __init__(self):
        self.money = 1000
        self.hand = []

    def calc_hand_value(self):
        value = 0
        for card in self.hand:
            value += value_lookup_dictionary.get(card)
        return value

#Dealer Class
class Dealer:
    def __init__(self):
        self.hand = []

    def calc_hand_value(self):
        value = 0
        for card in self.hand:
            value += value_lookup_dictionary.get(card)
        return value

#Fuction for initial Deal
def inital_deal(player, dealer):
    player.hand.append(deck.pop(0))
    dealer.hand.append(deck.pop(0))
    player.hand.append(deck.pop(0))
    dealer.hand.append(deck.pop(0))

#Function to print Hand Values
def print_hand_value(hand):
    suit_dict = {'H':'Hearts', 'S':'Spades', 'C':'Clubs', 'D':'Diamonds'}
    value_dict = {'A':'Ace', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine', 'T':'Ten', 'J':'Jack', 'Q':'Queen', 'K':'King'}
    for card in hand:
        suit = suit_dict.get(card[0])
        value = value_dict.get(card[1])
    print('{value} of {suit}'.format(value = value, suit = suit))


deck = full_deck
random.shuffle(deck)

player = Player()
dealer = Dealer()

inital_deal(player = player, dealer = dealer)
print_hand_value(player.hand)
print_hand_value(dealer.hand)

if player.calc_hand_value() > dealer.calc_hand_value():
    print('Player Wins!')
else:
    print('Dealer Wins!')



