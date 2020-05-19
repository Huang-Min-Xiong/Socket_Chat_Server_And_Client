import socket 
import threading 

class ClientNode:
    def __init__(self):
        IP_and_Port = ('127.0.0.1', 12345) #設置IP與Port
        self.Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #創建Socket
        self.Socket.connect(IP_and_Port) #連接IP與Port
        print('已連接伺服端!\n')
        print('~聊天室~')


    #傳送訊息
    def send_Message(self, Message):
        self.Socket.send(Message.encode()) #傳送數據,並將訊息加碼  
        

    #取得訊息
    def receive_Message(self):
        while True:
            data = self.Socket.recv(1024).decode() #接收數據,並解碼
            print('Server說:\n'+data)
            print('請輸入訊息:')   
                

    #主程式
    def main(self):    
        while True:      
            message = input('請輸入訊息:\n')
            self.send_Message(message)
            

if __name__ == "__main__":
    #創建客戶端實例
    print('客戶端已開啟!')
    print('連接中......')
    Client = ClientNode()
    Always_Receive = threading.Thread(target=Client.receive_Message)
    Always_Receive.daemon = True
    Always_Receive.start()
    Client.main()
