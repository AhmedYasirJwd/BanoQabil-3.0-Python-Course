""" Ahmed Yasir
 ahmedyasirjwd@gmail.com """

import csv

# file initialization
def read_tasks(filename='tasks.csv'):
    tasks = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'Task' in row:
                    tasks.append({'Task': row['Task']})
    except FileNotFoundError:
        pass

    
    return tasks

# writing a task

def write_tasks(tasks, filename='tasks.csv'):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['Task']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)

# Adding a task

def add_task(task, filename='tasks.csv'):
    tasks = read_tasks(filename)
    tasks.append({'Task': task})
    write_tasks(tasks, filename)

# removing a task

def remove_task(task_index, filename='tasks.csv'):
    tasks = read_tasks(filename)
    if 0 <= task_index + 1 < len(tasks):
        tasks.pop(task_index)
        write_tasks(tasks, filename)
        return True
    else:
        return False

# viewing a task

def view_tasks(filename='tasks.csv'):
    tasks = read_tasks(filename)
    if not tasks:
        print("\t\t\t\tNo tasks found.")
    else:
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task['Task']}")

# Main Function of the program (this includes the flow of the program)

def main():
    
    while True:

        print("\n\t\t\t\t\t\t\t\t\033[1mPython To-do List\033[0m")
        view_tasks()

        # Print all the options 

        print("\n\t\t\t\tSelect any option:")
        print("\t\t\t\t1. Add Task")
        print("\t\t\t\t2. Remove Task")
        print("\t\t\t\t3. Exit")
        choice = input("Choose an option: ")
        
# if user chooses option 1:

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
            print("Task added successfully.")

# if user chooses option 2:

        elif choice == '2':
            try:
                task_index = int(input("Enter the task number to remove: "))-1
                if remove_task(task_index):
                    print("Task removed successfully.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

# if user chooses option 3:

        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()
