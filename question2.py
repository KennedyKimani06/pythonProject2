def input_until_exit():
    inputs = ["Hello", "Python", "exit"]  # Simulated input
    for user_input in inputs:
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        print(f"You entered: {user_input}")

# Run the function
print("While Loop with Input Simulation:")
input_until_exit()
