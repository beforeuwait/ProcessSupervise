# coding=utf-8


import json
import psutil
import platform
from loghandler import get_logger

logger = get_logger()
DEFAULT_ENCODING = 'utf-8'


class ProcessSupervise:
    """
    todo:
    1. 检索所有的python程序
    2. kill 指定的程序
    3. 监听本机状态
    """
    def __init__(self):
        self._process_list = None
        self.__node_status = None

    @property
    def all_process_list(self):
        process_list = []
        pids = psutil.pids()
        for pid in pids:
            process = psutil.Process(pid)
            try:
                if process.name() == 'python' or process.name() == 'python3':
                    cmd_line = process.cmdline()
                    process_list.append((pid, cmd_line))
            except Exception as e:
                logger.warning('检索进程列表时出错\t:{0}'.format(e))
        self._process_list = process_list
        return self._process_list

    @all_process_list.deleter
    def all_process_list(self):
        self._process_list = None

    @staticmethod
    def kill_process(pid):
        process = psutil.Process(pid)
        process.kill()
        return

    @staticmethod
    def process_status(pid):
        process = psutil.Process(pid)
        process_info = {
            'status': process.status(),
            'cpu_percent': process.cpu_percent(),
            'memeory_percent': process.memory_percent()
        }
        return json.dumps(process_info, ensure_ascii=False)

    @property
    def node_status(self):
        node_status = {
            'system': platform.uname().system,
            'cpu_percent': psutil.cpu_percent(),
            'memory_percent': psutil.virtual_memory().percent,
            'disk_usage': psutil.disk_usage('/').percent,
        }

        self.__node_status = node_status
        return json.dumps(self.__node_status, ensure_ascii=False)

    @node_status.deleter
    def node_status(self):
        self.__node_status = None
