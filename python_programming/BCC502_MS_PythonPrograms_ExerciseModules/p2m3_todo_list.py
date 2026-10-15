"""Part 2, Module 3: Build a to-do list that remembers tasks between runs."""

FILENAME = "tasks.txt"


def load_tasks(filename=FILENAME):
    """Read tasks from the file. Return an empty list if it does not exist yet."""
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []


def save_tasks(tasks, filename=FILENAME):
    """Write all tasks to the file, one per line."""
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def main():
    tasks = load_tasks()
    print(f"You have {len(tasks)} task(s).")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")
    while True:
        new_task = input("New task (or type 'quit'): ").strip()
        if new_task.lower() == "quit":
            break
        tasks.append(new_task)
    save_tasks(tasks)
    print("Tasks saved.")


if __name__ == "__main__":
    main()
