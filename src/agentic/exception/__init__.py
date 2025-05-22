



import sys

def error_message_detail(error: Exception):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    if exc_tb is not None:
        while exc_tb.tb_next:
            exc_tb = exc_tb.tb_next
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "Unknown file"
        line_number = "Unknown line"
    return f"Error occurred in script: [{file_name}] at line [{line_number}] error message: [{str(error)}]"

class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(str(error_message))
        self.error_message = error_message_detail(error_message)
    
    def __str__(self):
        return self.error_message