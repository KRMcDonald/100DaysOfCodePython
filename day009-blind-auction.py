from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
bids = {}
more_bidders = "Yes"

while more_bidders == "Yes":
  name = input("What is your name? ")
  bid = float(input("What is your bid? $"))
  bids[name] = bid
  more_bidders = input("Are there more bidders? Yes/No ")
  if more_bidders == "Yes":
    clear()

max_bid = 0
max_bidder = ""
for key in bids:
  if bids[key] > max_bid:
    max_bid = bids[key]
    max_bidder = key
max_bid = "{:.2f}".format(max_bid)
print(f"{max_bidder} was the winner, with a bid of ${max_bid}")