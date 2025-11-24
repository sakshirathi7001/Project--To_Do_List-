tasks = []

def show_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Save Tasks")
    print("5. Load Tasks")
    print("6. Exit")
    print("=============================")

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def delete_task():
    show_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to delete: "))
            tasks.pop(task_num - 1)
            print("Task deleted successfully!")
        except (ValueError, IndexError):
            print("Invalid task number!")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks saved to tasks.txt")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            loaded = file.readlines()
            global tasks
            tasks = [task.strip() for task in loaded]
        print("Tasks loaded successfully!")
    except FileNotFoundError:
        print("No saved file found.")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        save_tasks()
    elif choice == "5":
        load_tasks()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
