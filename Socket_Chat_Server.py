import socket
import threading 

# Host_Name=socket.gethostname() #取得主機名稱
# Host_IP=socket.gethostbyname('www.google.com') #取得主機IP

class ServerNode:
    def __init__(self):
        IP_and_Port = ('127.0.0.1', 12345) #設置IP與Port
        self.Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #創建Socket
        self.Socket.bind(IP_and_Port) #綁定IP與Port
        self.Socket.listen(5) #監聽   
        self.Connect,Address = self.Socket.accept() #當找到連接時接受連接
        print('客戶端已連接!\n')
        print('~聊天室~')


    #傳送訊息
    def Send_Message(self, Message):
        self.Connect.send(Message.encode()) #傳送數據,並將訊息加碼

        
    #取得訊息
    def Receive_Message(self):
        while True:
            data = self.Connect.recv(1024).decode() #接收數據,並解碼
            print('Client說:\n'+data)
            print('請輸入訊息:')
        

    #主程式
    def main(self): 
        while True:
            message = input('請輸入訊息:\n')
            self.Send_Message(message) 

            
if __name__ == "__main__":
    #創建伺服端實例
    print('伺服端已開啟!')
    print('監聽中......')
    server = ServerNode()
    Always_Receive = threading.Thread(target=server.Receive_Message)
    Always_Receive.daemon = True
    Always_Receive.start()
    server.main()


