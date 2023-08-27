class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True

    def list_tasks(self):
        for index, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else " "
            print(f"{index + 1}. [{status}] {task['task']}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)


def main():
    manager = ToDoListManager()

    while True:
        print("To-Do List Manager")
        print("1. Add Task")
        print("2. Mark Completed")
        print("3. List Tasks")
        print("4. Remove Task")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            task = input("Enter task: ")
            manager.add_task(task)
        elif choice == 2:
            index = int(input("Enter task index: ")) - 1
            manager.mark_completed(index)
        elif choice == 3:
            manager.list_tasks()
        elif choice == 4:
            index = int(input("Enter task index: ")) - 1
            manager.remove_task(index)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
