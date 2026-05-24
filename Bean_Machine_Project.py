import random

def simulate_bean_machine(num_balls, num_slots):
    """Simulates the bean machine and displays the results."""

    slots = [0] * num_slots  # Initialize slots to 0
    slot_width = 3  # Adjust width for histogram display

    for ball in range(num_balls):
        path = ""
        for i in range(num_slots - 1):  # Number of levels is slots - 1
            if random.random() < 0.5:
                path += "L"
            else:
                path += "R"

        print(path)  # Print the path of the ball

        # Calculate the slot index based on the number of 'R's
        slot_index = path.count('R')
        slots[slot_index] += 1  # Increment the ball count in the slot

    # Display the histogram
    max_height = max(slots)  # Find the maximum height for scaling

    for i in range(max_height, 0, -1):  # Iterate from top to bottom
        for slot_count in slots:
            if slot_count >= i:
                print(" * ", end="")  # Print a block if the height is reached
            else:
                print("   ", end="")  # Print spaces otherwise
        print()  # New line for each level

    # Display the base line with slot numbers
    for i in range(num_slots):
        print(f"{i:^{slot_width}}", end="")  # Centered slot numbers
    print()


# Get user input
num_balls = int(input("Enter the number of balls to drop: "))
num_slots = int(input("Enter the number of slots in the bean machine: "))

# Simulate and display the results
simulate_bean_machine(num_balls, num_slots)