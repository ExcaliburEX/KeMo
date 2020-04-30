import socket
import time
import threading
import os
import sys




def ReceiveFile(conn):
    while True:  # 连接成功后一直使用当前连接，直到退出
        with open("recv.py", "ab") as f:
            data = conn.recv(1024)
            if data == b'quit':
                break
            if data != b'success':
                f.write(data)
            conn.send("success".encode())
    print("文件barrier.py已经接收！存储为recv.py")
    f.close()


def SendAnswer(conn):
    while True:
        if os.path.exists("recv.py"):
            ans = os.popen("python recv.py")
            ansRead = ans.read()
            print("recv.py运行完毕，得到结果为%s" % (str(ansRead)))
            with open('output.txt', "w") as f:
                f.write(ansRead)
                f.close()
            print("将得到的结果写入output.txt")
            with open('output.txt', 'rb') as f:
                for i in f:
                    conn.send(i)
                    data = conn.recv(1024)
                    if data != b'success':
                        break
                conn.send('quit'.encode())
            print("将output.txt发送完毕！")
            break
    conn.close()


def SendPyFile(conn):
    with open('barrier.py', 'rb') as f:
        for i in f:
            conn.send(i)
            data = conn.recv(1024)
            if data != b'success':
                break
    print("文件barrier.py已经发送！")
    conn.send('quit'.encode())


def ReceiveAnswer(conn):
    while True:
        with open("recv_output.txt", "ab") as f:
            data = conn.recv(1024)
            if data == b'quit':
                break
            if data != b'success':
                f.write(data)
            conn.send("success".encode())
    print("结果接收完毕，存储在recv_output.txt！")
    f.close()
    conn.send('quit'.encode())


def process(conn):
    print("等待5秒返回GOON！")
    for i in range(5):
        print(i+1)
        time.sleep(1)
    conn.send('GOON'.encode())


def ClientBarrier(conn):
    while True:
        conn, addr = conn.accept()
        print("barrier函数阻塞，连接建立，地址为%s"%(str(addr)))
        t = threading.Thread(target=process, args=(conn,))
        t.start()
        break

# 改写线程类
class msgThread(threading.Thread):
    def __init__(self, conn, flag):
        threading.Thread.__init__(self)
        self.conn = conn
        self.flag = flag

    def run(self):
        if self.flag == "send_file":
            SendPyFile(self.conn)
        elif self.flag == "receive_answer":
            ReceiveAnswer(self.conn)
        elif self.flag == "receive_file":
            ReceiveFile(self.conn)
        else:
            SendAnswer(self.conn)


def Client(address):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            client.connect((address, 6999))  # 建立一个链接，连接到本地的6999端口
            break
        except:
            print("等待侦听！")
            time.sleep(1)
    Thread_receive = msgThread(client, "receive_file")
    Thread_send = msgThread(client, "send_answer")
    Thread_receive.start()
    Thread_send.start()

def Server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 6999))  # 绑定要监听的端口
    server.listen(5)  # 开始监听 表示可以使用五个链接排队
    conn, addr = server.accept()  # 等待链接,多个链接的时候就会出现问题,其实返回了两个值
    print("侦听器已启动！port：6999")
    print("连接建立，地址在%s"%(str(addr)))
    Thread_receive = msgThread(conn, "send_file")
    Thread_send = msgThread(conn, "receive_answer")
    Thread_barrier = threading.Thread(target=ClientBarrier, args=(server,))
    Thread_receive.start()
    Thread_send.start()
    Thread_barrier.start()


if __name__ == "__main__":
    BootMode = input("请选择启动方式(1(控制节点)或2(计算节点))：\n")
    if BootMode == '1':
        Server()
    else:
        port = input("请输入侦听服务器地址(默认127.0.0.1)：\n")
        Client(port)
