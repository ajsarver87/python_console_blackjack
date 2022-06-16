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

        for card in self.hand:
            if card[1] == 'A' and value > 21:
                value = 0
                for card in self.hand:
                    if card[1] == 'A':
                        value += 1
                    else:
                        value += value_lookup_dictionary.get(card)
        return value

    def hit(self):
        self.hand.append(deck.pop(0))

    def clear_hand(self):
        self.hand = []

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

player = Player()
dealer = Player()

while player.money > 0:
    bet = int(input('You have ${money}.  How much would you like to bet? '.format(money = player.money)))
    deck = full_deck
    random.shuffle(deck)

    is_playerstand = 0
    inital_deal(player = player, dealer = dealer)

    while is_playerstand == 0:
        print('\nThe Player has:')
        print_hand_value(player.hand)
        print('for a score of:{score}'.format(score = player.calc_hand_value()))
        action = ''
        
        while action not in ('HIT','STAND'):
            action = input('Would you like to HIT or STAND? ').upper()
            if action == 'HIT':
                player.hit()
                if player.calc_hand_value() > 21:
                    print('\nYou have busted with a {value}!'.format(value = player.calc_hand_value()))
                    is_playerstand = 1
            elif action == 'STAND':
                is_playerstand = 1
            else:
                print('Try your selection again.')

    while dealer.calc_hand_value() <= 16:
        dealer.hit()
        
    print('\nThe Dealer has:')
    print_hand_value(dealer.hand)
    print('for a score of:{score}'.format(score = dealer.calc_hand_value()))

    if (player.calc_hand_value() > dealer.calc_hand_value() and player.calc_hand_value() <= 21) or dealer.calc_hand_value() > 21:
        print('\nPlayer Wins!')
        player.money += bet
    elif player.calc_hand_value() == dealer.calc_hand_value():
        print('\nPush.')
    else:
        print('\nDealer Wins!')
        player.money -= bet

    player.clear_hand()
    dealer.clear_hand()