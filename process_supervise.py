# coding=utf-8


import os
import sys
import psutil
import logging
import platform

DEFAULT_ENCODING = 'utf-8'

# logging

logger = logging.getLogger('__main__')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(os.path.abspath('./ps_log.log'))
fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(fmt)
logger.addHandler(handler)

# TypeCode
_AllProcess = list
_AProcessCmdline = list
_NodeState = dict
_TaskList = list


class ProcessSupervise:
    """进程管理工具

    提供以下服务:

    - 启动进程
    - kill进程
    - 检索全部进程
    - 检查指定进程状态
    - 当前节点状态

    """
    def __init__(self, task_list: list = None, task_ctx: str = None) -> None:
        self._task_list = task_list
        self._task_ctx = task_ctx
        self._process_list = None
        self.parse_task_list = None

    @property
    def parse_task_list(self) -> _TaskList:
        # 接收到进程列表
        # 返回加工过后的task_list
        task_list = []
        # 开始处理
        if self._task_ctx is not None:
            for task in self._task_ctx.split('\n'):
                if task != '':
                    task_list.append(task.split('\t'))
            self._task_list = task_list
        return self._task_list

    @parse_task_list.setter
    def parse_task_list(self, task_ctx) -> None:
        """文本形式的task_ctx"""
        if isinstance(self._task_ctx, str):
            self._task_ctx = task_ctx
        else:
            # 抛出错误
            # raise xxxError
            self._task_ctx = ''

    @parse_task_list.deleter
    def parse_task_list(self) -> None:
        """腾内存"""
        self._task_ctx = None
        self._task_list = None

    def start_process(self, task_ctx) -> None:
        """给一个元组，启动进程

        :param task_ctx:元组,任务列表文档
        :return: None
        """
        # 将任务文本变成
        self.parse_task_list = task_ctx

        # 开始执行任务
        # 先确定操作系统,不同的操作系统，文件目录的表示不同
        system = platform.uname().system

        # 拿到当前的进程列表
        process_list = self.all_process_list
        # task_list中每一个元素: [task_name, task_xxx.py, path]
        for task in self.parse_task_list:
            if system == 'Windows':
                # 就windows奇葩一些
                execute_path = '\\'.join([task[-1], task[-2]])
            else:
                execute_path = os.path.join(task[-1], task[-2])
            cmd = 'nohup python3 {0} &'.format(execute_path)
            # cmd代表向shell里输入的执行语句
            # nohup python3 C:\Users\forme\Desktop\Github\spider_platform\Node\demo\demo_persistence.py &
            # nohup python3 C:\Users\forme\Desktop\Github\spider_platform\Node\demo\demo_parser.py &
            # nohup python3 C:\Users\forme\Desktop\Github\spider_platform\Node\demo\demo_downloader.py &
            # nohup python3 C:\Users\forme\Desktop\Github\spider_platform\Node\demo\demo_seed.py &

            # 开始检索每个任务，是否已经存在
            if execute_path not in process_list:
                # 执行该task
                try:
                    os.system(cmd)
                except Exception as e:
                    logger.warning('进程启动失败\t{0}\n启动命令:\t{1}'.format(e, cmd))

        # 腾内存
        del self.parse_task_list
        del self.all_process_list

    def kill_process(self, *args) -> None:
        """kill掉指定的进程
        需要根据给的任务列表，去检索出该程序的pid
        :param args: 元组，进程列表,需要提供,((xxx.py, ptah), (xxx.py, path))
        :return:
        """
        pass

    def search_all_process(self) -> _AllProcess:
        """返回当前节点所有进程的pids

        :return: 列表
        """
        pass

    def get_pid_cmdline(self) -> _AProcessCmdline:
        """获取当前的进程cmdline信息
        大概获取
        :return:
        """
        pass

    @property
    def all_process_list(self) -> _AllProcess:
        """获取当前节点，全部的进程及执行路径

        """
        process_list = []
        for i in psutil.pids():
            process = psutil.Process(i)
            try:
                # 只看python 的进程
                if process.name() == 'Python':
                    cmdline = process.cmdline()
                    # 判断cmdline的长度, 第一个参数是python 第二个是任务路径
                    if cmdline.__len__() > 1:
                        process_list.append(cmdline[1])
            except Exception as e:
                print('error', e)

        self._process_list = process_list
        return self._process_list

    @all_process_list.deleter
    def all_process_list(self) -> None:
        """腾内存"""
        self._process_list = None

    def check_process_state(self, execute_path) -> None:
        """返回当前节点该进程的状态
        通过检测各个进程的执行路径，来确定该进程
        是否存活
        :return:
        """
        pass

    def check_node_state(self) -> _NodeState:
        """返回当前节点的状态
        cpu占用率
        memory占用率
        disk占用率
        :return: 一个字典
        """
        pass


if __name__ == '__main__':
    ps = ProcessSupervise()
    index = open('./task_index.ini', 'r', encoding='utf8').read()
    ps.start_process(index)
