# 05/04/20

def pay_check():
	your_pay = float(input('How much do you make? '))
	your_hours = int(input('How many hours did you work? '))
	if your_hours > 40:
		print((your_pay * 1.5) * your_hours)
	elif your_hours >= 40:
		print(your_hours * your_pay)
		

pay_check()
