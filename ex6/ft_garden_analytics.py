class Plant:
    """Basic plant with name and height."""

    def __init__(self, name, height):
        """
        Initialize a Plant.
        Args:
            name (str): Name of the plant.
            height (int): Height of the plant in cm.
        """
        self.name = name
        self.height = height
        self.initial_height = height

    def grow(self):
        """Increase height by 1cm and print growth message."""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def describe(self):
        """
        Return a string describing the plant.

        Returns:
            str: Plant description.
        """
        return f"- {self.name}: {self.height}cm"

    def score(self):
        """
        Return contribution to garden score (default: height).

        Returns:
            int: Height of the plant.
        """
        return self.height


class FloweringPlant(Plant):
    """Plant with flowers."""

    def __init__(self, name, height, color):
        """
        Initialize a FloweringPlant.

        Args:
            name (str): Name of the plant.
            height (int): Height of the plant in cm.
            color (str): Color of the flowers.
        """
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def show_flowers(self):
        """
        Return flower status.

        Returns:
            str: Color and blooming status of flowers.
        """
        return (f"{self.color} flowers "
                f"({'blooming' if self.blooming else 'not blooming'})")

    def describe(self):
        """Return a string describing the flowering plant."""
        return f"- {self.name}: {self.height}cm, {self.show_flowers()}"


class PrizeFlower(FloweringPlant):
    """Flowering plant with prize points."""

    def __init__(self, name, height, color, prize_points):
        """
        Initialize a PrizeFlower.

        Args:
            name (str): Name of the plant.
            height (int): Height in cm.
            color (str): Flower color.
            prize_points (int): Points awarded for the prize flower.
        """
        super().__init__(name, height, color)
        self.prize_points = prize_points * 4

    def show_prize(self):
        """Return prize points information."""
        return f"Prize points: {self.prize_points}"

    def describe(self):
        """Return a string describing the prize flower."""
        return (f"- {self.name}: {self.height}cm, "
                f"{self.show_flowers()}, {self.show_prize()}")

    def score(self):
        """
        Return score contribution: height + prize points.

        Returns:
            int: Total score of the plant.
        """
        return self.height + self.prize_points


class GardenManager:
    """Manages multiple gardens."""
    total_gardens = 0

    class GardenStats:
        """Static methods for garden analytics."""

        @staticmethod
        def count_plants(plants):
            """
            Count the number of plants in a list.

            Args:
                plants (list): List of Plant objects.

            Returns:
                int: Total number of plants.
            """
            return len(plants)

        @staticmethod
        def total_growth(plants):
            """
            Calculate total growth since planting.
            Args:
                plants (list): List of Plant objects.
            Returns:
                int: Sum of growth for all plants.
            """
            return sum(p.height - p.initial_height for p in plants)

        @staticmethod
        def count_types(plants):
            """
            Count different types of plants.
            Args:
                plants (list): List of Plant objects.
            Returns:
                tuple: Number of (regular, flowering, prize) plants.
            """
            regular = sum(1 for p in plants if type(p) is Plant)
            flowering = sum(1 for p in plants if type(p) is FloweringPlant)
            prize = sum(1 for p in plants if type(p) is PrizeFlower)
            return regular, flowering, prize

    def __init__(self):
        """Initialize a GardenManager and increment total gardens count."""
        self.gardens = []
        GardenManager.total_gardens += 1

    def add_garden(self, garden):
        """
        Add a garden to this manager.
        Args:
            garden (Garden): Garden object to add.
        """
        self.gardens.append(garden)

    @classmethod
    def create_garden_network(cls):
        """
        Create a garden network message.
        Returns:
            str: Status message with total managers.
        """
        return f"Garden network initialized with {cls.total_gardens} managers"


class Garden:
    """Represents a garden with plants."""

    def __init__(self, owner):
        """
        Initialize a Garden.
        Args:
            owner (str): Name of the garden owner.
        """
        self.owner = owner
        self.plants = []

    def add_plant(self, plant):
        """
        Add a plant to the garden.
        Args:
            plant (Plant): Plant object to add.
        """
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        """Grow all plants in the garden by 1cm each."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def garden_report(self):
        """
        Generate a report for the garden.
        Returns:
            str: Detailed report including plant
            descriptions, counts, and growth.
        """
        report = f"=== {self.owner}'s Garden Report ===\nPlants in garden:\n"
        for p in self.plants:
            report += p.describe() + "\n"

        total = GardenManager.GardenStats.count_plants(self.plants)
        total_growth = GardenManager.GardenStats.total_growth(self.plants)
        reg, flow, prize = GardenManager.GardenStats.count_types(self.plants)

        report += f"\nPlants added: {total}, Total growth: {total_growth}cm\n"
        report += (f"Plant types: {reg} regular,"
                   f" {flow} flowering, {prize} prize flowers\n")
        return report


def height_validation(manager):
    """
    Verify all plants in all gardens have height > 0.
    Args:
        manager (GardenManager): GardenManager object.
    Returns:
        bool: True if all plants have height > 0, else False.
    """
    return all(p.height > 0 for g in manager.gardens for p in g.plants)


def calculate_garden_score(garden):
    """
    Calculate total garden score using polymorphic score().

    Args:
        garden (Garden): Garden object.

    Returns:
        int: Total score of all plants in the garden.
    """
    return sum(p.score() for p in garden.plants)


print("=== Garden Management System Demo ===\n")

manager = GardenManager()
manager2 = GardenManager()

alice_garden = Garden("Alice")
manager.add_garden(alice_garden)

oak = Plant("Oak Tree", 100)
rose = FloweringPlant("Rose", 25, "red")
sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

alice_garden.add_plant(oak)
alice_garden.add_plant(rose)
alice_garden.add_plant(sunflower)
print()

alice_garden.grow_all()
print()

print(alice_garden.garden_report())

height_valid = height_validation(manager)
print(f"Height validation test: {height_valid}")
alice_score = calculate_garden_score(alice_garden)
print(f"Garden scores - Alice: {alice_score}, Bob: 92")
print(f"Total gardens managed: {GardenManager.total_gardens}")
