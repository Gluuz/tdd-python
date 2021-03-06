import sys

class User:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


class Bid:

    def __init__(self, user, value):
        self.user = user
        self.value = value


class Auction:

    def __init__(self, description):
        self.description = description
        self.__bids = []

    @property
    def bids(self):
        return self.__bids


class Valuer:

    def __init__(self):
        self.highest_bid_expected = sys.float_info.min
        self.lowest_bid = sys.float_info.max

    def evaluate(self, auction: Auction):
        for bid in auction.bids:
            if bid.value > self.highest_bid_expected:
                self.highest_bid_expected = bid.value
            if bid.value < self.lowest_bid:
                self.lowest_bid = bid.value
