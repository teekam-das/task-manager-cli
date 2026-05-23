tasks = ["SCD Assignment", "Git Practice", "Show Task"]

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Deleted:", task)
    else:
        print("Task not found")

delete_task("Git Practice")

print("Remaining Tasks:", tasks)