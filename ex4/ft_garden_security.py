class SecurePlant:
    """
    Represents a secure plant with encapsulated height and age attributes.

    This class protects sensitive data (height and age) from invalid changes
    by providing getter and setter methods with validation. Negative values
    for height or age are rejected to maintain data integrity.

    Attributes:
        name (str): The name of the plant.
        _height (int/float): The height of the plant in centimeters (private).
        __age (int): The age of the plant in days (private).
    """
    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age
        print(f"Plant created: {self.name}")

    def get_height(self):
        """Returns the current height."""
        return self._height

    def get_age(self):
        """Returns the current age."""
        return self._age

    def set_height(self, value):
        """
        Updates the height of the plant if the value is valid (non-negative).
        """
        if value >= 0:
            self._height = value
            print(f"Height updated: {value}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, value):
        """
        Updates the age of the plant if the value is valid (non-negative).
        """
        if value >= 0:
            self._age = value
            print(f"Age updated: {value} days [OK]")
        else:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose", 15, 100)

    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-5)
    print()
    print(
        f"Current plant: {plant.name} "
        f"({plant.get_height()}cm, {plant.get_age()} days)"
    )
