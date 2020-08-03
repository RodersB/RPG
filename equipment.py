class Equipment:
    def __init__(self, tier, name, slot, sockets, stats):
        self.tier = tier
        self.name = name
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





