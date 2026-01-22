# Simple Todo Application in Python

todo_list = []

def show_menu():
    print("\n--- TODO APPLICATION ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print("Task added successfully!")

def view_tasks():
    if not todo_list:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def delete_task():
    view_tasks()
    if todo_list:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(todo_list):
            removed = todo_list.pop(task_no - 1)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Exiting Todo App. Bye 👋")
        break
    else:
        print("Invalid choice. Please try again.")
