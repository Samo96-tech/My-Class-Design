class Hero:
    def __init__(self, name: str, power: str, level: int = 1):
        self._name = name               # Encapsulated attribute
        self._power = power
        self.level = level              # Public attribute

    def description(self) -> str:
        return f"{self._name} (Level {self.level}) wields the power of {self._power}."

    def level_up(self):
        self.level += 1
        print(f"{self._name} has leveled up to {self.level}!")


class Superman(Hero):
    def __init__(self, secret_identity: str):
        # Initialize base class with fixed name and power
        super().__init__(name="Superman", power="Super Strength & Flight", level=5)
        self.secret_identity = secret_identity

    def reveal_identity(self):
        print(f"I am actually {self.secret_identity}!")


if __name__ == "__main__":
    clark = Superman(secret_identity="Clark Kent")
    print(clark.description())
    clark.level_up()
    clark.reveal_identity()
