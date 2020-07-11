import os
import sys

# 终端先输入 cd \ 再运行效果更佳

# 文件所在路径
print('\n\033[31m文件所在路径\033[0m')
print('\033[0;36m __file__: \033[0m %s' % __file__)

# realpath 绝对路径，命令是显示软连接内容源头的真正目录
print('\033[0;36m os.path.realpath(__file__): \033[0m %s' % os.path.realpath(__file__))

# abspath 绝对路径，命令是显示软连接的所在目录
print('\033[0;36m os.path.abspath(__file__): \033[0m %s' % os.path.abspath(__file__))

# 文件所在目录
print('\n\033[31m文件所在目录\033[0m')
print('\033[0;36m os.path.split(__file__)[0]: \033[0m %s' % os.path.split(__file__)[0])
print('\033[0;36m os.path.dirname(__file__): \033[0m %s' % os.path.dirname(__file__))

# 文件所在目录（输出绝对路径）
print('\n\033[31m文件所在目录（输出绝对路径）\033[0m')
print('\033[0;36m os.path.split(os.path.realpath(__file__))[0]: \033[0m %s' % os.path.split(os.path.realpath(__file__))[0])
print('\033[0;36m os.path.dirname(os.path.realpath(__file__)): \033[0m %s' % os.path.dirname(os.path.realpath(__file__)))

# 获取文件所在目录的上一级目录
print('\n\033[31m获取文件所在目录的上一级目录\033[0m')
print('\033[0;36m os.path.dirname(os.path.dirname(__file__)): \033[0m %s' % os.path.dirname(os.path.dirname(__file__)))

# 文件运行路径（打包后用处较大）
print('\n\033[31m文件运行路径（打包后用处较大）\033[0m')
print('\033[0;36m os.path.dirname(os.path.realpath(sys.executable)): \033[0m %s' % os.path.dirname(os.path.realpath(sys.executable)))

# 连接路径
print('\n\033[31m连接路径\033[0m')
print('\033[0;36m os.path.join(dirpath,"test","test.txt"): \033[0m %s' % os.path.join(os.path.dirname(os.path.realpath(__file__)), "test", "test.txt"))

# 工作路径（cmd 最前面的 C:\Users\shj> ）
print('\n\033[31m工作路径（cmd 最前面的 C:\\Users\\shj> )\033[0m')
print('\033[0;36m os.getcwd(): \033[0m %s' % os.getcwd())
print('\033[0;36m os.path.abspath("."): \033[0m %s' % os.path.abspath('.'))
print('\033[0;36m os.path.abspath(".."): \033[0m %s' % os.path.abspath('..'))
print('\033[0;36m os.path.abspath("fileName.txt"): \033[0m %s' % os.path.abspath('fileName.txt'))
print('\033[0;36m os.path.abspath(os.curdir): \033[0m %s' % os.path.abspath(os.curdir))
