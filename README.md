# 项目管理课程设计


## 前端界面运行方法
### 环境配置
OpenEuler环境
>1. 在虚拟机中克隆项目地址：git clone https://github.com/riacd/Security_Project.git
>2. 更新pip版本：python -m pip install --upgrade pip
>3. 安装所需Python包：pip3 install streamlit

[comment]: <> (>3. 安装所需Python包：pip3 install -r requirements.txt  )

windows环境：
前端运行所需的python环境保存在虚拟环境VirEnv里面，运行时只需进入虚拟环境即可
>1. 打开终端(Terminal)
>2. 进入Security_Project/VirEnv/Scripts目录下：
>   cd VirEnv/Scripts
>3. 进入虚拟环境： 
>   activate  
> 进入后如图所示:![img.png](img.png)

### 加载前端界面
4. 使用streamlit指令运行前端界面（注意当前所处目录应该在Security_Project/目录下）：
    streamlit run web/主页.py  
   运行如图所示:![img_1.png](img_1.png)  
5. 此时用浏览器打开终端提示的网址即可看到对应页面


## 项目结构
主页.py是项目主页，启动的时候可以从这个文件启动（如前面教程所述）  
/pages/中保存前端页面  
/clamav_test/文件夹下存放后端整体的代码（在这里面开发时，要保证每次上传的修改功能完整，不然会影响到其他人）
/white_list/, /crypto_jacking/, /virus_database/文件目录下分别是按分工分配（白名单、恶意挖矿脚本、病毒库更新）的文件目录，一个模块出问题不会影响到其它组员的开发  
每个分工的文件夹下的API.py，用于存放供前端调用的功能函数（比如按下某个按钮该触发哪个函数）。

## 合作
1. 前端需要知道，后端要什么样的界面。前端会按照需求做出一个包含所有需要元素的简易demo。  
2. 前端还需要知道每个按钮需要触发什么函数，文本输入框的文本需要传递到哪里等。后端组员可以把触发的函数和一些数据放在各自分工文件夹下的API.py中方便前端调用，也可以共用global_API.py。  
3. 项目暂时这么设计的，后面根据开发需要可以随时修改，或者有更好的想法直接在上面改就是了。

## 前端教程
streamlit比Django简单很多，如果想要看可以直接百度搜，学起来很容易  
官网https://docs.streamlit.io/  
其它教程https://zhuanlan.zhihu.com/p/448853407  

## TODO