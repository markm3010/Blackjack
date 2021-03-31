# Blackjack game by Mark Matthias 
# I made this a few years ago (2018?) while following a tutorial at Udemy.com. I tried to
# make it my own tho.  I was not new to Python but needed a good example of a more substantial 
# program and this was a good one.  I followed the class setups but after that I tried to 
# complete the program myself.  But I don't take credit for this, it wouldn't be right.  
# Thanks Udemy!

# It is stil fun to play too...I want to improve it to give the option to continue playing games,
# and add currency to the mix so it tells you how much money you made (or lost) as the games progress.

# It requires ~Python 3.5 or better.

from random import randint
import time


class Deck(object):
    def __init__(self):
        # each row is, in order: SPADES, CLUBS, HEARTS, DIAMONDS
        self.the_deck = ['s0', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 'st', 'sj', 'sq', 'sk', \
                         'c0', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ct', 'cj', 'cq', 'ck', \
                         'h0', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'ht', 'hj', 'hq', 'hk', \
                         'd0', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'dt', 'dj', 'dq', 'dk']

        # These are printable representations of all the cards.
        self.deck_description = ['Ace of Spades', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades',
                                 '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades',
                                 'Jack of Spades', 'Queen of Spades', 'King of Spades', \
                                 'Ace of Clubs', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs',
                                 '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs',
                                 'Queen of Clubs', 'King of Clubs', \
                                 'Ace of Hearts', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts',
                                 '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts',
                                 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', \
                                 'Ace of Diamonds', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds',
                                 '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds',
                                 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds']
        self.card_num = None
        self.card = None
        self.n = 51 # cards in deck
        self.ace = False

    def deal_card(self):
        global n
        self.card_num = randint(0, self.n)
        self.card = self.the_deck.pop(self.card_num)
        self.n -= 1
        self.get_card_points()
        return self.get_card_points(), (self.get_current_desc())

    def get_current_desc(self):
        return self.deck_description.pop(self.card_num)

    def get_card_points(self):
        if self.card[1] == '0':
            self.ace = True
            return 11
        elif self.card[1] == '2':
            self.ace = False
            return 2
        elif self.card[1] == '3':
            self.ace = False
            return 3
        elif self.card[1] == '4':
            self.ace = False
            return 4
        elif self.card[1] == '5':
            self.ace = False
            return 5
        elif self.card[1] == '6':
            self.ace = False
            return 6
        elif self.card[1] == '7':
            self.ace = False
            return 7
        elif self.card[1] == '8':
            self.ace = False
            return 8
        elif self.card[1] == '9':
            self.ace = False
            return 9
        else:
            return 10


class Player():
    def __init__(self, player_type, name): # player_type = 'house' or 'player' 
        self.player_type = player_type[0]
        self.name = name
        self.total_score = 0
        self.points = 0
        self.has_ace = 0

    def get_ace_status(self):
        return self.has_ace

    def set_ace_status_round1(self, card_status):
        if card_status[0] == 'A':
            self.has_ace += 1
        elif card_status[0] == 'R': # rm an Ace from ct. as 10 was removed from pt tot since he has 2 aces
            self.has_ace -= 1

    def adjust_ace_status_round2(self, card_status):
        if card_status[0] == 'A' and self.total_score > 21:
            self.total_score -= 10

    def add_to_score(self, score):
        self.total_score += score

    def get_total_score(self):
        return self.total_score

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------

def check_if_ace_needs_reducing_round1(this_guy):
    if this_guy.has_ace and this_guy.total_score > 21:
        this_guy.add_to_score(-10)

# ------------------------------------------------------------------------------------
def deal_card_round1(the_player, name):
    print("-"*41)
    data = game_deck.deal_card()
    card_pts = data[0]
    card_desc = data[1]
    the_player.add_to_score(card_pts)
    the_player.set_ace_status_round1(card_desc)
    print(name + ":\n" + card_desc + "\nAce Count:    " + \
          str(the_player.get_ace_status()) + "\nTotal Points: " + str(the_player.get_total_score()))
    time.sleep(1)

# ------------------------------------------------------------------------------------
def check_for_winner_round1(the_playah, the_house):
    time.sleep(2)
    if the_playah.get_total_score() == 21 and the_house.get_total_score() != 21:
        print("-" * 41)
        print ("Blackjack: " + the_playah.name)
    elif the_playah.get_total_score() != 21 and the_house.get_total_score() == 21:
        print ("-"*41)
        print ("WINNER: " + the_house.name)
        exit()
    elif the_playah.get_total_score() == 21 and the_house.get_total_score()== 21:
        print("-" * 41)
        print("TIE GAME!")
        exit()

# ------------------------------------------------------------------------------------
def check_for_2_aces_round1(this_dude):
    if this_dude.get_total_score() == 22:
        this_dude.add_to_score(-10)
        this_dude.set_ace_status_round1('Remove one Ace')
        print("-"*41)
        print(this_dude.name + ":\nAdjusted Total Points: " + str(this_dude.get_total_score()) + \
               "\nAdjusted Ace Count:     " + str(this_dude.get_ace_status()) )

# ------------------------------------------------------------------------------------
def deal_card_round2(the_player, name):
    print("-"*41)
    data = game_deck.deal_card()
    card_pts = data[0]
    card_desc = data[1]
    the_player.add_to_score(card_pts)
    the_player.adjust_ace_status_round2(card_desc)
    print(name + ":\n" + card_desc + "\nAce Count:    " + \
          str(the_player.get_ace_status()) + "\nTotal Points: " + str(the_player.get_total_score()))
    time.sleep(1)


# ------------------------------------------------------------------------------------
def decide_winner_round2(dude1, dude2):
    print("-" * 41)
    time.sleep(2)
    if dude1.get_total_score() > 21:
        print("WINNER GETS THE DOUGH: " + dude2.name)
        exit()
    if dude2.get_total_score() > 21:
        print("WINNER GETS THE DOUGH: " + dude1.name)
        exit()
    if dude1.get_total_score() > dude2.get_total_score():
        print ("WINNER GETS THE DOUGH: " + dude1.name)
        exit()
    elif dude1.get_total_score() < dude2.get_total_score():
        print ("WINNER GETS THE DOUGH: " + dude2.name)
        exit()
    else:
        print("GAME IS A PUSH (TIE). PLAYERS BET IS RETURNED")
        exit()

# ------------------------------------------------------------------------------------
def check_for_bust(bustee, winner):
    time.sleep(2)
    if bustee.total_score > 21:
        if bustee.has_ace:
            bustee.total_score -= 10
            if bustee.total_score > 21:
                print(bustee.name + " busted.")
                print("-" * 41)
                print("WINNER: " + winner.name)
                exit()
        print (bustee.name + " busted, " + winner.name + " gets the money.")
        time.sleep(2)
        print ("-"*41)
        print ("WINNER: " + winner.name)
        keepon = input("Keep on going? y/n: ")
        if tolower(keepon[0]) == 'y':

            
        exit()
# ------------------------------------------------------------------------------------
def dealer_stays_or_hits_round2(dealer, dealer_name, player):
    time.sleep(2)
    print("-" * 41)
    while dealer.total_score < 18 or dealer.total_score < player.total_score:
        print(dealer_name + " has " + str(dealer.get_total_score()) + ", so dealer hits.")
        time.sleep(2)
        deal_card_round2(dealer, dealer_name)
        time.sleep(1)
        check_for_bust(dealer, player)
    else:
        print(dealer_name + " has " + str(dealer.get_total_score()) + ", so dealer stays.")

# ------------------------------------------------------------------------------------
def player_hits_round2(player, player_name, dealer):
    # print("-" * 41)
    print(player_name + " has " + str(player.get_total_score()) + ", so player hits.")
    time.sleep(2)
    deal_card_round2(player, player_name)
    check_for_bust(player, dealer)
    time.sleep(1)
    print(player_name + " has " + str(player.get_total_score()))

# ------------------------------------------------------------------------------------
def get_decision (aPlayer):
    decision = input(aPlayer + ', Do you want to Stay or Hit? >> ')
    if decision[0].lower() == 's':
        return False
    else:
        return True
# ------------------------------------------------------------------------------------

######################################################################################

# MAIN MAIN MAIN MAIN

# player_card = []
# player_total_pts = 0
# house_card = []
# house_total_pts = 0
# game_done = False


house_nm = 'THE DEALER'
house = Player(player_type = 'house', name = house_nm)

player_nm = input("Your Name Please: ")
player = Player(player_type = 'player', name = player_nm)

game_deck = Deck()

#                            ROUND 1 (each player given 2 cards)
for i in range(2):
    deal_card_round1(player, player_nm)
    deal_card_round1(house, house_nm)

check_if_ace_needs_reducing_round1(player)
check_if_ace_needs_reducing_round1(house)
check_for_2_aces_round1(player)
check_for_2_aces_round1(house)
check_for_winner_round1(player, house)

#                            ROUND 2 (player decides to stay or hit, each player hits or stays)
while True:
    print ("-"*41)
    if(player.total_score == 21):
        while True:
            dealer_stays_or_hits_round2(house, house_nm, player)
        if player.total_score == 21:
            print("-" * 41)
            print("WINNER: " + winner.name)
    take_another_card = True
    while take_another_card:
        time.sleep(2)
        take_another_card = get_decision(player_nm)
        if take_another_card:
            player_hits_round2(player, player_nm, house)
            time.sleep(1)
    dealer_stays_or_hits_round2(house, house_nm, player)
    decide_winner_round2(player, house)

