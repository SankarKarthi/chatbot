import re

# Define a function to perform the math operation based on the user's input
def calculate(user_input):
    # Use regular expressions to extract the numbers and operation from the user's input
    match = re.search(r'(\d+) ([+\-*/]) (\d+)', user_input)
    if match:
        num1 = int(match.group(1))
        operator = match.group(2)
        num2 = int(match.group(3))
        
        # Perform the appropriate math operation
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
            
        return result
    else:
        return None

# Define the main function to handle user input and generate responses
def chat():
    print("Hi! I'm a math bot. I can perform basic mathematical operations.")
    while True:
        user_input = input("What would you like me to calculate? ")
        if user_input.lower() in ('bye', 'exit', 'quit'):
            print("Goodbye!")
            break
        
        result = calculate(user_input)
        if result is not None:
            print(f"The answer is {result}.")
        else:
            print("Sorry, I didn't understand that. Please try again.")

# Call the main function to start the chat bot
if __name__ == '__main__':
    chat()
