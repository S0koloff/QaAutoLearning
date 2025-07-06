import logging
import os

def setup_logger():
    logging.basicConfig(
        filename='lesstwo/logs/test_log.log',
        level=logging.INFO,
        format ='%(asctime)s [%(levelname)s] %(message)s',
        filemode='w'
    )
    return logging.getLogger("qa_logger")


logger = setup_logger()