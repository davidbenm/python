class Clothing:
    stock = { 'name':[], 'material':[], 'amount':[]}
    def __init__(self,name):
        self.name = name
    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)
    def Stock_by_Material(self, material):
        count = 0
        for item, amount in zip(Clothing.stock['material'], Clothing.stock['amount']):
            if item == material:
                count += amount
        return count

class shirt(Clothing):
    material="Cotton"
class pants(Clothing):
    material="Cotton"
  
polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)