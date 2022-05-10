from clearml import Logger

from common import init_task

task = init_task("task_with_deps")

task.execute_remotely("services")

Logger.current_logger().report_text("Hello from task_with_deps")
