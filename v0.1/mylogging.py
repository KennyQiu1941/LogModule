from logging import handlers
import logging
from setting import Log
'''
封装三种handler
打印，文件，socket：接收后server端写入数据库
mylogging调用方式
默认实例化参数只要填写name 后面默认是使用数据库和打印handler
    from mylogging import Logging
    import os

    l = Logging(name=os.path.basename(__file__)[:-3], filehandler=True, sockethandler=False)
    l.logger.warning('ceshi')
'''


class Logging:
    def __init__(self, name, filehandler=False, sockethandler=True):
        level_relations = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'error': logging.ERROR,
            'crit': logging.CRITICAL
        }  # 日志级别关系映射
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level_relations[Log.baseLogLevel])
        format_log = logging.Formatter(Log.fmt)
        sh = logging.StreamHandler()
        sh.setFormatter(format_log)
        sh.setLevel(level_relations[Log.StreamHandlerlevel])
        self.logger.addHandler(sh)
        if sockethandler:
            sockhandler = handlers.SocketHandler(Log.severip, Log.socket_handler_port)
            sockhandler.setLevel(level_relations[Log.sockhandlerLevel])
            sockhandler.setFormatter(format_log)
            self.logger.addHandler(sockhandler)
        if filehandler:
            filename = '{}.log'.format(name)
            th = handlers.TimedRotatingFileHandler(filename=filename, when='D', backupCount=30, interval=1,
                                                   encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
            # 实例化TimedRotatingFileHandler
            # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
            # S 秒
            # M 分
            # H 小时、
            # D 天、
            # W 每星期（interval==0时代表星期一）
            # midnight 每天凌晨
            th.setLevel(level_relations[Log.filehandlerlevel])
            th.setFormatter(format_log)
            self.logger.addHandler(th)


