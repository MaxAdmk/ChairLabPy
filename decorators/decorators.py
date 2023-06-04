"""
This module is needed for lab №10
"""
import logging


def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                logger = logging.getLogger(__name__)
                logger.setLevel(logging.INFO)
                formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

                if mode == "concole":
                    console_handler = logging.StreamHandler()
                    console_handler.setFormatter(formatter)
                    logger.addHandler(console_handler)
                    logger.error(str(e))
                elif mode == "file":
                    file_handler = logging.FileHandler('error.log')
                    file_handler.setFormatter(formatter)
                    logger.addHandler(file_handler)
                    logger.error(str(e))
                else:
                    raise ValueError("Invalid logging mode")
        return wrapper
    return decorator
