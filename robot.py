
# Nummer 8, classes + init + loop för product så jag slipper def allt i total_price
# Varje product def i listan products. Tillhör även klassen Product.

class Product:
	def __init__(self, price, count, tax):
		self.price = price
		self.count = count
		self.tax = tax
	def price_with_tax(self):
		return self.price * self.count * self.tax

products = [Product (price=900, count=2, tax=1.25), Product(price=100, count=1, tax=1.06)]

total_price = 0

for product in products:
	total_price = total_price + product.price_with_tax()
print(total_price)