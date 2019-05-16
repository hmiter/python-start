#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
# ================= 模块 =====================
# 一、内建模块
# 1、sys ：提供了特定系统的配置和操作
# sys.platform	用来构建解释器的操作系统平台
print(sys.platform)
# sys.version	构建时的版本信息, 包含完整的版本号和构建日期、编译器、平台信息等
print(sys.version)
# sys.version_info	同样是版本信息, 但不是字符串, 可以直接获得对应类型版本的信息
print(sys.version_info)
# sys.path[0]	搜索模块的路径列表
# sys.modules.get()	已经导入的模块列表
# sys.getrefcount()	查看对象的引用计数
# sys.getsizeof()	以字节（byte）为单位返回对象大小。这个对象可以是任何类型的对象。 所以内置对象都能返回
# sys.exc_info() 如果堆栈中的任何位置没有异常处理，则返回包含三个None值的元组。否则，返回的值是（type，value，traceback）

# 2、os ： 主要包含创建和管理进程或者文件系统内容(比如文件和目录)的函数
# os.getcwd()	获取当前所在的目录	os.getcwd() Current Working Directory
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
import datetime,time
# datetime.date：表示日期的类
# datetime.datetime：表示日期时间的类
# datetime.time：表示时间的类
# datetime.timedelta：表示时间间隔，即两个时间点的间隔
# datetime.tzinfo：时区的相关信息

print(time.time())
# time.time()：获得当前以秒表示的时间，浮点数
print(time.localtime())
print(time.localtime(time.time()))
# time.localtime([secs])：将 secs 转换至当地时区的时间，不输入 secs 则返回当前时间
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %H:%M:%S'))
# time.strftime(format[, t])：将 t 以 format 形式输出，不输入 t 则用当前时间代替
print(time.strptime('2019-06-01 20:51:11','%Y-%m-%d %H:%M:%S'))
# time.strptime(string[, format])：将时间以 string 形式输入，format 默认为"%a %b %d %H:%M:%S %Y"，即标准格式，返回 time.struct_time 对象
# time.gmtime([secs])：将 secs 转换至0时区的时间，不输入 secs 则返回当前时间
# time.mktime(t)：将t转换至当地时区的时间，是 localtime 的反函数
# time.asctime([t])：将 t 转换至当地时区的时间，不输入 t 则返回当前时间
# time.ctime([secs])：将 secs 转换至当地时区的时间，不输入 secs 则返回当前时间
# time.timezone 获得时区
# time.tzname
# time.sleep(secs) 暂停一段时间

# 5、csv
# collections base64
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431937554888869fb52b812243dda6103214cd61d0c2000

# 6、hashlib
import hashlib

# ######## md5 ########
string = "test"

md5 = hashlib.md5()
md5.update(string.encode('utf-8'))     #注意转码
res = md5.hexdigest()
print("md5加密结果:",res)

# ######## sha1 ########
sha1 = hashlib.sha1()
sha1.update(string.encode('utf-8'))
res = sha1.hexdigest()
print("sha1加密结果:",res)

# ######## sha256 ########
sha256 = hashlib.sha256()
sha256.update(string.encode('utf-8'))
res = sha256.hexdigest()
print("sha256加密结果:",res)


# ######## sha384 ########
sha384 = hashlib.sha384()
sha384.update(string.encode('utf-8'))
res = sha384.hexdigest()
print("sha384加密结果:",res)

# ######## sha512 ########
sha512 = hashlib.sha512()
sha512.update(string.encode('utf-8'))
res = sha512.hexdigest()
print("sha512加密结果:",res)

# 7、random
# random.random() # 产生0-1的随机浮点数
# random.uniform(a, b) # 产生指定范围内的随机浮点数
# random.randint(a, b) 产生指定范围内的随机整数
# random.randrange([start], stop[, step]) 从一个指定步长的集合中产生随机数
# random.choice(sequence) 从序列中产生一个随机数
# random.shuffle(x[, random]) 将一个列表中的元素打乱
# random.sample(sequence, k) 从序列中随机获取指定长度的片断

