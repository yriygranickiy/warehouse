
import logging
from logging.handlers import RotatingFileHandler

__path_to_file__ = "logs/warehouse.log"

logger = logging.getLogger("warehouse.app")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(__path_to_file__)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

handler = RotatingFileHandler(
    __path_to_file__,  # name file
    maxBytes=5 * 1024,  # max size file (1 MB)
    backupCount=2
)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s\n")
handler.setFormatter(formatter)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)


logger.addHandler(console_handler)
logger.addHandler(file_handler)

