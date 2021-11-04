'''
start = 2 for 52cards
start = 6 for 36cards
start = 7 for 32cards
'''

def card(start):
    pack_of_card = []
    card_symbol = ["♠", "♥", "♦", "♣"]
    for i in range(4):
        for high_cards in range(start, 15):
            if high_cards == 14:
                high_cards = "A"
            elif high_cards == 13:
                high_cards = "K"
            elif high_cards == 12:
                high_cards = "Q"
            elif high_cards == 11:
                high_cards = "J"
            passe_var = str(high_cards)+str(card_symbol[i])
            pack_of_card.append(passe_var)
    return pack_of_card

card(2)