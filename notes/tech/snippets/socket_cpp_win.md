# windows socket C++
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

 
 

```cpp
//Server.cpp
#include <iostream>
#include <winsock2.h>

using namespace std;

#pragma comment(lib, "ws2_32.lib")

#define PORT 4000
#define IP_ADDRESS "10.241.39.19"


DWORD WINAPI ClientThread(LPVOID lpParameter)
{
    SOCKET CientSocket = (SOCKET)lpParameter;
    int Ret = 0;
    char RecvBuffer[MAX_PATH];

    while ( true )
    {
        memset(RecvBuffer, 0x00, sizeof(RecvBuffer));
        Ret = recv(CientSocket, RecvBuffer, MAX_PATH, 0);
        if ( Ret == 0 || Ret == SOCKET_ERROR ) 
        {
            cout<<"客户端退出!"<<endl;
            break;
        }
        cout<<"接收到客户信息为:"<<RecvBuffer<<endl;
    }

    return 0;
}

int main(int argc, char* argv[])
{
    WSADATA  Ws;
    SOCKET ServerSocket, ClientSocket;
    struct sockaddr_in LocalAddr, ClientAddr;
    int Ret = 0;
    int AddrLen = 0;
    HANDLE hThread = NULL;

    //Init Windows Socket
    if ( WSAStartup(MAKEWORD(2,2), &Ws) != 0 )
    {
        cout<<"Init Windows Socket Failed::"<<GetLastError()<<endl;
        return -1;
    }

    //Create Socket
    ServerSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if ( ServerSocket == INVALID_SOCKET )
    {
        cout<<"Create Socket Failed::"<<GetLastError()<<endl;
        return -1;
    }

    LocalAddr.sin_family = AF_INET;
    LocalAddr.sin_addr.s_addr = inet_addr(IP_ADDRESS);
    LocalAddr.sin_port = htons(PORT);
    memset(LocalAddr.sin_zero, 0x00, 8);

    //Bind Socket
    Ret = bind(ServerSocket, (struct sockaddr*)&LocalAddr, sizeof(LocalAddr));
    if ( Ret != 0 )
    {
        cout<<"Bind Socket Failed::"<<GetLastError()<<endl;
        return -1;
    }
    //listen
    Ret = listen(ServerSocket, 10);
    if ( Ret != 0 )
    {
        cout<<"listen Socket Failed::"<<GetLastError()<<endl;
        return -1;
    }

    cout<<"服务端已经启动"<<endl;

    while ( true )
    {
        AddrLen = sizeof(ClientAddr);
        ClientSocket = accept(ServerSocket, (struct sockaddr*)&ClientAddr, &AddrLen);
        if ( ClientSocket == INVALID_SOCKET )
        {
            cout<<"Accept Failed::"<<GetLastError()<<endl;
            break;
        }

        cout<<"客户端连接::"<<inet_ntoa(ClientAddr.sin_addr)<<":"<<ClientAddr.sin_port<<endl;

        hThread = CreateThread(NULL, 0, ClientThread, (LPVOID)ClientSocket, 0, NULL);
        if ( hThread == NULL )
        {
            cout<<"Create Thread Failed!"<<endl;
            break;
        }

        CloseHandle(hThread);
    }

    closesocket(ServerSocket);
    closesocket(ClientSocket);
    WSACleanup();

    return 0;
}
```


```cpp
// Client.cpp
#include <iostream>
#include <winsock2.h>

using namespace std;

#pragma comment(lib, "ws2_32.lib")

#define PORT 4000
#define IP_ADDRESS "10.241.39.19"

int main(int argc, char * argv[])
{
    WSADATA Ws;
    SOCKET ClientSocket;
    struct sockaddr_in ServerAddr;
    int Ret = 0;
    int AddrLen = 0;
    HANDLE hThread = NULL;
    char SendBuffer[MAX_PATH];

    //Init Windows Socket
    if ( WSAStartup(MAKEWORD(2,2), &Ws) != 0 )
    {
        cout<<"Init Windows Socket Failed::"<<GetLastError()<<endl;
        return -1;
    }
    //Create Socket
    ClientSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if ( ClientSocket == INVALID_SOCKET )
    {
        cout<<"Create Socket Failed::"<<GetLastError()<<endl;
        return -1;
    }

    ServerAddr.sin_family = AF_INET;
    ServerAddr.sin_addr.s_addr = inet_addr(IP_ADDRESS);
    ServerAddr.sin_port = htons(PORT);
    memset(ServerAddr.sin_zero, 0x00, 8);

    Ret = connect(ClientSocket,(struct sockaddr*)&ServerAddr, sizeof(ServerAddr));
    if ( Ret == SOCKET_ERROR )
    {
        cout<<"Connect Error::"<<GetLastError()<<endl;
        return -1;
    }
    else
    {
        cout<<"连接成功!"<<endl;
    }

    while ( true )
    {
        cin.getline(SendBuffer, sizeof(SendBuffer));
        Ret = send(ClientSocket, SendBuffer, (int)strlen(SendBuffer), 0);
        if ( Ret == SOCKET_ERROR )
        {
            cout<<"Send Info Error::"<<GetLastError()<<endl;
            break;
        }
    }

    closesocket(ClientSocket);
    WSACleanup();

    return 0;
}
```
