import re
import sys
class UserRegistration:
	
	def first_name_check(self,first_name):
		
		result  = re.search("^[A-Z][a-z]{3,}",first_name)
		if result:
			print("Valid User name")
		else:
			print("Invalid User name")

			
if __name__ == "__main__":

	userregistration_object = UserRegistration()
	first_name=input("Enter the first name : ")
	userregistration_object.first_name_check(first_name)
