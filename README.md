# Chem-QQBot
使用python-Flask框架，自建框架使用正反向htyp与go-cqHttp程序通信
新人自研，有问题请联系QQ：3254806570 - 非诚勿扰

# 已实现功能：

# 框架提供的函数API
## add()
使用add() - Hook函数 来注册命令事件，与plugins下的插件模块交互

# API命令目录
基础：/表示命令，#分隔符后表示参数
/ls
获取所有可用命令

## /help#[具体命令名称]
获取帮助
示例：
/help
/help#tqh
/ls
获取所有可用命令

## /jwc
获取教务处最新通知

## /tqh#[地点]#[小时数n]
查询中国某地(市级单位)未来n小时的天气预报
最多支持24h，默认查询西安市
示例：
/tqh#拉萨#4
/tqh#西宁
/tqh

## /tqd#[地点]#[天数n]
查询中国某地(市级单位)未来n天的天气预报
最多支持15天
示例：
/tqd#拉萨#4
/tqd#西宁
/tqd

## /nl#[日期date]
查询某日的日期，公历+农历，默认查今天日期
日期的表示方式有
date=’2020/2/2‘：查询具体某一天
date为负数时查询从查询日期倒退的那天
date为正时查询从查询日起未来的那天
示例：
/nl
/nl#-2
/nl#2
/nl#2023/5/1

## /fy#[词语]
翻译词语，中文和英文互译，自动检测。仅对单词和部分短语有效，无法翻译长句

## /rs#[热搜条数n]
查询微博热搜前n条，默认10条，最多50条
示例：
/rs
/rs#2



