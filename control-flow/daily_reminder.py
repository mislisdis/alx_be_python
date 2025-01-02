
# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()  # Convert to lowercase for uniform handling
time_bound = input("Is it time-bound? (yes/no): ").lower()  # Convert to lowercase for uniform handling

# Process the task based on priority
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = "Invalid priority level entered."


if time_bound == "yes":
    message += " that requires immediate attention today!"
elif time_bound == "no":
    message += ". Consider completing it when you have free time."
else:
    message = "Invalid input for time-bound status."

# Print the reminder
print(f"\nReminder: {message}")
