import logic
old = input('Enter original currency: ').upper()
new = input('Enter required currency: ').upper()
amt = input('Enter original amount: ')
if(not(logic.is_currency(old))):
	print(old," is not a valid currency")
	quit()
if(not(logic.is_currency(new))):
	print(new," is not a valid currency")
	quit()

conv_amt = logic.exchange(old,new,amt)
print(f'You can exchange {amt} {old} for {conv_amt} {new} .')

