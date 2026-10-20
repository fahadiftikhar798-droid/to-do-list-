# PROJECT 1: TO-DO LIST - DecodeLabs

my_tasks = []

def add_task(task):
    """MODEL: Data Logic"""
    my_tasks.append(task)
    print(f"Task added: {task}")

def view_tasks():
    """VIEW: User Interface"""
    if not my_tasks:
        print("No tasks yet!")
    else:
        print("\n--- Your To-Do List ---")
        for index, task in enumerate(my_tasks):
            print(f"{index} - {task}")

# --- Main Program Loop ---
while True:
    print("\n1. Add Task | 2. View Tasks | 3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        new_task = input("Enter task: ")
        add_task(new_task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        break
    else:
        print("Invalid choice")