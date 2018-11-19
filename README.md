# ProcessSupervise

vsersion = 1.0

该库是基于 psutil 库封装的进程管理工具

被节点调用提供以下功能:

- 启动进程

- kill进程

- 检索全部进程

- 检查全部进程状态

- 当前节点状态


## 如何使用

导入并实例化类

		from process_supervise import ProcessSupervise
		
		ps = ProcessSupervise()

- 启动进程
		
进程的启动目录文件 task_index.ini

		demo	demo_persistence.py	C:\Users\forme\Desktop\Github\spider_platform\Node\demo
		demo	demo_parser.py	C:\Users\forme\Desktop\Github\spider_platform\Node\demo
		demo	demo_downloader.py	C:\Users\forme\Desktop\Github\spider_platform\Node\demo
		demo	demo_seed.py	C:\Users\forme\Desktop\Github\spider_platform\Node\demo

启动进程
	
	task_ctx = open(task_index.ini, 'r', encoding='utf8').read()
	ps.start_process(task_ctx)

- kill进程

传入一个执行文件列表

		kill_process_list = ('demo_persistence.py', 'demo_parser.py', 'demo_downloader.py', 'demo_seed.py')

启动进程
	
		ps.kill_process(kill_process_list)


- 检索所有Python进程的状态

		all_process_state = ps.check_all_process_state()
	
		# 返回列表
		all_process_state = [
			proc_state = {
                'pid': 'xxx',             # 该进程的pid
                'filename': 'xxx',        # 该进程执行文件
                'servival': 'xxxx',       # 状态
                'cpu_percent': 'xxxxx',   # cpu占用率
                'belong': 'xxxxx',           # 隶属于
                'memeory_percent': 'xxxxxx',  # 内存占用率
            },
			{...}, {....}
		]

- 返回当前节点状态:

		node_state = ps.check_node_state()
		# 返回字典
		{
            'cpu_percent': 'xxx',       # cpu使用率
            'memory_percent': ''xxxx,   # 内存使用率
            'disk_usage': 'xxx',        # 硬盘使用率
        } 

