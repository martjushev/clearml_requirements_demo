from clearml import Task


def init_task(task_name):
    return Task.init(
        project_name="PROJECT_NAME",
        task_name=task_name,
    )
