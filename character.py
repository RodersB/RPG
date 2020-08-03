class Character:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
        self.gear = {}
        self.inventory = []

    def equip_item(self, equipment):
        if self.gear.get(equipment.slot, None) is not None:
            self.inventory.append(self.gear.pop(equipment.slot))

        self.gear[equipment.slot] = equipment
        self.calculate_stats()

    def calculate_stats(self):
        pass


