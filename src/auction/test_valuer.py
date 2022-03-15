from unittest import TestCase

from src.auction.domain import User, Bid, Auction, Valuer


class TestValuer(TestCase):

    def test_evaluate(self):
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
        biggest_bid_expected = 150.0

        self.assertEqual(lowest_bid_expected, valuer.lowest_bid)
        self.assertEqual(biggest_bid_expected, valuer.biggest_bid)
