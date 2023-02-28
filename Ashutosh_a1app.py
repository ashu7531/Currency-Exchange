import Ashutosh_a1
old=input('Enter original currency: ').upper()
new=input('Enter required currency: ').upper()
amt=input('Enter original amount: ')
if(not(Ashutosh_a1.is_currency(old))):
	print(old," is not a valid currency")
	quit()
if(not(Ashutosh_a1.is_currency(new))):
	print(new," is not a valid currency")
	quit()

a=Ashutosh_a1.exchange(old,new,amt)
print(f'You can exchange {amt} {old} for {a} {new} .')

