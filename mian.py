import os
import json
from card import *
from decode import *
from reptile import *

def read_json_files_from_directory(directory):
    # 存储所有JSON文件内容的列表
    json_contents = []
    
    # 确保目录存在
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return json_contents

    # 遍历指定目录
    for filename in os.listdir(directory):
        # 检查文件是否为JSON文件
        if filename.endswith(".json"):
            # 构造完整的文件路径
            file_path = os.path.join(directory, filename)
            # 打开并读取JSON文件内容
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    json_contents.append(data)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                
    return json_contents

if __name__ == "__main__":
    #P卡部分
    web_p_data = p_card_reptile()
    p_luaTable = 'local p ={\n'
    file_list = read_json_files_from_directory('pCard') #传入json字符串数组，需要解析迷糊程序的接口down本地用file加载或者直接调用内存
    for p_data in file_list:
        decode_data = pCardDecode(p_data)
        decode_data["date"] = ""
        decode_data["get_med"] = ""
        for j in web_p_data:
            if j["cardname"] == decode_data['name']:
                decode_data['get_med'] = word_translate(j["get_med"],get_medDic)
                decode_data['date'] = j["date"]
            else:
                continue
        p_luaTable += pCard_to_luaTable(decode_data)
        p_luaTable += ',\n'
    p_luaTable += '}\n'
    p_luaTable += 'return p' #此处p_luaTable就是最后的数据库lua代码文本，需要通过接口把此字符串变量传到 模块:P卡数据库内容
    # 指定output目录相对于当前脚本的路径
    output_directory = "output"
    output_file_path = os.path.join(output_directory, "pCard.txt")

    # 确保output目录存在
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 写入文件
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(p_luaTable)

    print(f"内容已写入到{output_file_path}")

    #S卡部分
    web_s_data = s_card_reptile()
    s_luaTable = 'local p ={\n'
    file_list2 = read_json_files_from_directory('sCard') #传入json字符串数组，需要解析迷糊程序的接口down本地用file加载或者直接调用内存
    for s_data in file_list2:
        decode_sdata = sCardDecode(s_data)
        decode_sdata["date"] = ""
        decode_sdata["get_med"] = ""
        for j in web_s_data:
            if j["cardname"] == decode_sdata['name']:
                decode_sdata['get_med'] = word_translate(j["get_med"],get_medDic)
                decode_sdata['date'] = j["date"]
            else:
                continue
        s_luaTable += sCard_to_luaTable(decode_sdata)
        s_luaTable += '\n'
    s_luaTable += '}\n'
    s_luaTable += 'return p' #此处s_luaTable就是最后的数据库lua代码文本，需要通过接口把此字符串变量传到 模块:S卡数据库内容
    output_file_path2 = os.path.join(output_directory, "sCard.txt")

    # 确保output目录存在
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 写入文件
    with open(output_file_path2, "w", encoding="utf-8") as file:
        file.write(s_luaTable)

    print(f"内容已写入到{output_file_path2}")