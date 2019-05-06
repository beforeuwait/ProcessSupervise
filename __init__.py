# coding=utf-8

__author__ = 'wangjiawei'
__version__ = '1.0'
__date__ = '2018-11-15'


"""
由节点的TaskExecutor和NodeState来调用

该Executor执行的任务包括:
    1. 根据task_index.ini 启动进程
    2. 根据反馈去kill 相应的进程

NodeState需要执行的:
    1. 根据 task_index.ini 来检索每个进程的状态
    2. 当前节点的状态
========================分割线==============================
2019-05-06: 
我对ps的理解为,在调度下，作为监控的角色
负责:
1. 监听状态
2. kill进程

"""
from .process_supervise import ProcessSupervise as PS

__all__ = ['PS']
