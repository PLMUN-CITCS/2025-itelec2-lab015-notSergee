# Initialize the total sum variable
total_sum = 0

# Start an infinite loop
while True:
    # Prompt the user for input
    user_input = input("Enter a number (or 'stop' to finish): ")

    # Check if the user wants to stop
    if user_input.strip().lower() == "stop":
        break  # Exit the loop

    # Try to convert input to a number and add to total_sum
    try:
        number = float(user_input)
        total_sum += number
    except ValueError:
        print("Invalid input. Please enter a numeric value or 'stop'.")

# Print the final total sum
print("The total sum is:", total_sum)