# 8、string模块
# str.capitalize() 把字符串的第一个字符大写
# str.center(width) 返回一个原字符串居中，并使用空格填充到width长度的新字符串
# str.ljust(width) 返回一个原字符串左对齐，用空格填充到指定长度的新字符串
# str.rjust(width) 返回一个原字符串右对齐，用空格填充到指定长度的新字符串
# str.zfill(width) 返回字符串右对齐，前面用0填充到指定长度的新字符串
# str.count(str,[beg,len]) 返回子字符串在原字符串出现次数，beg,len是范围
# str.decode(encodeing[,replace]) 解码string,出错引发ValueError异常
# str.encode(encodeing[,replace]) 解码string
# str.endswith(substr[,beg,end]) 字符串是否以substr结束，beg,end是范围
# str.startswith(substr[,beg,end]) 字符串是否以substr开头，beg,end是范围
# str.expandtabs(tabsize = 8) 把字符串的tab转为空格，默认为8个
# str.find(str,[stat,end]) 查找子字符串在字符串第一次出现的位置，否则返回-1
# str.index(str,[beg,end]) 查找子字符串在指定字符中的位置，不存在报异常
# str.isalnum() 检查字符串是否以字母和数字组成，是返回true否则False
# str.isalpha() 检查字符串是否以纯字母组成，是返回true,否则false
# str.isdecimal() 检查字符串是否以纯十进制数字组成，返回布尔值
# str.isdigit() 检查字符串是否以纯数字组成，返回布尔值
# str.islower() 检查字符串是否全是小写，返回布尔值
# str.isupper() 检查字符串是否全是大写，返回布尔值
# str.isnumeric() 检查字符串是否只包含数字字符，返回布尔值
# str.isspace() 如果str中只包含空格，则返回true,否则FALSE
# str.title() 返回标题化的字符串（所有单词首字母大写，其余小写）
# str.istitle() 如果字符串是标题化的(参见title())则返回true,否则false
# str.join(seq) 以str作为连接符，将一个序列中的元素连接成字符串
# str.split(str=‘‘,num) 以str作为分隔符，将一个字符串分隔成一个序列，num是被分隔的字符串
# str.splitlines(num) 以行分隔，返回各行内容作为元素的列表
# str.lower() 将大写转为小写
# str.upper() 转换字符串的小写为大写
# str.swapcase() 翻换字符串的大小写
# str.lstrip() 去掉字符左边的空格和回车换行符
# str.rstrip() 去掉字符右边的空格和回车换行符
# str.strip() 去掉字符两边的空格和回车换行符
# str.partition(substr) 从substr出现的第一个位置起，将str分割成一个3元组。
# str.replace(str1,str2,num) 查找str1替换成str2，num是替换次数
# str.rfind(str[,beg,end]) 从右边开始查询子字符串
# str.rindex(str,[beg,end]) 从右边开始查找子字符串位置
# str.rpartition(str) 类似partition函数，不过从右边开始查找
# str.translate(str,del=‘‘) 按str给出的表转换string的字符，del是要过虑的字符

# 9、urllib模块：
# urllib.quote(string[,safe]) 对字符串进行编码。参数safe指定了不需要编码的字符
# urllib.unquote(string) 对字符串进行解码
# urllib.quote_plus(string[,safe]) 与urllib.quote类似，但这个方法用‘+‘来替换‘ ‘，而quote用‘%20‘来代替‘ ‘
# urllib.unquote_plus(string ) 对字符串进行解码
# urllib.urlencode(query[,doseq]) 将dict或者包含两个元素的元组列表转换成url参数。
# 例如 字典{‘name‘:‘wklken‘,‘pwd‘:‘123‘}将被转换为”name=wklken&pwd=123″
# urllib.pathname2url(path) 将本地路径转换成url路径
# urllib.url2pathname(path) 将url路径转换成本地路径
# urllib.urlretrieve(url[,filename[,reporthook[,data]]]) 下载远程数据到本地
# filename：指定保存到本地的路径（若未指定该，urllib生成一个临时文件保存数据）
# reporthook：回调函数，当连接上服务器、以及相应的数据块传输完毕的时候会触发该回调
# data：指post到服务器的数据
# rulrs = urllib.urlopen(url[,data[,proxies]]) 抓取网页信息，[data]post数据到Url,proxies设置的代理
# urlrs.readline() 跟文件对象使用一样
# urlrs.readlines() 跟文件对象使用一样
# urlrs.fileno() 跟文件对象使用一样
# urlrs.close() 跟文件对象使用一样
# urlrs.info() 返回一个httplib.HTTPMessage对象，表示远程服务器返回的头信息
# urlrs.getcode() 获取请求返回状态HTTP状态码
# urlrs.geturl() 返回请求的URL

# 10、re模块
# re.match(pattern, string, flags=0) 从字符串的起始位置匹配，如果起始位置匹配不成功的话，match()就返回none
# re.search(pattern, string, flags=0) 扫描整个字符串并返回第一个成功的匹配
# re.findall(pattern, string, flags=0) 找到RE匹配的所有字符串，并把他们作为一个列表返回
# re.finditer(pattern, string, flags=0) 找到RE匹配的所有字符串，并把他们作为一个迭代器返回
# re.sub(pattern, repl, string, count=0, flags=0) 替换匹配到的字符串

# 二、第三方模块
# 第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索
# 1、Pillow 图像处理库
# 2、requests 处理URL资源
# 3、chardet 用它来检测编码
# 4、psutil 有许多系统命令可以让我们时刻监控系统运行的状态，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块
# 5、MySQL-python mysql驱动
# 6、NumPy 科学计算
# 7、Jinja2用于生成文本的模板工具
