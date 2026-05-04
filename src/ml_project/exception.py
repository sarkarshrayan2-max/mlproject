import sys
from src.ml_project.logger import logging


class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message = self.error_message_detail(error_message, error_detail)
        logging.error(self.error_message)

    def error_message_detail(self, error_message, error_detail):
        _, _, exc_tb = error_detail.exc_info()

        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

        message = (
            f"Error occurred in script: [{file_name}] "
            f"at line number: [{line_number}] "
            f"with error message: [{str(error_message)}]"
        )

        return message

    def __str__(self):
        return self.error_message