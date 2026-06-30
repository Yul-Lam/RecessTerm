import random
import string
from datetime import datetime, timedelta
from time import perf_counter


def generate_mock_tasks(count=100_000, start_date=None, days_span=180):
    """Generate mock task records with string deadlines."""
    if start_date is None:
        start_date = datetime(2026, 6, 1)

    tasks = []
    for i in range(count):
        name = f"Task-{i:06d}"
        priority = random.randint(1, 5)
        deadline_date = start_date + timedelta(days=random.randint(0, days_span))
        tasks.append(
            {
                "name": name,
                "priority": priority,
                "deadline": deadline_date.strftime("%Y-%m-%d"),
            }
        )

    return tasks


def parse_task_dates(tasks):
    """Convert string deadlines into datetime objects in-place."""
    for task in tasks:
        if isinstance(task["deadline"], str):
            task["deadline"] = datetime.strptime(task["deadline"], "%Y-%m-%d")
    return tasks


def sort_tasks(tasks):
    """Sort by priority (ascending) then deadline (earliest first)."""

    def sort_key(task):
        return task["priority"], task["deadline"]

    return sorted(tasks, key=sort_key)


def due_within_next_days(tasks, days=3, reference_time=None):
    """Filter tasks with deadlines due within the next `days` days."""
    reference_time = reference_time or datetime.now()
    end_time = reference_time + timedelta(days=days)
    return [
        task
        for task in tasks
        if reference_time <= task["deadline"] <= end_time
    ]


def build_task_index(tasks):
    """Build a dictionary index for O(1) lookup by task name."""
    return {task["name"]: task for task in tasks}


def find_task_by_name(task_index, task_name):
    """Lookup a task by name using the dictionary index."""
    return task_index.get(task_name)


def benchmark(task_count=100_000):
    """Benchmark sorting vs dictionary lookup for the task list."""
    tasks = generate_mock_tasks(count=task_count)

    parse_task_dates(tasks)

    start_sort = perf_counter()
    sorted_tasks = sort_tasks(tasks)
    end_sort = perf_counter()

    start_index = perf_counter()
    task_index = build_task_index(tasks)
    end_index = perf_counter()

    lookup_name = sorted_tasks[0]["name"]
    start_lookup = perf_counter()
    found_task = find_task_by_name(task_index, lookup_name)
    end_lookup = perf_counter()

    due_tasks = due_within_next_days(tasks, days=3)

    print("Benchmark results for", task_count, "tasks")
    print("- Sort time:      ", f"{end_sort - start_sort:.6f}s")
    print("- Index build time:", f"{end_index - start_index:.6f}s")
    print("- Dictionary lookup:", f"{end_lookup - start_lookup:.9f}s")
    print("- Tasks due in next 3 days:", len(due_tasks))
    print("- Example found task:", found_task)
    print("- First 3 sorted tasks:")
    for task in sorted_tasks[:3]:
        print("  ", task)

    return {
        "sorted_count": len(sorted_tasks),
        "due_count": len(due_tasks),
        "found_task": found_task,
    }


if __name__ == "__main__":
    benchmark()
