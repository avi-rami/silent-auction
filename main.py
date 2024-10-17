from clear import clear  # Import a function to clear the console screen
from art import logo  # Import a logo for display

print(logo)  # Display the logo
print("Welcome to the secret auction program.")  # Introduction message

# Initialize an empty list to store auction bids
silent_auction = []


def add_bid(name, bid):
    """
  Function to add a new bid to the silent auction list.

  Parameters:
  name (str): The name of the bidder.
  bid (int): The bid amount.
  """
    silent_auction.append({"name": name, "bid": bid})


# Loop to collect bids from users
new_bid = "yes"
while new_bid == 'yes':
    name = input("What's your name?: ")  # Get the name of the bidder
    bid = int(input("What's your bid?: $"))  # Get the bid amount
    # Note: A more refined version of this program would include error handling here
    new_bid = input("Are there any other bidders? Type 'yes' or 'no': ").lower()  # Check if there are more bidders
    add_bid(name, bid)  # Add the bid to the auction list
    clear()  # Clear the console screen for the next bidder

# Note: A more refined version of this program would include handling for equal highest bids
# Algorithm to determine the highest bid
highest_bid = 0
highest_bid_name = ""

for bid in silent_auction:
    if bid["bid"] > highest_bid:
        highest_bid = bid["bid"]
        highest_bid_name = bid["name"]

# Display the winner
print(f"The winner is {highest_bid_name} with a bid of ${highest_bid}.")
