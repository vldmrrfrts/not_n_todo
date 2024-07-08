# not_n_todo
![Python](https://img.shields.io/badge/python%203.12.4-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pytest](https://img.shields.io/badge/passing-green?style=for-the-badge&logo=Pytest)
![Windows](https://img.shields.io/badge/made%20in%20windows-blue?style=for-the-badge&logo=Windows)
![GitHub](https://img.shields.io/badge/open%20for%20pulls-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![edX](https://img.shields.io/badge/edX-%2302262B.svg?style=for-the-badge&logo=edX&logoColor=white)

![main menu/commands of the program](https://github.com/vldfrts/not_n_todo/assets/172185952/ad91cace-c0e5-44f8-915c-397a315e7056)

"not_n_todo" is a Python-written command line interface program dedicated to managing tasks effectively and efficiently. This is the much more complicated version of my CS50P Final Project (Task Manager) complete with the core functionality of the base version but with additional reading, writing, and appending capability to a CSV file to store the tasks.

It's called not_n_todo after I simplified and made the words "To do and not to do" more fun. 
> Yeah.. Lmao

You may see the base version of this which is my final project in CS50P at: https://youtu.be/CdcH_jJYYF8?si=qOw4Qiios2_IOJ0S

> [!IMPORTANT]
> This was created using Python 3.12.4, and this program specifically requires you to import the CSV, os, and tabulate modules.
> If Python or the modules are not installed yet, make sure you have Python in your device; and run this in the terminal one by one:
```
pip install csv
pip install os
pip install tabulate
```
You may see the full Python Docs at: https://docs.python.org/3/

## SUGGESTIONS | :D
Suggestions to improve and/or shorten this code will be much appreciated:D
> Create a pull request

## HOW DOES IT WORK?
This ultra-simplistic command line interface program is dedicated to managing tasks effectively and efficiently. 
> The worst part about this is that I took 6 hours to figure out how all of this works:(

A Task object is summoned to create a new CSV file if there is not an existing one yet, and append to the file the user's task Title, Description, Due Date, and Status, based on the corresponding object parameters.
```python
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
```

It also initializes the object itself.
> I went with this approach as I want to learn object-oriented programming.

A variable assigned to a string is then called to show the program's commands if printed.
```python
commands = """
    _______________________________________
    ===========not_n_todo==================

    add      | Add Task
    view     | View Tasks
    mark     | Mark Tasks Completed
    unmark   | Unmark Tasks
    del      | Delete Tasks
    clear    | Restart
    Ctrl + D | Exit

    A command line interface task manager.
    _______________________________________
    """
```

Then the main function is created that manages and is responsible for the program's loop system via an infinite loop and a match case statement for maximum efficiency.
> I used a match/case since I prefer it rather than an if/else, plus, it looks cooler - I guess...
```python
def main():
    print(commands)
    while True:
        try:
            match func := input("Function: ").strip():
                case "add":
                    add_task()
                case "view":
                    view_tasks()
                case "mark":
                    complete_task()
                case "unmark":
                    uncomplete_task()
                case "del":
                    delete_task()
                case "clear":
                    raise SyntaxError
                case _:
                    raise ValueError
        except SyntaxError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(commands)
            pass
        except ValueError:
            print("Invalid function!")
        except EOFError:
            print("")
            break
```

### IF "FUNC" IS...

### add
 The add_task function is initiated where the user is asked for certain parameters to be assigned to each parameter in the Task object; where it is appended to a CSV file called task.csv.
```python
def add_task():
    title = input("Title: ")
    description = input("Description: ")
    due_date = input("Due Date: ")

    new_task = Task(title, description, due_date, status=("Uncompleted"))
    new_task.write()
```
### view
 The view_tasks function is initiated where it iterates over the task.csv file and prints its contents herein in a tabulated format.
 > Using the tabulate module
```python
def view_tasks():
    with open("task.csv") as csvfile:
        print(tabulate(csv.DictReader(csvfile), headers="keys", tablefmt="grid"))
```
### mark
 The complete_task function is initiated when it accepts the user's input from the main which is the task title that will be marked "Completed". It then checks if the title is equivalent to the user input; if yes, the status will be amended to "Completed".
 > Else, nothing will happen...
```python
def complete_task():
    complete = input("Task Completed: ")
    with open("task.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        row = list(reader)
        for task in row:
            if complete == task["Title"]:
                task["Status"] = "Completed"
        with open("task.csv", "w", newline="") as csvfile:
                fieldnames = ["Title", "Description", "Due Date", "Status"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames,dialect="excel")
                writer.writeheader()
                writer.writerows(row)
```
### unmark
 The uncomplete_task function is initiated when it accepts the user's input from the main which is the task title that will be marked "Uncompleted". It then checks if the title is equivalent to the user input; if yes, the status will be amended to "Uncompleted".
 > Else, nothing will happen...
```python
def uncomplete_task():
    uncomplete = input("Task Completed: ")
    with open("task.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        row = list(reader)
        for task in row:
            if uncomplete == task["Title"]:
                task["Status"] = "Uncompleted"
        with open("task.csv", "w", newline="") as csvfile:
                fieldnames = ["Title", "Description", "Due Date", "Status"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames,dialect="excel")
                writer.writeheader()
                writer.writerows(row)
```
### del
 The delete_task function is initiated when it accepts the user's input from the main which is the task title that will be deleted. It then checks if the title is equivalent to the user input; if yes, the entire task is removed from the list.
 > Else, nothing will happen... Even if it is already deleted and this function is rerun, it will not throw an error and will not delete any other task.
 ```python
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
 ```
 ### clear
 The main function will raise a SyntaxError that would be accepted by the exception for the same error; this accomplishes the terminal clearing and reinitializes the program while not deleting the tasks contained within.
 > Using the os module...
 ```python
except SyntaxError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(commands)
 ```
 > commands is the variable that stores the string of the commands allowed

### Ctrl + D
 The main function will raise an EOFError that would be accepted by the exception for the same error; this ends the infinite loop induced by the "while True" loop thus ending the program.
 ```python
except EOFError:
            print("")
            break
 ```
 > print("") is used to have a new line after the program is terminated to prevent the terminal from immediately succeeding the killed statement, like this:
 ```
 func = project/ $
```
### ValueError (Invalid Function)
If the user input for functions is not within the lists of commands, it will raise a ValueError thus resulting in a reprompt.
```python
 except ValueError:
    print("Invalid function!")
 ```




