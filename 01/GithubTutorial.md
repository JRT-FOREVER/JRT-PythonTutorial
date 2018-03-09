Github-Tutorial
=====

## 1.概要
> GitHub是一个面向开发者的远程代码托管仓库，通过GitHub你可以和你的朋友们轻松的分享代码。
>
> Git与GitHub是两种不同的事物，Git是一个**分布式**版本控制系统(就是说Git系统是**去中心化**的，每一个用户都可以**独立**于服务器，在**本地**完成开发工作)。
>
> GitHub提供了一种社会化的开发流程，你可以通过GitHub轻松的实现和其他开发者之间的互动(与他人协作开发，给其他开发者提议或者接受他人意见，了解需求，获得灵感，少造轮子)
## 2.环境搭建

- Windows:
  去官网下载[Git bash](https://git-scm.com/downloads)
- Mac:
  默认安装了Git
- Linux:
  对于大多数发行版，通过软件包获取即可~(目测不需要展开)~
  - debian && Ubuntu && LinuxMint && deepin
  ```sh
  apt install git
  ```

  - archlinux
  ```sh
  pacman -S git
  ```

  - gentoo
  ```sh
  emerge git
  ```

  - contOS
  ```sh
  yum install git
  ```


最后不管你是什么系统，都要注册GitHub账号哦，注册方式很简单这里略过，温馨提示一点，请认真填写您的用户名和邮箱地址，他们真的很有用！

***用户名很重要。请不要乱取！！！***。这里很重要！！！。用户名以后可以更改。所以不用太在意

github的用户名会作为url的一部分，所以对大小写不敏感。如：http://github.com/:你的用户名/:你的仓库名

> 大多数网站用户名都是用正则表达式的 \w 规则，等价于`[A-Za-z0-9_]`　支持字母数字和下划线。github 可以支持连字符 `-`

## 3.配置SSH Key:
GitHub提供了认证SSH公钥的方法访问已有仓库(通过账号密码登录太麻烦)。为了实现SSH登录，需要配置SSH Key:
对于Windows而言，你需要做的是打开安装好的Git bash。然后输入命令:
```sh
ssh-keygen -t rsa -C "your_email@example.com"
```

之后把生成的公钥复制到GitHub相应位置即可(图形操作，这里不赘述)。之后使用下面的命令检验是否配置成功。
```sh
ssh -T git@github.com
```

## 4.配置用户名和邮箱
```sh
git config --global user.name "your_name"
git config --global user.email "your_email"
```
这里要注意的是，如果你想要GitHub能正常统计你的贡献，用户名和邮箱必须和注册账号时的一致。

## 5.gunpg (这个不重要。等你平均每天一次commit再回来看这篇文章)

https://github.com/longtian/gpg-howto



# Github

### 可以申请学生包哦！(学生包用途自己去挖掘)

[https://education.github.com/](https://education.github.com/)

> 懒癌患者可求助万能的某宝


### Github开发者

> 可使用一堆神奇的API。可以做好多事情呐

[https://developer.github.com/](https://developer.github.com/)

