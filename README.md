### Server
#### 透過socket套件來實作功能
- socket.gethostname(): 取得主機名稱
- socket.gethostbyname(): 取得主機IP
- sock = socket.socket(): #建立Socket
- sock.bind(): 綁定IP與Port
- sock.listen(): 監聽
- Connect,Address = sock.accept(): 當找到連接時,接受連接
- Connect.recv(): 接收數據
- Connect.close(): 關閉連線

#### 透過threading套件來實作功能
- threading.Thread(): 建立執行緒

### Client
#### 透過socket套件來實作功能
- Socket = socket.socket(): 建立Socket
- Socket.connect(): 連接Server
- Socket.send(): 傳送訊息
- Socket.recv(): 接收數據

#### 透過threading套件來實作功能
- threading.Thread(): 建立執行緒
