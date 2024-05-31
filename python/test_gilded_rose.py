# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 10, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_update_aged_bried(self):
        items = [Item("Aged Brie", 3, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(3, items[0].quality)

    def test_update_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 20, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(20, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_update_backstage_passes(self):
        # Test for 10+ days out
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

        # Test for 5+ days out
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(3, items[0].quality)

        # Test for day of concert (0 days out)
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_update_conjured_item(self):
        items = [Item("Conjured Mana Cake", 10, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(3, items[0].quality)

    def test_update_normal_item(self):
        # Test for before sell date
        items = [Item("bar", 10, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

        # Test for after sell date
        items = [Item("bar", -1, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(1, items[0].quality)


if __name__ == '__main__':
    unittest.main()
