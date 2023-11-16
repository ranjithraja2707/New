import logging


logging.basicConfig(level=logging.INFO)

# Example usage of different logging levels
logging.debug("This is a debug message")    # Will not be displayed
logging.info("This is an info message")      # Will be displayed
logging.warning("This is a warning message")  # Will be displayed
logging.error("This is an error message")     # Will be displayed
logging.critical("This is a critical message")# Will be displayed
