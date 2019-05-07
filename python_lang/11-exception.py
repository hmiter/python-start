#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()

# 一：traceback说明
# 该模块提供了一个标准接口来提取，格式化和打印Python程序的堆栈跟踪。它完全模仿Python解释器在打印堆栈跟踪时的行为。
# 当您想要在程序控制下打印堆栈跟踪时，这很有用。
#
# 二：模块定义了以下功能：
# 复制代码
# traceback.print_tb（tb [，limit [，file ] ] ）
# 打印以限制回溯对象tb的堆栈跟踪条目。如果 省略限制或者None打印所有条目。如果文件被省略或者None输出到了sys.stderr;
# 否则它应该是一个打开的文件或文件类对象来接收输出。
#
# traceback.print_exception（etype，value，tb [，limit [，file ] ] ）
# 打印异常信息，并将traceback tb中的堆栈跟踪条目限制为文件。这与以下方面有所不同：
# （1）如果tb不是，则打印一个标题;
# （2）在堆栈跟踪之后打印异常etype和值 ;
# （3）如果etype的值和值具有适当的格式，则会打印语法错误发生的行，并在其中指出错误的大概位置。
# print_tb()NoneTraceback (most recent call last):SyntaxError
#
# traceback.print_exc（[ limit [，file ] ] ）
# 这是一个简写。（事实上​​，它用于以线程安全的方式检索相同的信息，而不是使用已弃用的变量。）
# print_exception(sys.exc_type, sys.exc_value, sys.exc_traceback, limit, file)sys.exc_info()
#
# traceback.format_exc（[ 限制] ）
# 这就像是print_exc(limit)返回一个字符串，而不是打印到一个文件。
#
# 2.4版本中的新功能。
#
# traceback.print_last（[ limit [，file ] ] ）
# 这是一个简写。一般而言，只有在例外达到交互式提示后才能使用（请参阅）。
# print_exception(sys.last_type, sys.last_value, sys.last_traceback, limit, file)sys.last_type
#
# traceback.print_stack（[ f [，limit [，file ] ] ] ）
# 该函数从其调用点打印堆栈跟踪。可选的 f参数可用于指定要启动的备用堆栈帧。可选限制和文件参数与for具有相同的含义 print_exception()。
#
# traceback.extract_tb（tb [，limit ] ）
# 返回一个列表，最多可以限制从回溯对象tb中提取的“预处理”堆栈跟踪条目。这对堆栈跟踪的替代格式非常有用。
# 如果限制被忽略或者None所有条目被提取。“预处理”堆栈跟踪条目是一个4元组（文件名，行号，函数名称*，文本），
# 表示通常为堆栈跟踪打印的信息。该文本是一个带有前导和尾随空白字符的字符串; 如果源不可用，它是None。
#
# traceback.extract_stack（[ f [，limit ] ] ）
# 从当前堆栈帧中提取原始回溯。返回值与格式相同extract_tb()。可选的f和限制 参数与for具有相同的含义print_stack()。
#
# traceback.format_list（extracted_list ）
# 给出extract_tb()or extract_stack()返回的元组列表，返回一个准备打印的字符串列表。
# 结果列表中的每个字符串对应于参数列表中具有相同索引的项目。每个字符串以换行符结束;
# 这些字符串也可以包含内部换行符，对于那些源文本行不是的项目 None。
#
# traceback.format_exception_only（etype，value ）
# 格式化追溯的异常部分。的参数是异常类型，VLAN时和值，如由下式给出sys.last_type和 sys.last_value。
# 返回值是一个字符串列表，每个字符串都以换行符结尾。通常，该列表包含一个字符串; 但是，
# 对于 SyntaxError例外情况，它包含几行（打印时）显示有关语法错误发生位置的详细信息。指示发生异常的消息是列表中总是最后一个字符串。
#
# traceback.format_exception（etype，value，tb [，limit ] ）
# 格式化堆栈跟踪和异常信息。参数与相应的参数具有相同的含义print_exception()。返回值是一串字符串，每个字符串以换行符结尾，
# 一些字符串包含内部换行符。当这些行连接并打印时，打印的文本与打印的文本完全相同print_exception()。
#
# traceback.format_tb（tb [，limit ] ）
# 速记。format_list(extract_tb(tb, limit))
#
# traceback.format_stack（[ f [，limit ] ] ）
# 速记。format_list(extract_stack(f, limit))
#
# traceback.tb_lineno（tb ）
# 该函数返回在回溯对象中设置的当前行号。这个函数是必须的，因为在2.3之前的Python版本中，当-O标志被传递给Python时，tb.tb_lineno它没有被正确更新。这个功能在2.3版以后没有用。