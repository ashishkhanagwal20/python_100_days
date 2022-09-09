
bid_dict = {}
continue_bid = True
while continue_bid:
    name = input("What is Your Name?\n")
    bid = int(input("What is your bid?\n$:"))
    bid_dict[name] = bid
    other_users = input("Are there other users who want to bid?\n")

    if other_users == "yes":
        pass
    else:
        continue_bid = False
        winner= (max(bid_dict, key=bid_dict.get))
        print(bid_dict)
        print(winner)
        bid_value = bid_dict[winner]
        print(f"{winner} has won the bid with {bid_value} dollars")