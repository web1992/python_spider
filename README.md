### python_spider
Python spider 爬虫抓取`<谍影重重5>`豆瓣影评

> 参考的文章： [https://github.com/Andrew-liu/Dou_Ban_Spider](https://github.com/Andrew-liu/Dou_Ban_Spider)
>

### 本文地址：
[https://github.com/web1992/python_spider](https://github.com/web1992/python_spider)

### 说明

`<谍影重重5>` 影评截止2016-08-31 10:28:00 有大约`26000`条影评

爬虫抓取，每次每页20条数据，考虑到豆瓣有对机器人屏蔽的限制，实际抓取电影评论的时候会进行时间间隔的控制

### 使用说明

在获取豆瓣的影评时，当页数过多时，需要用户登陆，才能继续访问，所以使用 gen_login_cookie.py 生成登陆cookie，模式登陆

- 1, 注册豆瓣账号
- 2, 使用 gen_login_cookie.py 进行手机验证码方式的登陆
- 3, 执行 douban_JasonBourne_spider.py 获取所有的电影评论
- 4, 查看 douban_JasonBourne_yingping.txt 中的电影评论
- 5, 待续...

### 其他
可使用以下命令对影评进行 简单的统计，可统计出5星好评，4星评论，3星评论 ... 的比例

	# 评论统计
    cat douban_JasonBourne_yingping.txt  |awk -F'\t' '{print $1}' |sort |uniq -c
	# 总记录数
	cat douban_JasonBourne_yingping.txt  |wc -l

> 输出

      9 0
     14 10
     27 20
    112 30
    116 40
     22 50

5星好评的有22个，4星评论的有116 个，以此类推，总统计评论数= `9+14+27+112+116+22`

说明：
>50 力荐
>40 推荐
>30 还行
>20 较差
>10 很差
>0  没有进行星星评论



