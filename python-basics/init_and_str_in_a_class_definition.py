class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return f"This apple is {self.color} and its flavor is {self.flavor}"
    
jonagold = Apple("red", "sweet")
print(jonagold)