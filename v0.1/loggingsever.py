import socket
import pickle
import struct
import pymongo
import setting
from setting import Database
from sendEmail import sender


class GetMongodb:
    def __init__(self):
        # 初始化mongodb
        con = pymongo.MongoClient(host=Database.database_host, port=Database.mongoport)
        db = con[setting.project]
        self.collDict = {
            'DEBUG': db['DEBUG'],
            'INFO': db['INFO'],
            'WARNING': db['WARNING'],
            'ERROR': db['ERROR'],
            'CRITICAL': db['CRITICAL']
        }

    def formatLog(self, rawlog):
        # 预处理log数据为列表
        keylist = ['name', 'msg', 'pathname', 'module', 'lineno', 'funcName', 'created', 'threadName',
                   'processName']  # 存入mongodb数据key的list也代表log的字段名
        return [rawlog.get(i) for i in rawlog if i in keylist]

    def writeLog(self, logInfoList, level):
        # log写入mongodb
        self.collDict[level].insert_one({'log': logInfoList})
        print('写入mongodb')


# tcp
def recvlog():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 30002))  # 绑定本机8000端口
    s.listen(8)
    print('waiting for connections...')
    getMongodb = GetMongodb()
    while 1:
        # 无限循环等待接收客户端连接
        sock, addr = s.accept()
        while 1:
            chunk = sock.recv(4)  # 发送端会添加4个字节的长度
            if len(chunk) < 4:
                break
            slen = struct.unpack('>L', chunk)[0]  # 将长度解包, 网络传输统一是大端, L代表无符号长整数
            chunk = sock.recv(slen)  # 接收数据
            logDict = pickle.loads(chunk)  # 反序列化, 系统默认发送的是序列化后的字节流
            logLevel = logDict['levelname']
            logInfoList = getMongodb.formatLog(logDict)
            print('接收到的数据：{}: {}'.format(logLevel, logInfoList))
            getMongodb.writeLog(logInfoList, logLevel)  # log写入mongodb
            if logLevel in ['WARNING', 'ERROR', 'CRITICAL']:
                sender(str(logInfoList))
        sock.close()


if __name__ == '__main__':
    recvlog()
