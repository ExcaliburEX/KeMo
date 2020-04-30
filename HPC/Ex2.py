import socket  # 客户端 发送一个数据，再接收一个数据
import time
import threading
import ctypes
import inspect
quit = 0


# 终止线程
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


def ReceiveMsg(conn):
    global quit
    while True:
        try:
            data = conn.recv(1024)
        except:
            print("连接结束")
            conn.close()
            break
        if str(data.decode()).upper() != 'QUIT':
            print('recive:', data.decode())
        else:
            quit = 1
            conn.close()
            break


def SendMsg(conn):
    global quit
    while True:
        send = input("send:\n")
        try:
            conn.send(send.encode('utf-8'))
        except:
            print("连接结束")
            conn.close()
            break
        if str(send).upper() == 'QUIT':
            conn.close()
            break

# 改写线程
class msgThread(threading.Thread):
    def __init__(self, conn, flag):
        threading.Thread.__init__(self)
        self.conn = conn
        self.flag = flag

    def run(self):
        if self.flag == 1:
            ReceiveMsg(self.conn)
        else:
            SendMsg(self.conn)

# 声明socket类型，同时生成链接对象
def Client(address):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            client.connect((address, 6999))  # 建立一个链接，连接到本地的6999端口
            break
        except:
            print("等待侦听！")
            time.sleep(1)
    Thread_receive = msgThread(client, 1)
    Thread_send = msgThread(client, 2)
    Thread_receive.start()
    Thread_send.start()

def Server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 6999))  # 绑定要监听的端口
    server.listen(5)  # 开始监听 表示可以使用五个链接排队
    conn, addr = server.accept()  # 等待链接,多个链接的时候就会出现问题,其实返回了两个值
    print("侦听器已启动！port：6999")
    print(conn, addr)
    Thread_receive = msgThread(conn, 1)
    Thread_send = msgThread(conn, 2)
    Thread_receive.start()
    Thread_send.start()


if __name__ == "__main__":
    BootMode = input("请选择启动方式(1或2)：\n")
    if BootMode == '1':
        Server()
    else:
        port = input("请输入侦听服务器地址(默认127.0.0.1)：\n")
        Client(port)
