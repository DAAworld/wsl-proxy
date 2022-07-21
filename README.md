# wsl-proxy
wsl2 与windows10/11之间的端口转发

ipnet.py
是端口转发的主文件，将需要转发的端口号放置在port_list中

ipnet.bat
将后面的路径替换为ipnet.py文件所在路径，然后“win+R”调出“运行”界面， 输入‘shell:startup’，打开自启动文件夹。将ipnet.bat文件放置在该
文件夹中，即可开机自动运行端口转发。

ipnet.ps1
将后面的路径替换为ipnet.py文件所在路径,然后将文件放置在已经在环境变量里的文件夹或将该文件路径添加在环境变量中，即可在terminal中使用“ipnet”命令
手动转发。
