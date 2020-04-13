class Email:
    '''log发送提醒email设置'''
    username = '' #发送邮箱地址
    password = '' #发送邮箱密码
    target_email_addr = '' #目标邮件地址

class Database:
    '''数据库设置'''
    database_host = '192.168.1.146'
    # redisport = 33003
    mongoport = 33002
    # mysqlport = 33001
    # dbusername = 'root'

class Log:
    '''设置封装类的参数'''
    severip = '127.0.0.1'   #logserver端ip
    socket_handler_port = 30002  #server端port
    baseLogLevel = 'debug'
    sockhandlerLevel = 'warning'
    StreamHandlerlevel = 'info'
    filehandlerlevel = 'warning'
    # fmt = '%(asctime)s - %(name)s%(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    fmt = '%(asctime)s - 线程id：%(thread)d 进程id：%(process)s %(name)s %(pathname)s [line:%(lineno)d] - %(levelname)s: %(message)s'


'''用于写入数据库命名'''
project = 'test'