from unittest import TestCase

from src.auction.domain import User, Bid, Auction, Valuer


class TestValuer(TestCase):

    def test_should_return_the_largest_and_smallest_when_added_in_ascending_order(self):
        bruno = User('Bruno')
        mari = User('Mari')

        bid_from_bruno = Bid(bruno, 100)
        bid_from_mari = Bid(mari, 150)

        auction = Auction('Laptop')

        auction.bids.append(bid_from_bruno)
        auction.bids.append(bid_from_mari)

        valuer = Valuer()
        valuer.evaluate(auction)

        lowest_bid_expected = 100.0
        highest_bid_expected = 150.0

        self.assertEqual(lowest_bid_expected, valuer.lowest_bid)
        self.assertEqual(highest_bid_expected, valuer.highest_bid_expected)

    def test_should_return_the_largest_and_smallest_when_added_in_descending_order(self):
        bruno = User('Bruno')
        mari = User('Mari')

        bid_from_bruno = Bid(bruno, 100)
        bid_from_mari = Bid(mari, 150)

        auction = Auction('Laptop')

        auction.bids.append(bid_from_mari)
        auction.bids.append(bid_from_bruno)

        valuer = Valuer()
        valuer.evaluate(auction)

        lowest_bid_expected = 100.0
        highest_bid_expected = 150.0

        self.assertEqual(lowest_bid_expected, valuer.lowest_bid)
        self.assertEqual(highest_bid_expected, valuer.highest_bid_expected)

    def test_should_return_the_same_value_for_the_highest_and_lowest_bid_when_the_auction_has_a_bid(self):
        bruno = User('Bruno')

        bid = Bid(bruno, 100)

        auction = Auction('Book')
        auction.bids.append(bid)

        valuer = Valuer()
        valuer.evaluate(auction)

        self.assertEqual(100, valuer.lowest_bid)
        self.assertEqual(100, valuer.lowest_bid)

    def test_should_return_the_highest_and_lowest_value_when_the_auction_has_three_bids(self):
        bruno = User('Bruno')
        mari = User('Mari')
        leia = User('Leia')

        bid_from_bruno = Bid(bruno, 100)
        bid_from_mari = Bid(mari, 140)
        bid_from_leia = Bid(leia, 200)

        auction = Auction('Notebook')

        auction.bids.append(bid_from_mari)
        auction.bids.append(bid_from_bruno)
        auction.bids.append(bid_from_leia)

        valuer = Valuer()
        valuer.evaluate(auction)

        lowest_bid_expected = 100.0
        highest_bid_expected = 200.0

        self.assertEqual(lowest_bid_expected, valuer.lowest_bid)
        self.assertEqual(highest_bid_expected, valuer.highest_bid_expected)