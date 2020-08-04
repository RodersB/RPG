from item import Item


class Equipment(Item):
    def __init__(self, tier, name, sell_for, slot, sockets, stats):
        Item.__init__(self, name, tier, sell_for)
        self.slot = slot
        self.sockets = sockets
        self.stats = stats
        self.gems = []

    def add_gem(self, gem):
        if len(self.gems) < self.sockets:
            self.gems.append(gem)
            self.calculate_stats()

    def calculate_stats(self):
        pass





