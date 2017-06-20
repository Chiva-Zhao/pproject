# 运行目录或压缩文件
# 有一个复杂的脚本涉及多个文件的应用程序。想一些简单的方法让用户运行程序
# 如果你的应用程序已经有多个文件，你可以把你的应用程序放进它自己的目录并添
# 加一个 main .py 文件。举个例子，你可以像这样创建目录：
# myapplication/
#     spam.py
#     bar.py
#     grok.py
#     __main__.py
# 如果 main .py 存在，你可以简单地在顶级目录运行 Python 解释器：
# bash % python3 myapplication
# 解释器将执行 main .py 文件作为主程序。
# 如果你将你的代码打包成 zip 文件，这种技术同样也适用，举个例子：
# bash % ls
# spam.py bar.py grok.py __main__.py
# bash % zip -r myapp.zip *.py
# bash % python3 myapp.zip
# ... output from __main__.py ...
# 创建一个目录或 zip 文件并添加 main .py 文件来将一个更大的 Python 应用打包
# 是可行的。这和作为标准库被安装到 Python 库的代码包是有一点区别的。相反，这只
# 是让别人执行的代码包。
# 由于目录和 zip 文件与正常文件有一点不同，你可能还需要增加一个 shell 脚本，
# 使执行更加容易。例如，如果代码文件名为 myapp.zip，你可以创建这样一个顶级脚本：
#!/usr/bin/env python3 /usr/local/bin/myapp.zip