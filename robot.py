
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

	def tax_per_product(self):
		totaltax = self.price * self.count * self.tax - self.count * self.price
		if self.price * self.count * self.tax > 500:
			return 0.9 * totaltax 
		else: 
			return totaltax

products = [
Product(price=900, count=2, tax=1.25, name="Robot"), 
Product(price=100, count=1, tax=1.06, name="Book"),
Product(price=20, count=1, tax=1.25, name="Ice Cream"),
]

total_price = 0

# IMPORT PDF EDITOR
from fpdf import FPDF

# CREATE NEW PDF AND ADD A PAGE
pdf = FPDF()
pdf.add_page()

# SET FONT TO HEADER SIZE
pdf.set_font('Arial', 'B', 16)

# PRINT A HEADER
pdf.cell(40, 10, 'Sannas kvitto', 0, 1)

# SET FONT TO NORMAL SIZE
pdf.set_font('Arial', '', 12)

for product in products:
	print("Produkt: {:10} Antal: {:<10} Pris: {:>7} kr".format(product.name, product.count, product.price_with_tax()))
	# ADD THE SAME LINE TO THE PDF FILE
	pdf.cell(40, 10, "Produkt: {:10} Antal: {:<10} Pris: {:>7} kr".format(product.name, product.count, product.price_with_tax()), 0, 1)

print("-"*80) # streckad linje

# ADD THE STRECKAD LINJE TO THE PDF AS WELL
pdf.cell(40, 10, "-"*80, 0, 1)

total_tax = 0

for product in products:
	total_tax = total_tax + product.tax_per_product()


for product in products:
	total_price = total_price + product.price_with_tax()
print("\nTotalsumma: {:>39} kr".format(total_price))

# ADD THE TOTALSUMME TO THE PDF
pdf.cell(40, 10, "\nTotalsumma: {:>39} kr".format(total_price), 0, 1)

#line break \n
#Måsvingar där formateringen och variabeln ska in. 7 står för avståndet. Blir som en formaterad klass.


print("Varav moms: {:>39} kr".format(total_tax))

# AND ADD THE THE MOMS TO THE PDF
pdf.cell(40, 10, "\nTotalsumma: {:>39} kr".format(total_price), 0, 1)

# SAVE THE PDF TO DISK
pdf.output('sannas_fina_kvitto.pdf', 'F')  # SAVE PDF TO DISK
