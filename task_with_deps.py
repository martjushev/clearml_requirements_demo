import logging

from common import init_task
from clearml import Logger

log_format = "[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
logging.basicConfig(
    level=logging.INFO,
    format=log_format,
    datefmt="%Y-%m-%d %H:%M:%S",
)

task = init_task("task_with_deps")

task.execute_remotely("services")

Logger.current_logger().report_text("Hello from task_with_deps")
