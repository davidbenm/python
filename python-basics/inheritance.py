class Fruit:
    fruit_name = ""
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return f"This {self.fruit_name} is {self.color} and its flavor is {self.flavor}."
    
class Apple(Fruit):
    fruit_name = "apple"

class Grape(Fruit):
    fruit_name = "grape"
    
jonagold = Apple("red", "sweet")
carnelian = Grape("purple", "sweet")

print(jonagold)
print(carnelian)
