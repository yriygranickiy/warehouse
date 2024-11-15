import sys

from loguru import logger

logger.remove()
logger.add(sys.stderr, format="{time}\n {level}\n {message}\n", level="INFO" )
logger.add('logs/file_{time}.log',rotation='10 MB', retention='10 days',level='INFO', format='{time}\n {level}\n {message}\n')

