# TaskMaster: Command-Line To-Do Manager

tasks = []

def show_menu():
    print("\n--- TaskMaster Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            status = "✓" if task["done"] else "✗"
            print(f"{i+1}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    print("Task added!")

def mark_task_done():
    view_tasks()
    if len(tasks) == 0: return
    choice = int(input("Enter task number to mark done: ")) - 1
    if 0 <= choice < len(tasks):
        tasks[choice]["done"] = True
        print("Task marked as done!")

def delete_task():
    view_tasks()
    if len(tasks) == 0: return
    choice = int(input("Enter task number to delete: ")) - 1
    if 0 <= choice < len(tasks):
        tasks.pop(choice)
        print("Task deleted!")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1": view_tasks()
    elif choice == "2": add_task()
    elif choice == "3": mark_task_done()
    elif choice == "4": delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")