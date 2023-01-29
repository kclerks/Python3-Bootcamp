# %% [markdown]
# # Milestone Project 2 - Blackjack Game
# In this milestone project you will be creating a Complete BlackJack Card Game in Python.
# 
# Here are the requirements:
# 
# * You need to create a simple text-based [BlackJack](https://en.wikipedia.org/wiki/Blackjack) game
# * The game needs to have one player versus an automated dealer.
# * The player can stand or hit.
# * The player must be able to pick their betting amount.
# * You need to keep track of the player's total money.
# * You need to alert the player of wins, losses, or busts, etc...
# 
# And most importantly:
# 
# * **You must use OOP and classes in some portion of your game. You can not just use functions in your game. Use classes to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!**
# 
# 
# Feel free to expand this game. Try including multiple players. Try adding in Double-Down and card splits!

# %% [markdown]
# ## Imports and variables

# %%
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace': 11}
            
playing = True

# %% [markdown]
# ## Card and Deck

# %%
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

# %%
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            # print(suit)
            for rank in ranks:
                # print(rank)
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp
        # return  f'{len(self.deck)} cards'

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

# %% [markdown]
# ### Test cards

# %%
# test_deck = Deck()
# test_deck.shuffle()
# print(test_deck)

# %% [markdown]
# ## Hand Class

# %%
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# %% [markdown]
# ### Testing Hand Class

# %%
# test_deck = Deck()
# test_deck.shuffle()
# test_player = Hand()
# test_player.add_card(test_deck.deal())
# test_player.add_card(test_deck.deal())
# test_player.value


# %%
# for card in test_player.cards:
#     print(card)

# %%
# test_player.add_card(test_deck.deal())
# test_player.value

# %% [markdown]
# ## Chips

# %%
class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

# %% [markdown]
# ## Functions and Definitions

# %%
# def take_bet(chips):
#     while True:
#         try:
#             chips.bet = int(input('How much would you like to bet? '))
#         except ValueError:
#             print('That was not a number')
#         else:
#             if chips.bet > chips.total:
#                 print('Not enough money')
#             else:
#                 print(f'The bet is {chips.bet}')
#                 break
def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break

# %% [markdown]
# **Step 7: Write a function for taking hits**<br>
# Either player can take hits until they bust. This function will be called during gameplay anytime a Player requests a hit, or a Dealer's hand is less than 17. It should take in Deck and Hand objects as arguments, and deal one card off the deck and add it to the Hand. You may want it to check for aces in the event that a player's hand exceeds 21.

# %%
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

# %% [markdown]
# **Step 8: Write a function prompting the Player to Hit or Stand**<br>
# This function should accept the deck and the player's hand as arguments, and assign playing as a global variable.<br>
# If the Player Hits, employ the hit() function above. If the Player Stands, set the playing variable to False - this will control the behavior of a <code>while</code> loop later on in our code.

# %%
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        x = input('Hit or Stand? (h or s)')
        
        if x == 'h':
            hit(deck,hand)

        elif x == 's':
            print('Player stands. Dealers turn')
            playing = False
        
        else:
            print('Sorry, please try again')
            continue
        break

# %% [markdown]
# **Step 9: Write functions to display cards**<br>
# When the game starts, and after each time Player takes a card, the dealer's first card is hidden and all of Player's cards are visible. At the end of the hand all cards are shown, and you may want to show each hand's total value. Write a function for each of these scenarios.

# %%
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Current value: " + str(player.value))
    # print('Player hand below')
    # for card in player.cards:
    #     print(card)
    # print(f'Value: {player.value}')
    
    # print('Dealer hand below')
    # for card in dealer.cards:
    #     if dealer.cards:
    #         print(f'{card} + <-- hidden')
    #     else:
    #         print(card)
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    # for card in player.cards:
    #     print(card)
    # print(f'Value: {player.value}')
    # for card in dealer.cards:
    #     print(card)
    # print(f'Value: {dealer.value}')

# %% [markdown]
# **Step 10: Write functions to handle end of game scenarios**<br>
# Remember to pass player's hand, dealer's hand and chips as needed.

# %%
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

# %% [markdown]
# # Game!

# %%
while True:
    # Print an opening statement
    print('Welcome to BlackJack!')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
        
    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
    
        # Show all cards
        show_all(player_hand,dealer_hand)
    
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)

    # Ask to play again
    new_game = input("Would you like to play again? Enter 'y' or 'n' ")
    if new_game[0].lower() == 'y':
        playing=True
        continue
    else:
        print("Game over")
        break


