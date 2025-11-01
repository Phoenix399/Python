class Robot:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def introduce(self):
        print(f"🤖 Hello! I am {self.name}.")
        print(f"I am a {self.model} model robot, built in {self.year}.")
        print("I can help humans with various tasks and learn new things!")


r1 = Robot("Phoenix", "XTR-500", 2025)


r1.introduce()
