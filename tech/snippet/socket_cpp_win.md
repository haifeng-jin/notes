# windows socket C++
#tech/snippet
Windows下Socket编程主要包括以下几部分：
服务端
1、初始化Windows Socket库。
2、创建Socket。
3、绑定Socket。
4、监听。
5、Accept。
6、接收、发送数据。

客户端
1、初始化Windows Socket库。
2、创建Socket。
3、连接Socket。
4、接收、发送数据。

服务端每接收到一个客户端的Socket,则创建一个线程。满足一个服务端连接多个客户端。

 
![](windows%20socket%20C++/copycode.gif)
 

```
1 //Server.cpp
  2 #include <iostream>
  3 #include <winsock2.h>
  4 
  5 using namespace std;
  6 
  7 #pragma comment(lib, "ws2_32.lib")
  8 
  9 #define PORT 4000
 10 #define IP_ADDRESS "10.241.39.19"
 11 
 12 
 13 DWORD WINAPI ClientThread(LPVOID lpParameter)
 14 {
 15     SOCKET CientSocket = (SOCKET)lpParameter;
 16     int Ret = 0;
 17     char RecvBuffer[MAX_PATH];
 18 
 19     while ( true )
 20     {
 21         memset(RecvBuffer, 0x00, sizeof(RecvBuffer));
 22         Ret = recv(CientSocket, RecvBuffer, MAX_PATH, 0);
 23         if ( Ret == 0 || Ret == SOCKET_ERROR ) 
 24         {
 25             cout<<"客户端退出!"<<endl;
 26             break;
 27         }
 28         cout<<"接收到客户信息为:"<<RecvBuffer<<endl;
 29     }
 30 
 31     return 0;
 32 }
 33 
 34 int main(int argc, char* argv[])
 35 {
 36     WSADATA  Ws;
 37     SOCKET ServerSocket, ClientSocket;
 38     struct sockaddr_in LocalAddr, ClientAddr;
 39     int Ret = 0;
 40     int AddrLen = 0;
 41     HANDLE hThread = NULL;
 42 
 43     //Init Windows Socket
 44     if ( WSAStartup(MAKEWORD(2,2), &Ws) != 0 )
 45     {
 46         cout<<"Init Windows Socket Failed::"<<GetLastError()<<endl;
 47         return -1;
 48     }
 49 
 50     //Create Socket
 51     ServerSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
 52     if ( ServerSocket == INVALID_SOCKET )
 53     {
 54         cout<<"Create Socket Failed::"<<GetLastError()<<endl;
 55         return -1;
 56     }
 57 
 58     LocalAddr.sin_family = AF_INET;
 59     LocalAddr.sin_addr.s_addr = inet_addr(IP_ADDRESS);
 60     LocalAddr.sin_port = htons(PORT);
 61     memset(LocalAddr.sin_zero, 0x00, 8);
 62 
 63     //Bind Socket
 64     Ret = bind(ServerSocket, (struct sockaddr*)&LocalAddr, sizeof(LocalAddr));
 65     if ( Ret != 0 )
 66     {
 67         cout<<"Bind Socket Failed::"<<GetLastError()<<endl;
 68         return -1;
 69     }
 70     //listen
 71     Ret = listen(ServerSocket, 10);
 72     if ( Ret != 0 )
 73     {
 74         cout<<"listen Socket Failed::"<<GetLastError()<<endl;
 75         return -1;
 76     }
 77 
 78     cout<<"服务端已经启动"<<endl;
 79 
 80     while ( true )
 81     {
 82         AddrLen = sizeof(ClientAddr);
 83         ClientSocket = accept(ServerSocket, (struct sockaddr*)&ClientAddr, &AddrLen);
 84         if ( ClientSocket == INVALID_SOCKET )
 85         {
 86             cout<<"Accept Failed::"<<GetLastError()<<endl;
 87             break;
 88         }
 89 
 90         cout<<"客户端连接::"<<inet_ntoa(ClientAddr.sin_addr)<<":"<<ClientAddr.sin_port<<endl;
 91 
 92         hThread = CreateThread(NULL, 0, ClientThread, (LPVOID)ClientSocket, 0, NULL);
 93         if ( hThread == NULL )
 94         {
 95             cout<<"Create Thread Failed!"<<endl;
 96             break;
 97         }
 98 
 99         CloseHandle(hThread);
100     }
101 
102     closesocket(ServerSocket);
103     closesocket(ClientSocket);
104     WSACleanup();
105 
106     return 0;
107 }
```

 
![](windows%20socket%20C++/copycode%202.gif)
 

 
![](windows%20socket%20C++/copycode%203.gif)
 

```
1 // Client.cpp
 2 #include <iostream>
 3 #include <winsock2.h>
 4 
 5 using namespace std;
 6 
 7 #pragma comment(lib, "ws2_32.lib")
 8 
 9 #define PORT 4000
10 #define IP_ADDRESS "10.241.39.19"
11 
12 int main(int argc, char * argv[])
13 {
14     WSADATA Ws;
15     SOCKET ClientSocket;
16     struct sockaddr_in ServerAddr;
17     int Ret = 0;
18     int AddrLen = 0;
19     HANDLE hThread = NULL;
20     char SendBuffer[MAX_PATH];
21 
22     //Init Windows Socket
23     if ( WSAStartup(MAKEWORD(2,2), &Ws) != 0 )
24     {
25         cout<<"Init Windows Socket Failed::"<<GetLastError()<<endl;
26         return -1;
27     }
28     //Create Socket
29     ClientSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
30     if ( ClientSocket == INVALID_SOCKET )
31     {
32         cout<<"Create Socket Failed::"<<GetLastError()<<endl;
33         return -1;
34     }
35 
36     ServerAddr.sin_family = AF_INET;
37     ServerAddr.sin_addr.s_addr = inet_addr(IP_ADDRESS);
38     ServerAddr.sin_port = htons(PORT);
39     memset(ServerAddr.sin_zero, 0x00, 8);
40 
41     Ret = connect(ClientSocket,(struct sockaddr*)&ServerAddr, sizeof(ServerAddr));
42     if ( Ret == SOCKET_ERROR )
43     {
44         cout<<"Connect Error::"<<GetLastError()<<endl;
45         return -1;
46     }
47     else
48     {
49         cout<<"连接成功!"<<endl;
50     }
51 
52     while ( true )
53     {
54         cin.getline(SendBuffer, sizeof(SendBuffer));
55         Ret = send(ClientSocket, SendBuffer, (int)strlen(SendBuffer), 0);
56         if ( Ret == SOCKET_ERROR )
57         {
58             cout<<"Send Info Error::"<<GetLastError()<<endl;
59             break;
60         }
61     }
62 
63     closesocket(ClientSocket);
64     WSACleanup();
65 
66     return 0;
67 }
```

 
![](windows%20socket%20C++/copycode%204.gif)
 

http://common.cnblogs.com/images/copycode.gif