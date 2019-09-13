# autoInternet
四川大学校园网自动登录下线程序

--------------

>源码解释

- src/python是用python实现的脚本源代码，使用到的包/模块：requests,re,urllib。其中有4个函数，作用如下

  |函数名|参数|作用|
  |-----|---|---|
  |getLoginMsg|无|获取登录时的用的参数|
  |login|userId:学号,password:密码|登录校园网|
  |getLogoutMsg|无|获取userIndex字符串(下线参数)|
  |logout|无|下线函数|