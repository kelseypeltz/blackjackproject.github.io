import pandas as pd
import numpy as np
import time


class Card:
    FACES = {'Ace': 11, 'Jack': 10, 'Queen': 10, 'King': 10}
    
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
        
    def __str__(self):
        return "{0.face}_{0.suit}".format(self)
    
    @property
    def value(self):
        return self.FACES.get(self.face, self.face)
    

class Deck:

    def __init__(self, num_of_sets=1):
        self.num_of_sets = num_of_sets
        self.init_new_deck()

    def init_new_deck(self):
        self.cards = []
        for s in range(self.num_of_sets):
            for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
                for rank in ['Ace', 'Jack', 'Queen', 'King'] + [x for x in range(2, 11)]:
                    self.cards.append(Card(rank, suit))
        self.shuffle()

    def shuffle(self):
        np.random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def size(self):
        return self.cards.__len__()


class Hand:

    def __init__(self, list_of_cards):
        self.cards = list_of_cards
        
    def value(self):
        ret_val = sum(card.value for card in self.cards)
        num_aces = self.count_card_any_suit("Ace")
        while num_aces > 0:
            if ret_val > 21:
                ret_val -= 10
                num_aces -= 1
            else:
                break
        return ret_val

    def add_to_hand(self, card):
        self.cards.append(card)
        
    def size(self):
        return self.cards.__len__()

    def count_card_any_suit(self, card_face):
        count = 0
        for card in self.cards:
            if card.face == card_face:
                count += 1
        return count

    def __str__(self):
        cards_strs = [str(c) for c in self.cards]
        ret_str = ":".join(cards_strs)
        return ret_str


class Player:
    
    def __init__(self, player_id=1):
        self.player_id = player_id
        # state of the player is -1 if out of the game, 0 if playing
        self.state = 0 
        self.hand = Hand([])

    def reset_hand(self):
        if self.hand.size() != 0:
            self.hand = Hand([])

    def hand_value(self):
        return self.hand.value()
            
    def show_hand(self):
        return str(self.hand)
    
    def deal_from_deck(self, deck):
        self.hand.add_to_hand(deck.draw())

    # Need different logic from Dealer
    def hit_or_stay(self):
        return self.hand_value() < 17
    
    def busted(self):
        return self.hand_value() > 21


class Dealer(Player):
    
    def __init__(self, dealer_id=0):
        self.open_card = None
        super(Dealer, self).__init__(dealer_id)

    def deal_from_deck(self, deck):
        card = deck.draw()
        if self.open_card == None:
            self.open_card = card
        self.hand.add_to_hand(card)
    
    def reset_hand(self):
        super(Dealer, self).reset_hand()
        self.open_card = None

class Table():

    def __init__(self, num_of_sets, tab_num):
        self.table_number = tab_num
        self.deck = Deck(num_of_sets)
        self.dealer = Dealer(0)
        self.players = []
        self.num_of_players = 0

    def initiate_new_round(self, num_of_players):
        del self.players[:]
        for count in range(0,num_of_players):
            self.players.append(Player(count+1))
        self.dealer.reset_hand()
        self.deal_cards(2)

    def deal_cards(self, num_of_cards_to_deal=2):
        if self.deck.size() < 52:
            self.deck.init_new_deck()
        for d in range(num_of_cards_to_deal):
            for player in self.players:
                player.deal_from_deck(self.deck)
            self.dealer.deal_from_deck(self.deck)

    def check_dealer_blackjack(self):
        return self.dealer.hand_value() == 21

    def get_list_data(self, player, winner):
        eachRow = []
        eachRow.append(self.table_number)
        eachRow.append(len(self.players))
        eachRow.append(player.show_hand())
        eachRow.append(player.hand_value())
        eachRow.append(self.dealer.open_card)
        eachRow.append(self.dealer.show_hand())
        eachRow.append(self.dealer.hand_value())
        eachRow.append(winner)
        return eachRow

    def play_round(self, num_of_players):
        self.initiate_new_round(num_of_players)
        round_data = []
        if self.check_dealer_blackjack():
            #Add each hand to data frame and return
            for player in self.players:
                row = None
                if player.hand_value() == 21:
                    row = self.get_list_data(player, 'draw')
                else:
                    row = self.get_list_data(player, 'dealer')
                round_data.append(row)
        else:
            for player in self.players:
                while player.state != -1:
                    if player.hit_or_stay():
                        player.deal_from_deck(self.deck)
                        if player.busted():
                            row = self.get_list_data(player, 'dealer')
                            round_data.append(row)
                            player.state = -1
                    else:
                        break
            while self.dealer.state != -1:
                if self.dealer.hit_or_stay():
                    self.dealer.deal_from_deck(self.deck)
                    if self.dealer.busted():
                        self.dealer.state = -1
                else:
                    break
            for player in self.players:
                if player.state != -1:
                    winner = 'draw'
                    if self.dealer.state == -1:
                        winner = 'player'
                    else: 
                        if player.hand_value() > self.dealer.hand_value():
                            winner = 'player'
                        if player.hand_value() < self.dealer.hand_value():
                            winner = 'dealer'
                    row = self.get_list_data(player, winner)
                    round_data.append(row)
        return round_data


def create_table_and_play(num_of_sets, table_number):
    table = Table(num_of_sets, table_number)
    num_players = np.random.randint(1, 7)
    round_data = table.play_round(num_players)
    table_rounds_df = pd.DataFrame(columns=('TableNum', 'NumPlayers','PlayerHand','PlayerHandValue','DealerOpenCard','DealerHand','DealerHandValue','Winner'))
    count=0
    for x in round_data:
        table_rounds_df.loc[count] = x
        count+=1
    return table_rounds_df, table_rounds_df.shape[0]


def generate_casino_data(num_of_sets, num_tables, min_rows_of_data):
    all_dfs = []
    size = 0
    while min_rows_of_data > size:
        for tab_num in range(1, num_tables+1):
            tab_rounds_df, s = create_table_and_play(num_of_sets, tab_num)
            all_dfs.append(tab_rounds_df)
            size += s
            if min_rows_of_data < size:
                break

    return all_dfs

def main():
    num_of_sets = 20
    min_rows_of_data = 1000000
    num_tables = 50
    start = time.clock()
    dfs = generate_casino_data(num_of_sets, num_tables, min_rows_of_data)
    data = pd.concat(dfs, axis=0, ignore_index=True)
    data = data.sample(frac=1) # Shuffling to create some randomness in the output
    data.to_csv('blackjack_data.csv', index=False)
    end = time.clock()
    print("Total time taken is to generate",min_rows_of_data,"is", str(end-start))

if __name__ == "__main__":
    main()
