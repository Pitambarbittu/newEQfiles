# Create a class BANK and with two function simple interest and compound interest. 
#  U need to create instance for pnb, icici and hdfc banks with corresponding input.

class BANK():

	def __init__(self, bank_name , principal , time , rate) -> None:
		self.bank_name = bank_name
		self.principal = principal
		self.time = time
		self.rate = rate
		self.si = 0
		self.ci = 0

	def simple_interest(self):
		self.si = self.principal * self.time * self.rate / 100
		return self.si

	def compound_interest(self):
		amount = self.principal * (pow( (1 + self.rate/100), self.time) )
		self.ci = amount - self.principal
		return self.ci

	def print_details(self):
		self.simple_interest()
		self.compound_interest()

		print("Bank name:", self.bank_name)
		print("Principal =", self.principal)
		print("Time =", self.time)
		print("Rate =", self.rate)
		print("Simple Interest =", self.si)
		print("Compound Interest =", self.ci)


print("10. Create a class BANK and with two function simple interest and compound interest. U need to create instance for pnb, icici and hdfc banks with corresponding input.\n")

p = int(input ("Enter the Principal Ammount: "))

t = int(input("Enter the time(year): "))

r = int(input("Enter your Rate:  "))

pnb = BANK("\nPunjab National Bank", p , t , r )

icici = BANK("\nICICI Bank", p, t, r)

hdfc = BANK("\nHDFC Bank", p, t, r)

print("The simple interest and the compound interest on the following bank will be as follows")
pnb.print_details()
icici.print_details()
hdfc.print_details()
print()