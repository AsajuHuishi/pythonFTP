
# pythonFTP
## 地址

 - [github](https://github.com/AsajuHuishi/FTP_file_transfer_management/tree/main/pyFTP)
 - [pythonFTP 0.0.6](https://pypi.org/manage/project/pythonFTP/release/0.0.6/)

## 介绍
`pythonFTP` 是一个用来在Linux（Ubuntu）上管理ftp服务器文件的工具。它使用`python`实现，基于经典的`libftp`模块，保留了该模块的所有原有功能。它实现的核心功能包括：**ftp服务器上传/下载文件/文件夹，在ftp服务器上创建文件夹，删除ftp服务器上的文件/文件夹**。我们**对ftp的文件夹实现递归处理**，确保可以**实现便利的传输和管理ftp服务器上的文件和文件夹**。

## 环境

 - Ubuntu16.04
 - Python3.7

##  下载
0.0.6版本

```bash
pip install pythonFTP
```
## 使用

 - **模块导入**
```python
from pythonFTP.FTPTools import FTPTools
```
 - **对象建立**
 

```python
obj = FTPTools('ip', 'username', 'password')
```
- **核心功能实现**

| run() |  参数1     | 参数2|参数3|
|:--------:|:-------------:|:--------:|:--------:|
| **上传文件夹** |  ftp文件夹路径 |本地文件夹路径 |`'upload folder'`|
| **上传文件** | ftp文件夹路径 | 本地文件+文件名 |`'upload file'`|
| **下载文件夹** |  ftp文件夹路径 |本地文件夹路径 |`'download folder'`|
| **下载文件** | ftp文件路径+文件名 |本地文件夹路径 | `'download file'`|
| **删除文件夹** |  ftp文件夹路径 |`''` |`'delete folder'`|
| **删除文件** |  ftp文件路径+文件名 |`''` |`'delete file'`|
| **创建文件夹**| ftp文件夹路径|`''` |`'create folder'`|

**举例**

```python
localPath = '/media/lwt/qysdcj/'
ftpPath = '/private/lwt/qysdcj/'
obj.run(ftpPath, localPath, 'upload folder')

# 上传一个文件
localFile = '/media/lwt/qysdcj/GT_136.tif'
ftpPath = '/private/lwt/qysdcj/'
obj.run(ftpPath, localFile, 'upload file')

# 删除文件
i = 136
ftpFile = '/private/lwt/qysdcj/GT_'+str(i)+'.tif'
obj.run(ftpFile, '', 'delete file')

# 删除文件夹
ftpFolder = '/private/lwt/qysdcj/'
obj.run(ftpFolder, '', 'delete folder')    

# 下载文件
ftpFile = '/private/lwt/qysdcj/LR_1.tif'
localPath = '/media/lwt/qysdcj/01trainset/'
obj.run(ftpFile, localPath, 'download file')    

# 下载文件夹
ftpPath = '/private/lwt/qysdcj/'
localPath = '/media/lwt/qysdcj/01trainset/'
obj.run(ftpPath, localPath, 'download folder')    

# 创建文件夹
ftpPath = '/private/zengxinyang/qysdcj/'
obj.run(ftpPath, '', 'create folder') 
```

## 相关项目

 - [libftp](https://pypi.org/search/?q=libftp) 本项目在此项目的基础上进行了修改，并保留了原有的所有方法。您可以在`pyFTP`中使用以下命令，它包括原来模块中的所有功能。

```python
from pythonFTP.ftplib2 import FTP 
```


## 负责人

 - [AsajuHuishi](https://github.com/AsajuHuishi)




