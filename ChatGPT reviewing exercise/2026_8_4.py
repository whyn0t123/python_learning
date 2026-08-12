from pathlib import Path

class Task:
    def __init__(self, title, priority, completed=False):
        self.title = title
        self.priority = priority
        self.completed = completed

    def complete(self):
        self.completed = True

    def show_info(self):
        if self.completed:
            status = "Completed"
        else:
            status = "Not completed"

        return f"Task: {self.title}\nPriority: {self.priority}\nStatus: {status}"
    
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        for index, task in enumerate(self.tasks, 1):
            if task.completed:
                print(f"{index}. {task.title} | Priority: {task.priority} | Done")
            else:
                print(f"{index}. {task.title} | Priority: {task.priority} | Not Done")

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.complete()
                return True

        return False

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                break

    def sort_by_priority(self):
        new_tasks = sorted(self.tasks, key=lambda x: x.priority)
        for task in new_tasks:
            print(f"{task.title} {task.priority}")

    def get_statistics(self):
        total = 0
        completed = 0
        unfinished = 0
        for task in self.tasks:
            total += 1
            if task.completed:
                completed += 1
            else:
                unfinished += 1

        statistics = {}
        statistics["total"] = total
        statistics["completed"] = completed
        statistics["unfinished"] = unfinished

        return statistics

    def save_file(self, filename):
        path = Path(filename)

        lines = []

        for task in self.tasks:
            lines.append(f"{task.title},{task.priority},{task.completed}")

        path.write_text("\n".join(lines), encoding="utf-8")

    def load_file(self, filename):
        path = Path(filename)

        try:
            contents = path.read_text(encoding="utf-8")

        except FileNotFoundError:
            print("File not found.")

        else:
            lines = contents.splitlines()

            for line in lines:
                title, priority, completed = line.split(",")

                completed = completed == "True"

                task = Task(title, int(priority), completed)

                self.tasks.append(task)