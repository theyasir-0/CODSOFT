# Simple To-Do List

tasks = []

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task Added!")

    elif choice == "2":
        if tasks == []:
            print("No Tasks Found")
        else:
            print("\nTasks:")
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])

    elif choice == "3":
        if tasks == []:
            print("No Tasks To Update")
        else:
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])

            n = int(input("Enter task number: "))
            if n <= len(tasks):
                tasks[n - 1] = input("Enter new task: ")
                print("Task Updated!")
            else:
                print("Invalid Number")

    elif choice == "4":
        if tasks == []:
            print("No Tasks To Delete")
        else:
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])

            n = int(input("Enter task number: "))
            if n <= len(tasks):
                tasks.pop(n - 1)
                print("Task Deleted!")
            else:
                print("Invalid Number")

    elif choice == "5":
        print("Program Closed")
        break

    else:
        print("Wrong Choice")