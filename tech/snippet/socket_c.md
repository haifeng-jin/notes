# Linux C Socket
#tech/snippet
部分转自：http://goodcandle.cnblogs.com/archive/2005/12/10/294652.aspx

1. 什么是TCP/IP、UDP？

2. Socket在哪里呢？

3. Socket是什么呢？

4. 有很多的框架，为什么还在从Socket开始？

5. Linux C Socket简单示例
**1.什么是TCP/IP** **、UDP** **？**

TCP_IP（Transmission Control Protocol_Internet Protocol）即传输控制协议/网间协议，是一个工业标准的协议集，它是为广域网（WANs）设计的。
UDP（User Data Protocol，用户数据报协议）是与TCP相对应的协议。它是属于TCP/IP协议族中的一种。
下面的图表明了这些协议的关系。

![](Linux%20C%20Socket/27111530-6d4641d32e944b98b698e167f72a263f.png)
**2.Socket** **在哪里呢？**

 
![](Linux%20C%20Socket/27111710-a88a3bab25064f0480b41f22b50d6f76.png)
 

3.Socket* **是什么呢？***

Socket是应用层与TCP_IP协议族通信的中间软件抽象层，它是一组接口。在设计模式中，Socket其实就是一个门面模式，它把复杂的TCP_IP协议族隐藏在Socket接口后面，对用户来说，一组简单的接口就是全部，让Socket去组织数据，以符合指定的协议。

门面模式，用自己的话说，就是系统对外界提供单一的接口，外部不需要了解内部的实现。

**4.有很多的框架，为什么还在从Socket开始？**

现在的跨平台网络编程框架很多，如Java的SSH，C/C++的Boost等。

现在的分布式框架很多，如Hadoop等。

我的任务是把一个C/C++程序做成分布式，要求的不配环境，基本属于纯计算的，结果很小。所以选择了Socket。

重要的是Socket是分布式、云计算、网络编程的基础，对Socket的学习有利于对其他框架的理解。

下图是Socket编程的基本流程：

![](Linux%20C%20Socket/27113109-ad8f7a2ce6d64ae39706ef7db3aa07cd.png)
**5.Linux C Socket简单实例与详细注释**
 

程序为简单的“回射”，客户端将控制台输入的信息发送给服务器端，服务器原样返回信息。

服务器端：

![](Linux%20C%20Socket/ExpandedBlockStart.gif)
 
![](Linux%20C%20Socket/copycode.gif)
 

```
1 #include <sys/types.h>
 2 #include <sys/socket.h>
 3 #include <stdio.h>
 4 #include <netinet/in.h>
 5 #include <arpa/inet.h>
 6 #include <unistd.h>
 7 #include <string.h>
 8 #include <stdlib.h>
 9 #include <fcntl.h>
10 #include <sys/shm.h>
11 
12 #define MYPORT  8887
13 #define QUEUE   20
14 #define BUFFER_SIZE 1024
15 
16 int main()
17 {
18     ///定义sockfd
19     int server_sockfd = socket(AF_INET,SOCK_STREAM, 0);
20 
21     ///定义sockaddr_in
22     struct sockaddr_in server_sockaddr;
23     server_sockaddr.sin_family = AF_INET;
24     server_sockaddr.sin_port = htons(MYPORT);
25     server_sockaddr.sin_addr.s_addr = htonl(INADDR_ANY);
26 
27     ///bind，成功返回0，出错返回-1
28     if(bind(server_sockfd,(struct sockaddr *)&server_sockaddr,sizeof(server_sockaddr))==-1)
29     {
30         perror("bind");
31         exit(1);
32     }
33 
34     ///listen，成功返回0，出错返回-1
35     if(listen(server_sockfd,QUEUE) == -1)
36     {
37         perror("listen");
38         exit(1);
39     }
40 
41     ///客户端套接字
42     char buffer[BUFFER_SIZE];
43     struct sockaddr_in client_addr;
44     socklen_t length = sizeof(client_addr);
45 
46     ///成功返回非负描述字，出错返回-1
47     int conn = accept(server_sockfd, (struct sockaddr*)&client_addr, &length);
48     if(conn<0)
49     {
50         perror("connect");
51         exit(1);
52     }
53 
54     while(1)
55     {
56         memset(buffer,0,sizeof(buffer));
57         int len = recv(conn, buffer, sizeof(buffer),0);
58         if(strcmp(buffer,"exit\n")==0)
59             break;
60         fputs(buffer, stdout);
61         send(conn, buffer, len, 0);
62     }
63     close(conn);
64     close(server_sockfd);
65     return 0;
66 }
```

 
![](Linux%20C%20Socket/copycode%202.gif)
 

客户端：

![](Linux%20C%20Socket/ExpandedBlockStart%202.gif)
 
![](Linux%20C%20Socket/copycode%203.gif)
 

```
1 #include <sys/types.h>
 2 #include <sys/socket.h>
 3 #include <stdio.h>
 4 #include <netinet/in.h>
 5 #include <arpa/inet.h>
 6 #include <unistd.h>
 7 #include <string.h>
 8 #include <stdlib.h>
 9 #include <fcntl.h>
10 #include <sys/shm.h>
11 
12 #define MYPORT  8887
13 #define BUFFER_SIZE 1024
14 
15 int main()
16 {
17     ///定义sockfd
18     int sock_cli = socket(AF_INET,SOCK_STREAM, 0);
19 
20     ///定义sockaddr_in
21     struct sockaddr_in servaddr;
22     memset(&servaddr, 0, sizeof(servaddr));
23     servaddr.sin_family = AF_INET;
24     servaddr.sin_port = htons(MYPORT);  ///服务器端口
25     servaddr.sin_addr.s_addr = inet_addr("127.0.0.1");  ///服务器ip
26 
27     ///连接服务器，成功返回0，错误返回-1
28     if (connect(sock_cli, (struct sockaddr *)&servaddr, sizeof(servaddr)) < 0)
29     {
30         perror("connect");
31         exit(1);
32     }
33 
34     char sendbuf[BUFFER_SIZE];
35     char recvbuf[BUFFER_SIZE];
36     while (fgets(sendbuf, sizeof(sendbuf), stdin) != NULL)
37     {
38         send(sock_cli, sendbuf, strlen(sendbuf),0); ///发送
39         if(strcmp(sendbuf,"exit\n")==0)
40             break;
41         recv(sock_cli, recvbuf, sizeof(recvbuf),0); ///接收
42         fputs(recvbuf, stdout);
43 
44         memset(sendbuf, 0, sizeof(sendbuf));
45         memset(recvbuf, 0, sizeof(recvbuf));
46     }
47 
48     close(sock_cli);
49     return 0;
50 }
```

 
![](Linux%20C%20Socket/copycode%204.gif)
 

执行：

客户端

![](Linux%20C%20Socket/29163938-e5b43a8d3501467d8723b2de7392ab49.x-png.png)
服务器端

![](Linux%20C%20Socket/29163855-55c0a397cda04d4a9f46ada36149af3b.x-png.png)

http://images.cnitblog.com/blog/466768/201312/27111710-a88a3bab25064f0480b41f22b50d6f76.png