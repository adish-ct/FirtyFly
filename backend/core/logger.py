import logging
from logging.handlers import RotatingFileHandler

# Create a logger
logger = logging.getLogger("my_app_logger")
logger.setLevel(logging.INFO)  # can be DEBUG for development

# Console handler
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
console_handler.setFormatter(console_formatter)

# Optional: file handler with rotation
file_handler = RotatingFileHandler(
    "app.log", maxBytes=10*1024*1024, backupCount=5
)
file_handler.setFormatter(console_formatter)

# Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)