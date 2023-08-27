from project import ToDoListManager


def test_add_task():
    manager = ToDoListManager()
    manager.add_task("Buy groceries")
    assert len(manager.tasks) == 1


def test_mark_completed():
    manager = ToDoListManager()
    manager.add_task("Read a book")
    manager.mark_completed(0)
    assert manager.tasks[0]["completed"] is True


def test_remove_task():
    manager = ToDoListManager()
    manager.add_task("Do laundry")
    manager.remove_task(0)
    assert len(manager.tasks) == 0


def test_list_tasks(capsys):
    manager = ToDoListManager()
    manager.add_task("Write code")
    manager.add_task("Exercise")
    manager.list_tasks()
    captured = capsys.readouterr()
    assert "Write code" in captured.out
    assert "Exercise" in captured.out
