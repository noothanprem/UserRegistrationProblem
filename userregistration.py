import re
import sys
class UserRegistration:
	
	def first_name_check(self,first_name):
		
		pattern = "^[A-Z][a-z]{3,}"
		result  = re.search(pattern,first_name)
		if result:
			print("Valid First name")
		else:
			print("Invalid First name")

	def last_name_check(self,last_name):
		
		pattern = "^[A-Z][a-z]{3,}"
		result = re.search(pattern,last_name)
		if result:
			print("Valid Last name")
		else:
			print("Invalid Last name")

			
if __name__ == "__main__":

	userregistration_object = UserRegistration()
	first_name=input("Enter the first name : ")
	userregistration_object.first_name_check(first_name)
	last_name = input("Enter the last name : ")
	userregistration_object.last_name_check(last_name)
