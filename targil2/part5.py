def task_manager():
    tasks = {}

    def add_task(task, status="incomplete"):
        nonlocal tasks
        tasks[task] = status
    
    def get_tasks():
        return tasks

    def complete_task(task):
        if task in tasks:
            tasks[task] = "complete"

    return {
        'add_task': add_task,
        'get_tasks': get_tasks,
        'complete_task': complete_task
    }

tasks_manager = task_manager()

# adding tasks
tasks_manager['add_task']("Write email")
tasks_manager['add_task']("Shopping", "in progress")
tasks_manager['add_task']("Homework")

# get all the tasks
current_tasks = tasks_manager['get_tasks']()
print(current_tasks)

#mark it as complate
tasks_manager['complete_task']("Write email")

# get the updated tasks list
current_tasks = tasks_manager['get_tasks']()
print(current_tasks)
