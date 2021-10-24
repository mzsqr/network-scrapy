## 爬虫项目
----

### 简介

计算机网络课程设计的**爬虫项目**

采用Python进行开发

使用**Scrapy**框架完成程序的设计

----

### 开始

建议使用Python的虚拟环境进行管理

李屹荣在用的是virtualenv，以下是按照virtualenv的方法进行项目的搭建过程

1. 保证按照好Python
2. 在命令行(或者终端)输入 pip install virtualenv
3. 通过git工具同步代码：

   1. 下载Git
   2. 在你需要下载代码的位置右键打开git bash
   3. 输入如下命令进行初始化：
   ```
   git config --global user.name "名字/你想要的"
   git config --global user.email "邮箱"
   ```
   4. 输入如下命令克隆仓库并且切换分支，不要在master分支上修改：
   ```
   git clone git@github.com:mzsqr/network-scrapy.git
   # 或者git clone https://github.com/mzsqr/network-scrapy.git
   # 区别就是上面那个要在自己的电脑上个加上公钥，下面这个输入账号密码
   git switch dev
   ```
4. 创建Python虚拟环境：进入virus目录，打开命令行输入如下命令：
```
virtualenv venv
# 每次需要安装额外的库首先都要运行这个命令
# 避免污染本程序的库/你的电脑上的库
.\venv\Scripts\avtive
```
5. 确保安装好scrapy，使用以下命令：
```
pip install scrapy
```
6. 新建自己的爬虫脚本：进入到virus\virus\spiders文件夹，在命令行输入以下命令（或者自己直接在里面创建也可以，参考示例文件）
```
scrapy genspider 爬虫文脚本的名字 爬取的网页（不需要协议）
```
----

### 注意事项

- 不一定要用Python的虚拟环境，只是为了避免各个库之间的污染
- 如果使用了Python的虚拟环境，必须要每次运行命令之前都使用active脚本启动
- 上述只是一个项目搭建的过程，实际上的使用要自己探索

---

### 一些你可能用到的Git命令

```
git add . # 添加修改到本地
git commit -m "你的注释" # 提交本地修改到本地仓库
git pull # 拉取远程仓库，每次上传之前都要输入这个命令
git push # 上传内容，上传之前要先做上面的三个操作
```
其实IDE中都有可视化操作，不过我不喜欢

----

### 示例爬虫

文件./virus/spiders/quotes_spider.py是示例文件，一下是关于运行示例文件的说明：

1. 示例文件时一个最基本的爬虫，爬取网页"http://quotes.toscrape.com/page/1/"的内容，你可以打开查看网页结构
2. 在运行之前你需要先在项目的根目录创建一个target文件夹，或者更改一下行的内容：
```
filename = f"target/quotes-{page}.html" # line26 表示爬取的网页的储存位置
```
3. 在项目根目录下使用终端运行如下命令：
```
scrapy crawl quotes
```
4. 查看target目录下会有一些网页，实际上应该在爬取的时候就处理这些网页的Response，得到需要得到数据即可，不过这里为了简单就不处理了
