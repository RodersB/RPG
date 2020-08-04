from item import Item


class Gem(Item):
    def __init__(self, tier, name, sell_for, stats):
        Item.__init__(self, tier, name, sell_for)
        self.stats = stats
