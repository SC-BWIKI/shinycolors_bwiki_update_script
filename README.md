# auto_update_script
sc_bwiki自动化更新脚本
## 特别感谢
数据来自shinycolors.moe站点站长提供，日期和获得方式来自sc日文wiki，bvId来自编辑组成员奥数心白整理。翻译字典来自闪耀色彩汉化插件和部分sc_bwiki编辑组成员。
## 环境要求
基于python 3.12，使用旧版本会报错，用到需要下载的包有requests和BeautifulSoup
下载requests `pip install requests`
下载BeautifulSoup `pip install BeautifulSoup4`
## 文件结构
### 1030030040.json和2020070010.json
  源json文件样例，1开头对应Pcard，2开头对应sCard。
### dic.py
  翻译字典和函数都存在此文件中。
### decode.py
  主要负责P卡和S卡json数据传入后的解码，简化以及输出为luaTable。
### reptile.py
  爬取wikiwiki上的实装日期和获得方法。
### mian.py
  主函数入口，暂未实现，用来拼接现有程序分和mw API编辑部分，实现自动化更新。
## 使用说明
  程序仅供站内自动更新数据和站外人员wiki自动化更新参考学习使用
