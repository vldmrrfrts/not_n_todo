import csv
import os
from tabulate import tabulate


class Task:
    def __init__(self, title, description, due_date, status):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def write(self):
        with open("task.csv", "r", newline="") as csvfile:
            content = csvfile.read()
            if content == "":
                with open("task.csv", "w", newline="") as csvfile:
                    fieldnames = ["Title", "Description", "Due Date", "Status"]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect="excel")
                    writer.writeheader()
        with open("task.csv", "a", newline="") as csvfile:
            fieldnames = ["Title", "Description", "Due Date", "Status"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Title': self.title, 'Description': self.description, 'Due Date': self.due_date, 'Status': self.status})


def main():
    show_command()
    while True:
        try:
            match func := input("Function: ").strip():
                case "add":
                    add_task()
                case "view":
                    view_tasks()
                case "mark":
                    complete_task()
                case "del":
                    delete_task()
                case "clear":
                    raise SyntaxError
                case _:
                    raise ValueError
        except SyntaxError:
            os.system('cls' if os.name == 'nt' else 'clear')
            show_command()
            pass
        except ValueError:
            print("Invalid function!")
        except EOFError:
            print("")
            break


def add_task():
    title = input("Title: ")
    description = input("Description: ")
    due_date = input("Due Date: ")

    new_task = Task(title, description, due_date, status=("Incomplete"))
    new_task.write()


def view_tasks():
    with open("task.csv") as csvfile:
        print(tabulate(csv.DictReader(csvfile), headers="keys", tablefmt="grid"))


def complete_task():
    complete = input("Task Completed: ")
    with open("task.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        row = list(reader)
        for task in row:
            if complete == task["Title"]:
                task["Status"] = "Complete"
        with open("task.csv", "w", newline="") as csvfile:
                fieldnames = ["Title", "Description", "Due Date", "Status"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames,dialect="excel")
                writer.writeheader()
                writer.writerows(row)


def delete_task():
    delete = input("Task to be Deleted: ")
    with open("task.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        new_rows = []
        for task in reader:
            if delete != task["Title"]:
                new_rows.append(task)
        with open("task.csv", "w", newline="") as csvfile:
                fieldnames = ["Title", "Description", "Due Date", "Status"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(new_rows)


def show_command():
    print("""
    _____________________________________
    ===========Task Tracker==============

    add      | Add Task
    view     | View Tasks
    mark     | Mark Tasks Completed
    del      | Delete Tasks
    clear    | Restart
    Ctrl + D | Exit
    _____________________________________
    """)


if __name__ == "__main__":
    main()
