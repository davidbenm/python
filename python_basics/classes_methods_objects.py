class Piglet:
    name = "piglet"
    def speak(self):
        print(f"Oink! I'm {self.name}! Oink!")

hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()