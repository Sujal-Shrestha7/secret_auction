import os


def clear():
    os.system('cls')
    return None


bids = {}


def highest_bid(bid_record):
    highest_bid_amount = 0
    winner = ''
    for bidder in bid_record:
        if bid_record[bidder] > highest_bid_amount:
            highest_bid_amount = bid_record[bidder]
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid_amount}.')


case = True

while case:
    name = input("Enter your name : ")
    bid = int(input("Ener your bidding : $ "))
    bids[name] = bid
    print('\n________________________________________')
    bidders = input('Is there any other bidder left? (yes) or (no) ')
    print(bids)
    if bidders == 'no':
        case = False
        highest_bid(bids)
    elif bidders == 'yes':
        clear()
print('\n_________________________')
print(f'Name : {name}\nBidding : $ {bid}')
print('_________________________')
print(bids)
