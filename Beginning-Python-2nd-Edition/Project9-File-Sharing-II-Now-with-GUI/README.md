# Project 9: File Sharing II—Now with GUI!

Error:
errno 10061 socket.error

本项目是对27章开发的文件共享系统进行扩展，添加一个GUI客户端。

**目的：**

1. 让程序更易用，才会有更多的人会使用它，这样才有更多的用户共享文件。
2. 展示模块化设计的程序是多么容易扩展，也是使用**面向对象程序设计**的原因之一。

GUI客户端的需求：

- 它应该允许用户输入文件名，并将其提交给服务器的fetch方法。
- 它应该能列出服务器文件目录目录中当前的可用文件。

有用的工具：

- wxPython工具包。参见第12章。书中代码使用wxPython2.6开发。

**ERROR**

- xmlrpclib.Fault: <Fault 1: "<class 'socket.error'>:[Errno 10061] ">
> line拼写错误
    ```python
    for line in open(urlfile):
        line = line.strip()
        self.server.hello(line)
    ```
    未解决
