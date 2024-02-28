import os
from card import *
from decode import *
from reptile import *
from dic import *

if __name__ == "__main__":
    output_directory = "output"
    p_luaTable = pcardJson_to_luaTable() #接入api只保留这句，p_luaTable就是最终的文本
    s_luaTable = scardJson_to_luaTable() #接入api只保留这句，s_luaTable就是最终的文本
    output_file_path = os.path.join(output_directory, "pCard.txt")
    # 确保output目录存在
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    # 写入文件
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(p_luaTable)
    print(f"内容已写入到{output_file_path}")

    output_file_path2 = os.path.join(output_directory, "sCard.txt")
    # 确保output目录存在
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    # 写入文件
    with open(output_file_path2, "w", encoding="utf-8") as file:
        file.write(s_luaTable)
    print(f"内容已写入到{output_file_path2}")