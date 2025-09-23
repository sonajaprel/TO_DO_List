# 📋 To-Do List (Console Based)
# Uses a list to store tasks, supports add/remove/view, and saves to a text file.

FILENAME = "tasks.txt"

# Load tasks from file into a list
def load_tasks():
    tasks = []
    try:
        with open(FILENAME, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        pass  # if file doesn't exist, start with empty list
    return tasks

# Save tasks back to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display tasks
def view_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks in your to-do list.\n")
    else:
        print("\n📌 Your To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
        print()

# Add a task
def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"✔ Task '{task}' added.\n")
    else:
        print("⚠ Task cannot be empty!\n")

# Remove a task
def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"🗑 Task '{removed}' removed.\n")
            else:
                print("⚠ Invalid task number.\n")
        except ValueError:
            print("⚠ Please enter a valid number.\n")

# Main loop
def main():
    tasks = load_tasks()
    while True:
        print("==== To-Do List Menu ====")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("👋 Exiting... Your tasks are saved.")
            break
        else:
            print("⚠ Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
