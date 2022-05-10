from clearml import Task, Logger

task = Task.init(
    project_name="PROJECT_NAME",
    task_name="task_no_deps",
)

task.execute_remotely("services")

Logger.current_logger().report_text("Hello from task_no_deps")
