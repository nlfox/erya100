#ERYA Helper

##基于Mitmproxy来绕过逗逼尔雅的诸多限制
###原理说明
1. 关于自动暂停：在mitmproxy中修改response把自动暂停的代码直接去掉了= =绿色安全无副作用
2. 关于问题：把答案输出了...

###环境准备
1. Windows
安装Python与pip然后
`pip install mitmproxy`

2. Ubuntu 
`sudo apt-get install python-pip python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev`
`sudo pip install mitmproxy`

###使用说明
1. 建议使用Chrome 里的 SwitchyOmega 插件。
2. SwitchyOmega设置中导入所给bak文件。
3. 运行`python erya.py`
4. 代理选择erya。然后一切正常操作即可。


