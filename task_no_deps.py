import logging

from clearml import Task, Logger

log_format = "[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
logging.basicConfig(
    level=logging.INFO,
    format=log_format,
    datefmt="%Y-%m-%d %H:%M:%S",
)


task = Task.init(
    project_name="PROJECT_NAME",
    task_name="task_no_deps",
)

task.execute_remotely("services")

Logger.current_logger().report_text("Hello from task_no_deps")
