# win应急响应检测工具



![1](https://github.com/yuag/Select-YARA-Rule-Folder/assets/34123873/c22e11aa-f7ba-4059-a33e-5c930cfb33e9)




<br>
<br>

# 功能

系进程列表

系统服务    

系统日志 

网络连接 

计划任务 

共享资源  

近三天内修改的文件  

显示进程和服务信息  

显示进程和所有者 

yara脚本（支持检查shell，勒索病毒，挖矿，等）


yara脚本合集：

https://github.com/InQuest/awesome-yara/tree/master

https://segmentfault.com/q/1010000043271331




<br>
<br>

# 注意

安装yara库遇到的坑 

libyara.dll 提示找不到 。

解决方法：全局搜索libyara.dll

把这里的libyara.dll复制到（python3根目录）正确目录就可以了

参考：https://blog.csdn.net/weixin_43781139/article/details/131087788








<br>
<br>
<br>
<br>
<br>
<br>
=======================================分割线===============================================

# Linux应急响应检测工具

<img width="704" alt="image" src="https://github.com/yuag/Emergency-response-tools/assets/34123873/ae16d38e-de93-4eab-94dd-6077d9646c3b">


<br>
<br>

<img width="870" alt="image" src="https://github.com/yuag/Emergency-response-tools/assets/34123873/12e01fa8-cc3f-4ae8-9aad-7210671158e8">






<br>
<br>

# 功能

 1.  获取对外网络连接情况
 2.  显示进程
 3.  任务启动项 
 4.  检查异常端口
 5.  检查定时任务 
 6.  监控与目标IP通信的进程
 7.  CPU降序排序
 8.  查询历史命令
 9.  7天内被修改过的文件
 10. 登录记录
 11. 多少IP在爆破主机的root帐号
 12. 哪些IP在爆破
 13. 爆破用户名字典是什么
 14. 登录成功的日期、用户名、IP：
 15. 查询sudo权限账户
 16. 使用YARA规则检测文件
 17. 一键执行所有命令并导出
 18. 查找72小时内新增的文件            
 0.  退出





<br>
<br>


# 遇到的错误


ubuntu


安装yara错误
OSError: /usr/lib/libyara.so: cannot open shared object file: No such file or directory

libyara.so文件复制到这个目录就可以
/usr/lib/libyara.so

root 用户权限
cp -r libyara.so /usr/lib/

<br>
<br>




<br>
<br>

cenetos

cenetos7 直接安装yara安装不成功 只能虚拟环境才成功。 后续测8不会报错。

使用虚拟环境（可选）：

如果您尚未使用虚拟环境，请考虑创建一个虚拟环境来隔离该项目的 Python 环境：


python3 -m venv myenv
source myenv/bin/activate





<br>
<br>
注意：选择一个命令 16. 使用YARA规则检测文件

路径一定不要加 单/双引号 不然会报错误

