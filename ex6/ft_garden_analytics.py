class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def show_flowers(self):
        return (f"{self.color} flowers "
                f"({'blooming' if self.blooming else 'not blooming'})")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def show_prize(self):
        return f"Prize points: {self.prize_points}"


class GardenManager:
    total_gardens = 0  # class attribute

    class GardenStats:
        @staticmethod
        def count_plants(plants):
            return len(plants)

        @staticmethod
        def total_height(plants):
            return sum(p.height for p in plants)

        @staticmethod
        def count_types(plants):
            regular = sum(1 for p in plants if type(p) is Plant)
            flowering = sum(1 for p in plants if type(p) is FloweringPlant)
            prize = sum(1 for p in plants if type(p) is PrizeFlower)
            return regular, flowering, prize

    def __init__(self):
        self.gardens = []
        GardenManager.total_gardens += 1

    def add_garden(self, garden):
        self.gardens.append(garden)

    @classmethod
    def create_garden_network(cls):
        return f"Garden network initialized with {cls.total_gardens} managers"


class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def garden_report(self):
        report = f"=== {self.owner}'s Garden Report ===\n"
        report += "Plants in garden:\n"

        for p in self.plants:
            line = f"- {p.name}: {p.height}cm"

            if isinstance(p, FloweringPlant):
                line += f", {p.show_flowers()}"

            if isinstance(p, PrizeFlower):
                line += f", {p.show_prize()}"

            report += line + "\n"

        total = GardenManager.GardenStats.count_plants(self.plants)
        total_height = GardenManager.GardenStats.total_height(self.plants)
        reg, flow, prize = GardenManager.GardenStats.count_types(self.plants)

        report += f"Plants added: {total}, Total growth: {total_height}cm\n"
        report += (
            f"Plant types: {reg} regular, "
            f"{flow} flowering, {prize} prize flowers\n"
        )

        return report
