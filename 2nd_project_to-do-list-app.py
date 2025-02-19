import os

# File to store tasks
TASK_FILE = "tasks.txt"

# Load tasks from the file (if it exists)
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    else:
        return []

# Save tasks to the file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to display tasks
def view_tasks(tasks):
    if tasks:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks found. Please add some tasks.")

# Main task management function
def task_management():
    tasks = load_tasks()  # Load existing tasks from file
    print("----WELCOME TO THE TASK MANAGEMENT APP----")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Add a Task")
        print("2. Update a Task")
        print("3. Delete a Task")
        print("4. View Tasks")
        print("5. Exit")

        try:
            operation = int(input("Enter your choice (1-5): "))
            
            if operation == 1:
                task_name = input("Enter the task you want to add: ")
                tasks.append(task_name)
                save_tasks(tasks)  # Save the tasks after adding
                print(f"Task '{task_name}' has been successfully added.")
            
            elif operation == 2:
                view_tasks(tasks)
                task_num = int(input("\nEnter the task number to update: "))
                if 1 <= task_num <= len(tasks):
                    new_task = input("Enter the updated task: ")
                    tasks[task_num - 1] = new_task
                    save_tasks(tasks)
                    print(f"Task {task_num} has been updated to '{new_task}'.")
                else:
                    print("Invalid task number. Try again.")
            
            elif operation == 3:
                view_tasks(tasks)
                task_num = int(input("\nEnter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"Task '{removed_task}' has been deleted.")
                else:
                    print("Invalid task number. Try again.")
            
            elif operation == 4:
                view_tasks(tasks)
            
            elif operation == 5:
                print("Saving and closing the program...")
                break
            
            else:
                print("Invalid Input. Please choose a number between 1 and 5.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Run the task management system
if __name__ == "__main__":
    task_management()

