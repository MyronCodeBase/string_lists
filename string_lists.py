def string_lists():
	userString = str(input("Enter a word ")) 
	if userString[::-1] == userString:
		print("String is a palindrome!")
	else:
		print("String is not a palindrome")

string_lists()