class Plant:
    """
    Represents a plant with a name, height, and age."""
    def __init__(self, name, height, age):
        """
        Initializes a new Plant instance.

        Args:
            name (str): The name of the plant.
            height (int): The height of the plant in centimeters.
            age (int): The age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        """
        Prints information about the plant.
        """
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


class PlantFactory:
    """
    Factory class to create Plant objects from provided data.
    """

    def factory(self, data):
        """
        Creates a Plant object from a list of data.
        Args:
            data: A list containing [name (str), height (int), age (int)].
        Returns:
            Plant: A new instance of the Plant class.
        """
        return Plant(data[0], data[1], data[2])


plant_data = [
    ["Rose", 25, 30],
    ["Oak", 200, 365],
    ["Cactus", 5, 90],
    ["Sunflower", 80, 45],
    ["Fern", 15, 120]
]

factory = PlantFactory()

plants = []

for data in plant_data:
    plant = factory.factory(data)
    plants.append(plant)

print("=== Plant Factory Output ===")
for plant in plants:
    plant.get_info()
print()
print("Total plants created:", len(plants))
