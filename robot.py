
# Nummer 8, classes + init + loop för product så jag slipper def allt i total_price
# Varje product def i listan products. Tillhör även klassen Product.

#La till rabatt när en produkt överskrider 500 kr

class Product:
	def __init__(self, price, count, tax, name):
		self.price = price
		self.count = count
		self.tax = tax
		self.name = name
	def price_with_tax(self):
		total = self.price * self.count * self.tax 
		if total > 500:
			return 0.9 * total #här läggs rabatten på 10% till
		else: 
			return total #annars ingen rabatt

products = [
Product(price=900, count=2, tax=1.25, name="Robot"), 
Product(price=100, count=1, tax=1.06, name="Book"),
Product(price=20, count=1, tax=1.25, name="Ice Cream"),
]

total_price = 0


for product in products:
	print("Produkt: {:10} Antal: {:<10} Pris: {:>7} kr".format(product.name, product.count, product.price_with_tax()))

print("-"*80) # streckad linje

for product in products:
	total_price = total_price + product.price_with_tax()
print("Totalsumma: {:>39} kr".format(total_price))

#Måsvingar där formateringen och variabeln ska in. 7 står för avståndet. Blir som en formaterad klass.
