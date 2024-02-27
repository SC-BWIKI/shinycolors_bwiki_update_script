# auto_update_script
wiki自动化更新脚本
## 文件结构
### card.py
  程序暂时作废，封装成类的代码块。（缺少此文件不影响运行）
### dic.py
  翻译字典都存在此文件中。
### decode.py
  主要负责P卡和S卡json数据传入后的解码，简化以及输出位luaTable程序
### reptile.py
  爬取wikiwiki上的实装日期和获得方法
### mian.py
  主函数入口，目前是遍历pCard文件夹和sCard文件夹下的所有json文件转换成luaTable后输出到/output目录，后续将封装进decode，然后入口用来拼接现有程序和json爬取部分和mw API编辑部分。
