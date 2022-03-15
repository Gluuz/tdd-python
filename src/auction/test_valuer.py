from unittest import TestCase

from src.auction.domain import User, Bid, Auction, Valuer


class TestValuer(TestCase):

    def setUp(self):
        self.bruno = User('Bruno')
        self.mari = User('Mari')
        self.leia = User('Leia')
        self.bid_from_bruno = Bid(self.bruno, 100)
        self.bid_from_mari = Bid(self.mari, 150)
        self.bid_from_leia = Bid(self.leia, 200)
        self.auction = Auction('Laptop')

    def test_should_return_the_largest_and_smallest_when_added_in_ascending_order(self):
        self.auction.bids.append(self.bid_from_bruno)
        self.auction.bids.append(self.bid_from_mari)

        valuer = Valuer()
        valuer.evaluate(self.auction)

        lowest_bid_expected = 100.0
        highest_bid_expected = 150.0

        self.assertEqual(lowest_bid_expected, valuer.lowest_bid)
        self.assertEqual(highest_bid_expected, valuer.highest_bid_expected)

    def test_should_return_the_largest_and_smallest_when_added_in_descending_order(self):
        self.auction.bids.append(self.bid_from_mari)
        self.auction.bids.append(self.bid_from_bruno)

        valuer = Valuer()
        valuer.evaluate(self.auction)

        lowest_bid_expected = 100.0
        highest_bid_expected = 150.0

        self.assertEqual(lowest_bid_expected, valuer.lowest_bid)
        self.assertEqual(highest_bid_expected, valuer.highest_bid_expected)

    def test_should_return_the_same_value_for_the_highest_and_lowest_bid_when_the_auction_has_a_bid(self):
        bid = Bid(self.bruno, 100)

        auction = Auction('Book')
        auction.bids.append(bid)

        valuer = Valuer()
        valuer.evaluate(auction)

        self.assertEqual(100, valuer.lowest_bid)
        self.assertEqual(100, valuer.lowest_bid)

    def test_should_return_the_highest_and_lowest_value_when_the_auction_has_three_bids(self):
        self.auction.bids.append(self.bid_from_mari)
        self.auction.bids.append(self.bid_from_bruno)
        self.auction.bids.append(self.bid_from_leia)

        valuer = Valuer()
        valuer.evaluate(self.auction)

        lowest_bid_expected = 100.0
        highest_bid_expected = 200.0

        self.assertEqual(lowest_bid_expected, valuer.lowest_bid)
        self.assertEqual(highest_bid_expected, valuer.highest_bid_expected)