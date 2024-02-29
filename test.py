from dic import *
data = "[条件:VisualUPが2個以上付与されている場合]\n[確率:20％]\n[最大:2回]"
a = word_translate(enza_skill_senTrans(data,skillSenDic,enza_skill_str),skillWordDic)
print(a)

# import re

# # 假设的restored_text文本
# restored_text = "这是一个包含$1和$2的字符串: $1, $2, $3$4, $5$6, $7, $8"

# # 使用正则表达式查找所有形如$1, $2的元素
# dollar_items = re.findall(r'\$(\d+)', restored_text)

# # 检查是否有重复的元素，并进行调整
# adjusted_dollar_items = []
# adjustment = 0
# for item in dollar_items:
#     if dollar_items.count(item) > 1 and item not in adjusted_dollar_items:
#         # 如果当前元素重复且未处理过，增加调整量
#         adjustment += 1
#     # 如果已经有调整量，增加当前元素的数值
#     new_value = int(item) + adjustment
#     adjusted_dollar_items.append(f"${new_value}")

# # 生成新的文本
# adjusted_text = restored_text
# for original, new in zip(re.findall(r'\$\d+', restored_text), adjusted_dollar_items):
#     adjusted_text = adjusted_text.replace(original, new, 1)

# # 输出调整后的文本
# adjusted_text
