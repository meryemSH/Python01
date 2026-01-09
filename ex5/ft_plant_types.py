class Plant:
    """
    Base class representing a generic plant."""

    def __init__(self, name, height, age):
        """
        Initializes a Plant instance.
        """
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        """
        Prints information about the plant.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days")


class Flower(Plant):
    """
    Represents a flowering plant, inheriting from Plant.

    Attributes:
        color (str): Color of the flower.
    """

    def __init__(self, name, height, age, color):
        """
        Initializes a Flower instance.

        Args:
            name (str): Name of the flower.
            height (int): Height in centimeters.
            age (int): Age in days.
            color (str): Color of the flower.
        """
        super().__init__(name, height, age)
        self.color = color

    def get_info(self):
        """
        Prints detailed information about the flower, including its color.
        """
        print(f"{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")

    def bloom(self):
        """
        Prints a message indicating the flower is blooming.
        """
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """
    Represents a tree, inheriting from Plant.

    Attributes:
        trunk_diameter (int): Diameter of the tree trunk in centimeters.
    """

    def __init__(self, name, height, age, trunk_diameter):
        """
        Initializes a Tree instance.

        Args:
            name (str): Name of the tree.
            height (int): Height in centimeters.
            age (int): Age in days.
            trunk_diameter (int): Diameter of the trunk in centimeters.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_info(self):
        """
        Prints detailed information about the tree, including trunk diameter.
        """
        print(f"{self.name} (Tree): {self.height}cm, "
              f"{self.age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self):
        """
        Prints a message indicating the tree provides shade.
        """
        print(f"{self.name} provides 78 square meters of shade")


class Vegetable(Plant):
    """
    Represents a vegetable, inheriting from Plant.

    Attributes:
        harvest_season (str): The season when the vegetable is harvested.
        nutritional_value (str): Key nutritional benefit of the vegetable.
    """

    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """
        Initializes a Vegetable instance.

        Args:
            name (str): Name of the vegetable.
            height (int): Height in centimeters.
            age (int): Age in days.
            harvest_season (str): Harvest season.
            nutritional_value (str): Key nutrient.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        """
        Prints detailed information about the vegetable,
        including harvest season.
        """
        print(f"{self.name} (Vegetable): {self.height}cm, "
              f"{self.age} days, {self.harvest_season} harvest")

    def nutrition(self):
        """
        Prints a message about the vegetable's nutritional value.
        """
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 25, "yellow")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 450, 1500, 40)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 30, 70, "spring", "vitamin A")

    print()
    rose.bloom()
    print()
    oak.produce_shade()
    print()
    tomato.nutrition()
