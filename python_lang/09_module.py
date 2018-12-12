#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ================= 模块 =====================
# 一、内建模块
# 1、sys ：提供了特定系统的配置和操作
# sys.platform	用来构建解释器的操作系统平台
# sys.version	构建时的版本信息, 包含完整的版本号和构建日期、编译器、平台信息等
# sys.version_info	同样是版本信息, 但不是字符串, 可以直接获得对应类型版本的信息
# sys.path[0]	搜索模块的路径列表
# sys.modules.get()	已经导入的模块列表
# sys.getrefcount()	查看对象的引用计数
# sys.getsizeof()	以字节（byte）为单位返回对象大小。这个对象可以是任何类型的对象。 所以内置对象都能返回

# 2、os ： 主要包含创建和管理进程或者文件系统内容(比如文件和目录)的函数
# os.getcwd()	获取当前所在的目录	os.getcwd()
# os.chdir()	切换目录	os.chdir('..') (.. 为父级目录, 这里表示切换到上一级目录, 相当于命令行的 cd ..)
# os.getenv()	获取系统变量的值(若变量不存在返回 None)	os.getenv('SHELL')
# os.environ.getenv()	获取系统变量的值(若变量不存在会引发异常)	os.environ.getenv('SHELL')
# os.listdir()	列出目录下的全部文件	os.listdir('dir'), 列出 dir 目录下的全部文件
# os.walk()	递归地遍历指定的目录, 对于每个目录都会生成一个元组, 其中包含了目录的路径、该目录下所有的子目录以及该目录下所
#           有文件的列表。它是一个生成器, 可以用 list() 转换成一个列表	os.walk('dir'), list(os.walk('dir'))
# os.makedir()	创建一个目录, 只能创建单层目录, 若创建多层目录会报错	os.makedir('dir'), 创建一个名为 dir 的目录
# os.makedirs()	创建多层目录	os.makedirs('/dir2/dir3')
# os.remove()	删除指定文件	os.remove('1.txt'), 删除当前目录下的 1.txt 文件
# os.rmdir()	删除目录	os.rmdir('dir1'), 删除当前目录下的 dir 目录
# os.rename()	重命名文件或者目录	os.rename('dir2', 'dir1'), 将 dir2 目录重命名为 dir1

# 3、os.path
# os.path.abspath(path)  返回path规范化的绝对路径。
# os.path.basename(path)	获得指定文件路径的文件名字
# os.path.dirname()	获得文件路径的目录名字
# os.path.exists()	判断文件或者目录是否存在
# os.path.isdir()	判断指定路径是否是目录
# os.path.isfile()	判断指定路径是否是文件
# os.path.join()	拼接路径
# os.path.split(path)	将path分割成目录和文件名二元组返回
# os.path.splitext()	获得路径的后缀

# 4、datetime,time
# datetime.date：表示日期的类
# datetime.datetime：表示日期时间的类
# datetime.time：表示时间的类
# datetime.timedelta：表示时间间隔，即两个时间点的间隔
# datetime.tzinfo：时区的相关信息

# time.localtime([secs])：将 secs 转换至当地时区的时间，不输入 secs 则返回当前时间
# time.gmtime([secs])：将 secs 转换至0时区的时间，不输入 secs 则返回当前时间
# time.strptime(string[, format])：将时间以 string 形式输入，format 默认为"%a %b %d %H:%M:%S %Y"，即标准格式，返回 time.struct_time 对象
# time.time()：获得当前以秒表示的时间，浮点数
# time.mktime(t)：将t转换至当地时区的时间，是 localtime 的反函数
# time.asctime([t])：将 t 转换至当地时区的时间，不输入 t 则返回当前时间
# time.ctime([secs])：将 secs 转换至当地时区的时间，不输入 secs 则返回当前时间
# time.timezone 获得时区
# time.tzname
# time.sleep(secs) 暂停一段时间
# time.strftime(format[, t])：将 t 以 format 形式输出，不输入 t 则用当前时间代替

# 5、csv
# collections base64
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431937554888869fb52b812243dda6103214cd61d0c2000

# 二、第三方模块
# 第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索
# 1、Pillow 图像处理库
# 2、requests 处理URL资源
# 3、chardet 用它来检测编码
# 4、psutil 有许多系统命令可以让我们时刻监控系统运行的状态，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块
# 5、MySQL-python mysql驱动
# 6、NumPy 科学计算
# 7、Jinja2用于生成文本的模板工具
