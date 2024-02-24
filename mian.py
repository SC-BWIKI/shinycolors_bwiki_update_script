import json
from card import *
from decode import *
from reptile import *
if __name__ == "__main__":
    # with open('1040250010.json', 'r') as file:
    #     a = pCardDecode(file)
    # print(a)
    #P卡部分
    web_p_data = p_card_reptile()
    p_luaTable = 'local p ={'
    file_list = [] #传入json字符串数组，需要解析迷糊程序的接口down本地用file加载或者直接调用内存
    for i in file_list:
        p_data = pCardDecode(file_list[i])
        for j in web_p_data:
            if web_p_data[j]["name"] == p_data.name:
                p_data.get_med = web_p_data[j]["get_med"]
                p_data.date = web_p_data[j]["date"]
            else:
                continue
        p_luaTable += pCard_to_luaTable(p_data)
        p_luaTable += ',\n'
    p_luaTable += '}'
    p_luaTable += 'return p' #此处p_luaTable就是最后的数据库lua代码文本，需要通过接口把此字符串变量传到 模块:P卡数据库内容

    #S卡部分
    web_s_data = s_card_reptile()
    s_luaTable = 'local p ={'
    file_list2 = [] #传入json字符串数组，需要解析迷糊程序的接口down本地用file加载或者直接调用内存
    for i in file_list2:
        s_data = sCardDecode(file_list2[i])
        for j in web_s_data:
            if web_s_data[j]["name"] == s_data.name:
                s_data.get_med = web_s_data[j]["get_med"]
                s_data.date = web_s_data[j]["date"]
            else:
                continue
        s_luaTable += sCard_to_luaTable(s_data)
        s_luaTable += ',\n'
    s_luaTable += '}'
    s_luaTable += 'return p' #此处p_luaTable就是最后的数据库lua代码文本，需要通过接口把此字符串变量传到 模块:P卡数据库内容