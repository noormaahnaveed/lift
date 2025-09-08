# Lift Simulation Program

current_floor = 0 # Lift initially at floor 1

while True:
    button = input("\nPress 0 to call the lift OR 'q' to quit: ")

    # Exit condition
    if button.lower() == "q":
        print("Simulation ended. Goodbye!")
        break

    # Function for door opening
    def func1():
        print("\nLift is coming...")
        print(":door is opening:")
        print("Available floors: 1 to 14")

    # Function for door closing
    def func2():
        print(":door is closing:")

    # Call lift only if 0 is pressed
    if button == "0":
        func1()

        try:
            num = int(input("Enter the floor number you want to go: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 14.")
            continue

        func2()

        # Validate floor range
        if 0 <= num <= 14:
            # Lift going UP
            if num > current_floor:
                print("Lift is going up...")
                for f in range(current_floor + 1, num + 1):
                    print(f"Floor {f}...")
                print(f"Lift reached floor {num}. :door opening:")

            # Lift going DOWN
            elif num < current_floor:
                print("Lift is going down...")
                for f in range(current_floor - 1, num - 1, -1):
                    print(f"Floor {f}...")
                print(f"Lift reached floor {num}. :door opening:")

            else:
                print(f"Lift is already at floor {current_floor}. :door opening:")

            # Update current floor
            current_floor = num

        else:
            print(" This floor is not available. Please select between 1 and 14.")

    else:
        print(" Invalid button. Press 0 to call the lift or 'q' to quit.")