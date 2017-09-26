
#classes + init = blir lättare än att skapa en tom produkt för att sedan sätta värdena.
# bättre att sätta dem först med init och self. 

class Product:
	def __init__(self, price, count, tax):
		self.price = price
		self.count = count
		self.tax = tax
	def price_with_tax(self):
		return self.price * self.count * self.tax

robot = Product(price=900, count=2, tax=1.25)
book = Product(price=100, count=1, tax=1.06)


print(robot.price_with_tax() + book.price_with_tax())
