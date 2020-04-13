#分布式日志模块
通过对logging库的封装实现写入数据库目前只支持mongodb
###使用说明
1. setting.py 是设置logmode所有参数（包括发送邮件地址，数据库ip，log等级)
2. 使用时设置好ip地址，邮箱地址密码，日志等级
3. 导入方式
 ```python
from mylogging import Logging
import os    #可以不导入为了方便logger实例化

# 默认不启动本地文件日志记录启动服务器记录日志 修改话只需要设置filehandler, sockethandler
log = Logging(name = os.path.basename(__file__)[:-3], filehandler=True, sockethandler=False) #启动本地文件关闭数据库记录日志
log.logger.warning('发生错误')
log.logger.debug('xxx变量=xxx')
log.logger.info('xxxxxxxx')
```

