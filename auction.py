'''Secret Auction Program takes bids from users and determines the highest bid.'''

print("\nWelcome to Secret Auction Program.\n")
# print(input("What is your name? ")) 
# print("What is your bid? $")    

bids = {}
def add_bid(name, bid):
    bids[name] = bid
    

def find_highest_bidder(bids):
    highest_bid = 0 
    winner = ""

    for bidder in bids: 
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
        
    print(f"\nCongratulations! The winner is '{winner}' with a bid of '${highest_bid}'.\n")

while True:
    name = input("What is your name?\n")
    bid = int(input("What is your bid? $\n"))
    add_bid(name, bid)
    
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more_bidders == "no":
        find_highest_bidder(bids)
        break
    elif more_bidders == "yes":
        print("\n" * 20)
        continue
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        break