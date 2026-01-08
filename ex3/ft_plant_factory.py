class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


class PlantFactory:
    def factory(self, data):
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
