# This game of roullette models the outcomes of a wheel with numbers 1 to 30 where even numbers are black
# and odd numbers are red. There are 2 green zeros.
# A player can make a bet on the colors red or black for a 2:1 payout, the zeros for a 14:1 payout, or a number for a 28:1 payout.

import random

# Bet Payouts
color_bet = 1
zero_bet = 14
number_bet = 28

class game:
    def __init__(self, balance):
        self.balance = balance
        self.plays = []
        self.min = balance
        self.max = balance
        self.bust = False

    def play(self, bet, amount=1000):
        roll = random.randint(-1, 30)
        if (bet == 0):
            if (roll > 0) and (roll%2==0):
                self.balance -= amount*color_bet
            else:
                self.balance += amount
        elif (bet == 1):
            # zero
            if roll <= 0:
                self.balance -= amount*zero_bet
            else:
                self.balance += amount
        else:
            if roll == 30:
                self.balance -= amount*number_bet
            else:
                self.balance += amount

        if self.balance > self.max:
            self.max = self.balance
        elif self.balance < self.min:
            self.min = self.balance

        return self.balance >= number_bet*amount

    

# Integer simulationw

initial_balance = 250000000
games = []
num_bets = 2500
bet_amount = 1000000
# Simulate games with bets
for i in range(1000):
    # Start a game
    Game = game(initial_balance)

    for j in range(num_bets):
        if Game.play(random.randint(0,2), bet_amount):
            continue
        else:
            Game.bust = True
            break
    
    Game.profitable = Game.balance > initial_balance
    games.append(Game)

bust = 0
profitable = 0
balance = 0
min = 0
max = 0
for Game in games:
    bust += Game.bust
    profitable += Game.profitable
    balance += Game.balance
    min += Game.min
    max += Game.max

print("Num Bust: {}".format(bust))
print("Num Profitable: {}".format(profitable))
print("Average End Balance: ${:,.2f}".format(balance/1000))
print("Average Min Amount: ${:,.2f}".format(min/1000))
print("Average Max Amount: ${:,.2f}".format(max/1000))
print("Retention of Cashflow: {:.2f}%".format(100*(balance/1000 - initial_balance) / (bet_amount * num_bets)))