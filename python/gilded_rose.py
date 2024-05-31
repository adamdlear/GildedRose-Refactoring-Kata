# -*- coding: utf-8 -*-


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            match item.name:
                case "Aged Brie":
                    self.update_aged_brie(item)
                case "Sulfuras, Hand of Ragnaros":
                    continue
                case "Backstage passes to a TAFKAL80ETC concert":
                    self.update_backstage_passes(item)
                case "Conjured Mana Cake":
                    self.update_conjured_item(item)
                case _:
                    self.update_normal_item(item)

    def update_aged_brie(self, item):
        item.quality += 1
        item.sell_in -= 1
        self.handle_limits(item)

    def update_sulfuras(self, item):
        item.quality += 1

    def update_backstage_passes(self, item):
        if item.sell_in == 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality += 3
        elif item.sell_in <= 10:
            item.quality += 2
        else:
            item.quality += 1
        item.sell_in -= 1
        self.handle_limits(item)

    def update_conjured_item(self, item):
        if item.sell_in < 0:
            item.quality -= 4
        else:
            item.quality -= 2
        item.sell_in -= 1
        self.handle_limits(item)

    def update_normal_item(self, item):
        if item.sell_in < 0:
            item.quality -= 2
        else:
            item.quality -= 1
        item.sell_in -= 1
        self.handle_limits(item)

    def handle_limits(self, item):
        if item.quality > 50:
            item.quality = 50
        if item.quality < 0:
            item.quality = 0


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
