class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move().")


class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying through the clouds ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing on the water ⛵")


if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        v.move()
