# FTP_file_transfer_management
## 介绍
`pyFTP` 是一个用来在Linux（Ubuntu）上管理ftp服务器文件的工具。它使用`python`实现，基于经典的`libftp`库，保留了该库的所有原有功能。您可以用它实现的核心功能包括：**ftp服务器上传/下载文件/文件夹**，以及**删除ftp服务器上的文件/文件夹**。我们**对ftp的文件夹实现递归处理**，确保可以**实现便利的传输或者删除ftp服务器上的文件和文件夹**。

## 环境

 - Ubuntu16.04
 - Python3.7

##  下载

```bash
pip install pyFTP
```
## 使用

 - 导入
```python
from pyFTP.utils.FTPTools import FTPTools
```
 - 建立对象
 

```python
obj = FTPTools('ip', 'username', 'password')
```
- 实现功能

| run() |  参数1     | 参数2|参数3|
|:--------:|:-------------:|:--------:|:--------:|
| 上传文件夹 |  ftp文件夹路径 |本地文件夹路径 |`'upload folder'`|
| 上传文件 | ftp文件夹路径 | 本地文件+文件名 |`'upload file'`|
| 下载文件夹 |  ftp文件夹路径 |本地文件夹路径 |`'download folder'`|
| 下载文件 | ftp文件路径+文件名 |本地文件夹路径 | `'download file'`|
| 删除文件夹 |  ftp文件夹路径 |`''` |`'delete folder'`|
| 删除文件 |  ftp文件路径+文件名 |`''` |`'delete file'`|

- 举例

```python
# upload older
localPath = '/media/lwt/qysdcj/01trainset/beads1227/'
ftpPath = '/private/lwt/qysdcj/jojo/'
obj.run(ftpPath, localPath, 'upload folder')

# delete folder
# ftpFolder = '/private/lwt/qysdcj/jojo/'
# obj.run(ftpFolder, '', 'delete folder')    
  
# download older
# ftpPath = '/private/lwt/qysdcj/'
# localPath = '/media/lwt/qysdcj/01trainset/beads1226/nulckaj/'
# obj.run(ftpPath, localPath, 'download folder')    
```

## 相关项目

 - [libftp](https://pypi.org/search/?q=libftp) -本项目在此项目的基础上进行了修改，并保留了原有的所有方法。

## 负责人

 - [AsajuHuishi](https://github.com/AsajuHuishi)




