Git使用
=====

为什么要把Git 和 Github 分开呢。应为本身就是两个东西。

Git 是版本控制软件。类似的还有svn

Github 是代码托管平台。类似的有gitlib, gitee, bitbucket, Coding........

> 为什么要用Github？ Github 重新定义是社会化编程这一概念

这里不想说千篇一律的东西。比如分支管理，打标签啊之类的


[git中文文档](https://git-scm.com/book/zh/v2)

[如果你看不懂版本分支图，请看这篇](https://github.com/SB-IM/developer-center/wiki/Guidelines-for-Developers)

[如何写一个优秀的commit](https://github.com/linuxdeepin/developer-center/wiki/Git-Commit-Message-Style)


### git 常用命令（请根据此表单看文档，按使用频率排序）

> 这里是天天用git的人总结的

- 查看系列（不对仓库造成任何变化的）
  - git status
  - git diff
  - git log
  - git branch
- 日常用
  - git commit -am "我是描述"
  - git pull
  - git push
  - git checkout 分支名
  - git add .
- 版本控制用
  - git merge
  - git checkout -b 分支名
  - git reset --hard 版本哈希值
  - git rebase -i 版本哈希值
- 发布版本用
  - git tag -am "我是描述"

### 关于git 配置

> 分成两部分，一部分是git 的用户全局配置，一部分是git 仓库配置。（注：我没听说过git 有系统全局配置，做git 服务器会有）

#### git 的用户全局配置
一般都在这个里`~/.gitconfig`，用`git config --global user.name "John Doe"` 的配置会存在这里

#### git 仓库配置
这个在每个git 仓库里都有，在`.git/config`，这里记录着远程仓库的名称和地址。（注：`origin` 是仓库的默认值。不指定仓库名会使用`origin`仓库）

#### .gitignore
用于不想被控制版本的文件，比如编译后的产物，中间的tmp。。。但要注意已经加入版本控制的文件不受这个文件影响。（可以理解这个是git add 时会发生作用的）

