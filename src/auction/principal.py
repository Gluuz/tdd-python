from src.auction.domain import User, Bid, Auction

bruno = User('Bruno')
mari = User('Mari')

bid_from_bruno = Bid(bruno,100)
bid_from_mari = Bid(mari, 200)

auction = Auction('Laptop')

auction.bids.append(bid_from_bruno)
auction.bids.append(bid_from_mari)

for bid in auction.bids:
    print(f'The user {bid.user.name} bid on {bid.value}')
