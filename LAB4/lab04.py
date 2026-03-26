def main():
    tasks = {}
    n = int(input("please enter the number of tasks: "))

    for i in range(n):
        task = input("please enter the task name: ")
        dep_count = int(input(f"how many input dependencies for {task}? "))

        deps = []
        for j in range(dep_count):
            dep = input(f"please enter the dependency {j + 1}: ")
            deps.append(dep)

        tasks[task] = deps

    print("\nTASK STRUCTURE:")
    for t in tasks:
        print(f"{t} -> {tasks[t]}")

    print("\nINITIAL TASKS (no dependencies):")
    initial = [t for t in tasks if len(tasks[t]) == 0]

    if not initial:
        print("None")
    else:
        for t in initial:
            print(t)

    completed = set()
    execution_order = []

    print("\nEXECUTION ORDER:")
    step = 1

    while len(completed) < len(tasks):
        progress = False

        for task in tasks:
            if task not in completed:
                if all(dep in completed for dep in tasks[task]):
                    execution_order.append(task)
                    completed.add(task)
                    print(f"Step {step}: {task}")
                    step += 1
                    progress = True

        if not progress:
            print("No task can be started.")
            print("ERROR: Circular dependency detected!")
            print("These tasks could not be completed:")
            for task in tasks:
                if task not in completed:
                    print(task)
            return

    print("ALL TASKS COMPLETED SUCCESSFULLY")


main()