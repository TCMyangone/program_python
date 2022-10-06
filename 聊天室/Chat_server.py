import socket
import threading
import json
import os
import datetime

class ChatSever:
    
    def __init__(self):
        self.ADDR = ('127.0.0.1', 1225)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.ADDR))
        self.s.listen()
        self.client = {}
        self.user_ip = {}
        self.users = []
        self.lock = threading.Lock()
        self.file_name = ''
        self.time = datetime.datetime.today()
        self.examin_filename()
        self.run()
        


    def run(self):
        print('正在等待用户连接.......')
        while True:
            c, addr = self.s.accept()
            print(str(addr)+'已连接')
            self.client[c] = addr
            threading.Thread(target=self.client_management, args=(c, addr)).start()

    def examin_filename(self):
        for i in range(1, 10000000000000000):
            if os.path.exists('聊天室\\log\\log_%s.txt'%i):
                pass
            else:
                self.file_name = '聊天室\\log\\log_%s.txt'%i
                break
        with open(self.file_name, 'w', encoding='utf-8') as fil:
            fil.write('本次服务器开启于:%s\n'%self.time)
        

    def client_management(self, c, addr):

        user_name = c.recv(1024).decode('utf-8')
        self.user_ip[user_name] = c.getpeername()
        with open('聊天室\\sql.json', 'w') as f_obj:
                json.dump(self.user_ip, f_obj, indent=2)
        self.users.append(str(user_name))
        welcome = '-------------------欢迎%s加入聊天室-------------------\n当前在线人数:%s\n'%(str(user_name), len(self.users))
        self.send_msg(welcome, model=2)

        while True:
            try:
                new_msg = c.recv(1024).decode('utf-8')

                self.send_msg(new_msg, name=user_name)

            except:
                c.close()
                del self.client[c]
                self.users.remove(str(user_name))
                exit_msg = str(user_name) + '已离开,当前在线人数:%s'%(len(self.users))
                print(str(addr) + '已断开连接')
                self.send_msg(exit_msg, model=2)
                break


    def send_msg(self, msg, name='', model=1):
        if model == 1:
            for i in self.client.keys():
                i.send(('%s:%s\n'%(name, msg)).encode('utf-8'))
            with open(self.file_name, 'a', encoding='utf-8') as fil:
                fil.write('%s:%s\n'%(name, msg))

        elif model == 2:
            for i in self.client.keys():
                i.send(msg.encode('utf-8'))
            with open(self.file_name, 'a', encoding='utf-8') as fil:
                fil.write(msg)

                    
                
server = ChatSever()

