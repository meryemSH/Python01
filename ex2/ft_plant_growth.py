class Plant:
    def __init__(self, name, height, age_old):
        self.name = name
        self.height = height
        self.age_old = age_old

    def grow(self):
        """
        Increases the height of the plant by 1 cm.
        """
        self.height += 1

    def age(self):
        """
        Increases the age of the plant by 1 day.
        """
        self.age_old += 1

    def get_info(self):
        """
        Prints the current information of the plant: name, height, and age.
        """
        print(f"{self.name}: {self.height}cm, {self.age_old} days old")


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)

print("=== Day 1 ===")
rose.get_info()
start_height = rose.height
for i in range(6):
    rose.grow()
    rose.age()
print("=== Day 7 ===")
rose.get_info()
end_height = rose.height

print(f"Growth this week: +{end_height - start_height}cm")
