import re
import sys


class UserRegistration:
	
	def first_name_check(self,first_name):
		
		pattern = "^[A-Z][a-z]{3,}$"
		result  = re.search(pattern,first_name)
		if result:
			print("Valid First name")
		else:
			print("Invalid First name")

	def last_name_check(self,last_name):
		
		pattern = "^[A-Z][a-z]{3,}$"
		
		result = re.search(pattern,last_name)
		if result:
			print("Valid Last name")
		else:
			print("Invalid Last name")


	def email_check(self,email):
		pattern = "^\w+([+\.-]?\w+)*@(\d?\w+)(\.\w{2,3})(\.\D{2,3})?$"
		result = re.search(pattern,email)
		if result:
			print("Valid Email")

		else:
			print("Invalid Email")


	def mobile_number_check(self,mobile_number):
		pattern="[0-9]{2}[ ]?[0-9]{10}"
		result = re.search(pattern,mobile_number)
		if result:
			print("Valid Mobile number")
		else:
			print("Invalid Mobile number")

	def password_check(self,password):
		pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@$!%*^#?&])[A-Za-z0-9@$!^#%?&]{8,}$"
		pattern_object = re.compile(pattern)
		print("pat",pattern_object)
		subs=re.sub('[\w]+','',password)
		print("subs",subs)
		length = len(re.sub('[\w]+','',password))
		print("length",length)
		search_result = re.search(pattern_object,password)
		print("search result",search_result)
		if length == 1 and search_result is not None:
			print("Password is correct")
		else:
			print("Incorrect password")
	

if __name__ == "__main__":

	userregistration_object = UserRegistration()
	first_name=input("Enter the first name : ")
	userregistration_object.first_name_check(first_name)
	last_name = input("Enter the last name : ")
	userregistration_object.last_name_check(last_name)
	email=input("Enter the email address : ")
	userregistration_object.email_check(email)
	mobile_number = input("Enter the mobile number : ")
	userregistration_object.mobile_number_check(mobile_number)
	password = input("Enter the Password : ")
	userregistration_object.password_check(password)
