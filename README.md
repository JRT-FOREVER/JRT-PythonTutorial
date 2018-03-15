# JRT-PythonTutorial
**_用于JRT学习交流_**
## 简要说明
- 目录序号由一个 ~~两位十进制~~ (用0补不是markdown语法) 数字组成，内容逐渐更新，每一个目录表示一天的内容，整个项目包含基础语法和附加项目两部分，附加项目部分欢迎大家共同贡献代码，每个小项目单独放入一个文件夹，放在Tutorial根目录即可。

### 写在开始之前

请注意这个文件`.editorconfig`

这个文件了定义了换行格式字符编码。一般的代码编辑器都可以识别


[GitHub用法](./01/GithubTutorial.md)

##### 关于比较常见的python 代码头部
```python
#!/usr/bin/python
or
#!/usr/bin/env python
```
一般有这两张写法，这两种写法有区别

如果你用 python xxoo.py 来运行，那么写不写都没关系，如果要用 ./xxoo.py 那么就必须加这行，这行被称为 [shebang](https://zh.wikipedia.org/wiki/Shebang) , 用来为脚本语言指定解释器.

通常认为用 #!/usr/bin/env python 要比 #!/usr/bin/python 更好，因为 python 解释器有时并不安装在默认路径，例如在 virtualenv 中。

当然pyhton2 和python3 代码不完全兼容。一般系统默认python环境都是python2的  python == python2, python3 == python3

所以最好的写法是

```python
#!/usr/bin/env python3
```

##### python 代码的第二行
```python
#coding=utf-8
or
#-*- coding: utf-8 -*-
```
> 对于python解释器来说，这两种写法一样。但是对于编辑器来讲，可能会出现识别问题。第二种写法兼容性更好

这行代码是做什么用的？

> 指定字符编码，当然你如果用纯英文写可以不写这行（包括注释）qwq ， 不同操作系统的默认编码不同。比如windows 的中文默认编码GB2312，一般服务器都是Unix && Linux 默认编码utf-8。

为什么要用utf-8 ？ 这个问题解释起来很麻烦。。。记住utf-8 比 GB2312 好


### 所以最后，文件前两行应该写的是

```python
#!/usr/bin/env python3
#-*- coding: utf-8 -*-
```

***

## 目录
1. 常量，变量，运算符，内置函数，数据类型
2. 流程控制，导入
3. 函数和面向对象基础
4. 模块和高级专题
