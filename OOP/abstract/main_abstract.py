from abstract import Vehicle
class Bike(Vehicle):
    def __init__(self, n, color):
        super().__init__(n)
        self.color: color
    def start(self):
        print("Start with Kick")