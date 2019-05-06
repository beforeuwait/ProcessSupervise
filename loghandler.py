# coding=utf-8

import os
import logging


def get_logger():
    logger = logging.getLogger(name='logger')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(os.path.join(os.path.split(__file__)[0], './ps_log.log'))
    fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(fmt)
    logger.addHandler(handler)
    return logger
