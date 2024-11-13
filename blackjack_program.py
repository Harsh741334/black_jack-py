import random

# Define card values
card = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
card_values = {"A": 11, "J": 10, "Q": 10, "K": 10}

# Enter the name of the player
player = input("ENTER THE NAME OF PLAYER:\n ")
name = {player: [], "dealer": []}

# Initial cards for player and dealer
for n in range(2):
    name[player].append(random.choice(card))
    name["dealer"].append(random.choice(card))

# Display the player's cards and the first card of the dealer
print(f"CARDS OF THE PLAYER: {name[player]}\nFIRST CARD OF THE DEALER: {name['dealer'][0]}")

# Check if the player wants another card
choose = "p"
while choose != "y" and choose != "n":
    choose = input("IF PLAYER WANTS ANOTHER CARD TYPE 'Y' OR ELSE 'N':\n").lower()
    if choose == "y":
        name[player].append(random.choice(card))
        print(f"NEW CARDS OF THE PLAYER: {name[player]}")
    elif choose == "n":
        break
    else:
        print("ENTER A VALID INPUT...")

# Calculate the sum of cards for the player and dealer
def calculate_sum(cards):
    total = 0
    ace_count = 0
    for card in cards:
        # Assign values for face cards and Ace
        if card in card_values:
            total += card_values[card]
            if card == "A":
                ace_count += 1
        else:
            total += card
    # Adjust Ace value if total exceeds 21
    while total > 21 and ace_count:
        total -= 10
        ace_count -= 1
    return total

# Summing player and dealer hands
player_sum = calculate_sum(name[player])
dealer_sum = calculate_sum(name["dealer"])

# Dealer draws if sum is less than 17
while dealer_sum < 17:
    new_card = random.choice(card)
    name["dealer"].append(new_card)
    dealer_sum = calculate_sum(name["dealer"])

# Display final cards and sums
print(f"FINAL CARDS OF THE PLAYER: {name[player]} with sum {player_sum}")
print(f"FINAL CARDS OF THE DEALER: {name['dealer']} with sum {dealer_sum}")

# Determine the winner
if player_sum > 21:
    print("DEALER WINS (Player busts)")
elif dealer_sum > 21:
    print("PLAYER WINS (Dealer busts)")
elif dealer_sum > player_sum:
    print("DEALER WINS")
elif player_sum > dealer_sum:
    print("PLAYER WINS")
else:
    print("IT'S A TIE")




# take 'A' as 1 or 11 may to choose by the sum oif the end result from both side
# if dealer has sum less than 17 then dealer will have to pick a card
#campare than end result of the dealer and the player
# the closest to 21 will win and over 21 will loss
# announce the result
