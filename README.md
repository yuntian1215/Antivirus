# 交大金课（项目管理）课程设计


## 前端界面运行方法：
前端运行所需的python环境保存在虚拟环境VirEnv里面，运行时只需进入虚拟环境即可
1. 打开终端(Terminal)
2. 进入Security_Project/VirEnv/Scripts目录下：
   cd VirEnv/Scripts
3. 进入虚拟环境： 
   activate
   
进入后如图所示:![img.png](img.png) 

4. 使用streamlit指令运行前端界面：
    streamlit run web/主页.py
   
运行如图所示:![img_1.png](img_1.png)  
   此时用浏览器打开终端提示的网址即可看到对应页面


## 项目结构
主页.py是项目主页，启动的时候可以从这个文件启动（如前面教程所述）  
/pages/中保存前端页面  
/white_list/, /crypto_jacking/, /virus_database/文件目录下分别放白名单、恶意挖矿脚本、病毒库更新的后端代码。  
每个功能模块包的API.py，用于存放供前端调用的功能函数（比如按下某个按钮该触发哪个函数）。

## 合作
需要加按钮等需求，还有功能函数等写的时候多跟前端交流一下

## 前端教程
streamlit比Django简单很多，如果想要看可以直接百度搜，学起来很容易  
官网https://docs.streamlit.io/  
其它教程https://zhuanlan.zhihu.com/p/448853407