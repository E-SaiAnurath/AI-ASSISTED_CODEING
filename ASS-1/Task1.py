# Simple string reversal program
# Implements logic directly in main code (no user-defined functions)

if __name__ == "__main__":
	# Prompt the user for input
	user_input = input("Enter a string to reverse: ")

	# Reverse the string using slicing
	reversed_string = user_input[::-1]

	# Print the reversed string
	print("Reversed string:", reversed_string)

	# Example runs (you can uncomment to test quickly):
	# print('\nSample: Hello ->', 'Hello'[::-1])
	# print('Sample: abc123 ->', 'abc123'[::-1])

