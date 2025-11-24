import json
from datetime import datetime

# File to save tasks
TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
        return
    print("\nYour Tasks:")
    print("-" * 50)
    for i, task in enumerate(sorted(tasks, key=lambda x: (x['priority'], x['deadline']))):
        print(f"{i+1}. {task['title']} | Priority: {task['priority']} | Deadline: {task['deadline']}")
    print("-" * 50)

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    priority = input("Enter priority (High/Medium/Low): ").capitalize()
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    # Validate date
    try:
        datetime.strptime(deadline, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Task not added.")
        return
    tasks.append({"title": title, "priority": priority, "deadline": deadline})
    save_tasks(tasks)
    print("Task added successfully!")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{removed['title']}' deleted.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

