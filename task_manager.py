import json

# Dummy login credentials
DUMMY_EMAIL = "mnkglobal@example.com"
DUMMY_PASSWORD = "mnk123"

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if email == DUMMY_EMAIL and password == DUMMY_PASSWORD:
        print("Login successful!\n")
    else:
        print("Invalid email or password. Please try again.")
        exit()

class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def __str__(self):
        return f"ID: {self.id}, TITLE: {self.title}, STATUS: {'COMPLETED' if self.completed else 'NOT COMPLETED'}"

tasks = []

def add_task(title):
    task_id = len(tasks) + 1
    new_task = Task(task_id, title)
    tasks.append(new_task)

def view_tasks():
    if not tasks:
        print("No tasks available. ADD the Task")
        return
    print("\nID, TITLE, STATUS")
    for task in tasks:
        print(task)

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]

def mark_task_complete(task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            break

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump([task.__dict__ for task in tasks], file)

def load_tasks():
    global tasks
    try:
        with open('tasks.json', 'r') as file:
            task_data = json.load(file)
            tasks = [Task(task['id'], task['title'], task['completed']) for task in task_data]
    except FileNotFoundError:
        tasks = []

def main():
    login()
    load_tasks()
    while True:
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task Complete")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            add_task(title)
            save_tasks()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
            save_tasks()
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as complete: "))
            mark_task_complete(task_id)
            save_tasks()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()