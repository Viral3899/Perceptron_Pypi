import os
import logging
from datetime import datetime


def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


LOG_DIR = 'logs'


def get_log_file_name():
    return f"log_{get_current_time_stamp()}.log"


LOG_FILE_NAME = get_log_file_name()

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)


# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter("[%(asctime)s] || %(pathname)s || %(module)s || %(filename)s || %(lineno)d || %(name)s || %(funcName)s() || %(levelname)s -->> %(message)s")

# Create file handler
file_handler = logging.FileHandler(LOG_FILE_PATH, mode='w')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# Create stream handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)