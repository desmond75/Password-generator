"""Password geenrator program wrriten in python 
   By: Fon Desmond Ade
   Email: adedesmond6@gmail.com"""


import random 

capital_letters = 'ABCDEFGHIKLMNOPQRSTVXYZ'
lower_letters = 'AbCDEFGHIKLMNOPQRSTVYZ'.lower()
special_characters = '@$^&*()|?><<"?|/[]{\}'
numbers = '0123456789'


def weak_password():

	"""Generate password mix with upper letters,
	   lower letters and numbers  """

	password = ""
	group_of_selected_characters = []#list to group randomly selected characters
	
	for n in range(3):
		"""Select 3 characters from each of the 3 categories """
		upp = random.choice(capital_letters)
		num = random.choice(numbers)
		low = random.choice(lower_letters)

		password += upp
		password += num
		password += low

	return password


def strong_password():

	"""Generate password mix with upper,
	   lower,numbers and special characters """

	password = ""

	for n in range(6):
		"""Select 6 characters from each of the 4 categories """
		upp = random.choice(capital_letters)
		num = random.choice(numbers)
		low = random.choice(lower_letters)
		spec = random.choice(special_characters)
        #add each character to the list group_of_selected_characters
		password += upp
		password += num 
		password += low
		password += spec
	
	return password

def main():
	"""calls weak and strong password generator functions"""

	print("""
	    	Welcome to password generator 
	    	You have two choices to choose
	    	from.You can either choose to have 
	    	a strong or weak password generated 
	    	you.Have fun generating your password
	    	"""
    	)


	try:
	    password_choice = int(input('''Enter [2] for strong password and [3] for weak password'''))
	    if password_choice not in [2, 3]:
	    	print('Invalid choice')
	    if password_choice == 2:
	    	password = strong_password()
	    	print('This is your password as requested >>>>  {} '.format(password))
	    elif password_choice == 3:
	    	password = weak_password()
	    	print('This is your password as requested>>>   {} '.format(password))
	except:
		print('Enter a choice')

if __name__ == '__main__':
	main()
