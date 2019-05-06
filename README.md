# ProcessSupervise

vsersion = 1.0

该库是基于 psutil 库封装的进程管理工具

被节点调用提供以下功能:

[x] 启动进程

- kill进程

- 检索全部进程

- 检查全部进程状态

- 当前节点状态


## 如何使用

导入并实例化类

		from process_supervise import ProcessSupervise
		
		ps = ProcessSupervise()

- 启动进程

- kill进程

- 返回当前节点状态:

		node_state = ps.check_node_state()
		# 返回字典
		{
		    'system': 'xxxxx'             # 操作系统
            'cpu_percent': 'xxx',       # cpu使用率
            'memory_percent': ''xxxx,   # 内存使用率
            'disk_usage': 'xxx',        # 硬盘使用率
        } 

