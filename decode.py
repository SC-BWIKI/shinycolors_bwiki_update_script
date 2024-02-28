import json
import re
import os
from card import *
from dic import *
from reptile import *

def pCardDecode(pCardata):
    #除Bvid、获得方式外的其他属性转换字典传递
    data = {"envApt":{},"musicApt":{},"pfmApt":{},"memoryAppeals":[],"skillPanels":[]}
    data['name'] = word_translate(pCardata['idol']['name'].replace(" ",""),nameDic)
    data['uid']= pCardata['idol']['id']
    data['unit'] = word_translate(pCardata['idol']['character']['unit']['name'],unitDic)
    data['rarity'] = pCardata['idol']['rarity']
    #三种适性
    data['envApt']['fine']= pCardata['environmentAptitudes'][0]['stepName']
    data['envApt']['sunny']= pCardata['environmentAptitudes'][1]['stepName']
    data['envApt']['cloudy']= pCardata['environmentAptitudes'][2]['stepName']
    data['envApt']['rain']= pCardata['environmentAptitudes'][3]['stepName']
    musicApt = ["cute","cool","positive","relax","emotional"]
    j = 0
    for i in musicApt :
        if j < len(pCardata['musicStyleAptitudes']):
            data['musicApt'][i] = pCardata['musicStyleAptitudes'][j]['stepName']
            j += 1
    pfmApt = ["high","medium","slow"]
    j = 0
    for i in pfmApt :
        if j < len(pCardata['performanceAptitudes']):
            data['pfmApt'][i] = pCardata['performanceAptitudes'][j]['stepName']
            j += 1
    #回忆炸弹部分
    for i in range(len(pCardata['idol']['memoryAppeals'])):
        a = {"level":pCardata['idol']['memoryAppeals'][i]['level'],"name":word_translate(pCardata['idol']['memoryAppeals'][i]['name'],skillWordDic),
             "comment":word_translate(pCardata['idol']['memoryAppeals'][i]['comment'],skillWordDic)}
        data['memoryAppeals'].append(a)
    #技能盘部分
    for i in range(len(pCardata['idol']['skillPanels'])):
        sequence = pCardata['idol']['skillPanels'][i]['sequence'] #技能所在位置从右往左数的位置
        step = pCardata['idol']['skillPanels'][i]['step'] #技能所在位置的层数，从上到下
        name = word_translate(pCardata['idol']['skillPanels'][i]['skill']['name'],skillWordDic) 
        if pCardata['idol']['skillPanels'][i]['skillCategory'] == "passive":
            comment = word_translate(enza_skill_senTrans(pCardata['idol']['skillPanels'][i]['skill']['comment'],skillSenDic,enza_skill_str),skillWordDic) 
        elif pCardata['idol']['skillPanels'][i]['skillCategory'] == "limit_break":
            comment = pCardata['idol']['skillPanels'][i]['skill']['comment'] 
        else:
            comment = word_translate(pCardata['idol']['skillPanels'][i]['skill']['comment'],skillWordDic) 
        if pCardata['idol']['skillPanels'][i]['skill']['skillEffects'][0]['attribute'] == "vocal":
            color = "#ff8c94"
        elif pCardata['idol']['skillPanels'][i]['skill']['skillEffects'][0]['attribute']  == "dance":
            color = "#91eeff"
        elif pCardata['idol']['skillPanels'][i]['skill']['skillEffects'][0]['attribute']  == "visual":
            color = "#ffcf91"
        else:
            color = "#ffffff"
        a = {"sequence":sequence,"step":step,"name":name,"comment":comment,"color":color}
        data['skillPanels'].append(a)
    return data
        
def sCardDecode(sCardata):
    #sCardata = json.load(cardata)
    data = {}
    #基础资料部分
    data['name'] = word_translate(sCardata['supportIdol']['name'],nameDic)
    data['uid']= sCardata['supportIdolId']
    data['rarity'] = sCardata['supportIdol']['rarity']
    data['unit']= word_translate(sCardata['supportIdol']['character']['unit']['name'],unitDic)
    data['inspirationAttribute'] = sCardata['inspirationAttribute']
    data['ideaMark'] = sCardata['supportIdol']['ideaMark']
    data['musicSupportProficiencyBonuses'] = []
    for i in range(len(sCardata['musicSupportProficiencyBonuses'])):
        a = {"proficiency":sCardata['musicSupportProficiencyBonuses'][i]['proficiency'],"value":sCardata['musicSupportProficiencyBonuses'][i]['value']}
        data['musicSupportProficiencyBonuses'].append(a)
    defaultVocalBonus = sCardata['supportIdol']['defaultVocalBonus']
    defaultDanceBonus = sCardata['supportIdol']['defaultDanceBonus']
    defaultVisualBonus = sCardata['supportIdol']['defaultVisualBonus']
    defaultMentalBonus = sCardata['supportIdol']['defaultMentalBonus']
    middleVocalBonus = sCardata['supportIdol']['middleVocalBonus']
    middleDanceBonus = sCardata['supportIdol']['middleDanceBonus']
    middleVisualBonus = sCardata['supportIdol']['middleVisualBonus']
    middleMentalBonus = sCardata['supportIdol']['middleMentalBonus']
    maxVocalBonus = sCardata['supportIdol']['maxVocalBonus']
    maxDanceBonus = sCardata['supportIdol']['maxDanceBonus']
    maxVisualBonus = sCardata['supportIdol']['maxVisualBonus']
    maxMentalBonus = sCardata['supportIdol']['maxMentalBonus']
    data['bonus'] = {"defaultVocalBonus":defaultVocalBonus,"defaultDanceBonus":defaultDanceBonus,"defaultVisualBonus":defaultVisualBonus,"defaultMentalBonus":defaultMentalBonus,
                  "middleVocalBonus":middleVocalBonus,"middleDanceBonus":middleDanceBonus,"middleVisualBonus":middleVisualBonus,"middleMentalBonus":middleMentalBonus,
                  "maxVocalBonus":maxVocalBonus,"maxDanceBonus":maxDanceBonus,"maxVisualBonus":maxVisualBonus,"maxMentalBonus":maxMentalBonus}
    data['produceSupportIdolEvents'] = []
    for i in range(len(sCardata['supportIdol']['produceSupportIdolEvents'])):
        envet_name = sCardata['supportIdol']['produceSupportIdolEvents'][i]['eventCategoryName']
        envet_vocal = sCardata['supportIdol']['produceSupportIdolEvents'][i]['eventParam']['vocal']
        envet_dance = sCardata['supportIdol']['produceSupportIdolEvents'][i]['eventParam']['dance']
        envet_visual = sCardata['supportIdol']['produceSupportIdolEvents'][i]['eventParam']['visual']
        envet_mental = sCardata['supportIdol']['produceSupportIdolEvents'][i]['eventParam']['mental']
        envet_skillPoint= sCardata['supportIdol']['produceSupportIdolEvents'][i]['eventParam']['skillPoint']
        a = {"name":envet_name,"vocal":envet_vocal,"dance":envet_dance,"visual":envet_visual,"mental":envet_mental,"SP":envet_skillPoint}
        data['produceSupportIdolEvents'].append(a)
    data['fightSkill'] = {"name":sCardata['supportIdol']['fightSkill']['name'],"comment":sCardata['supportIdol']['fightSkill']['comment']}
    data['supportSkills'] = []
    for i in range(len(sCardata['supportSkills'])):
        s_skill_name = word_translate(sCardata['supportSkills'][i]['name'],supSkillDic)
        s_skill_description = word_translate(sCardata['supportSkills'][i]['name'],supSkillValueDic)
        if sCardata['supportSkills'][i]['name'] == "おやすみブースト" or sCardata['supportSkills'][i]['name'] == "トラブルガード":
            s_skill_value = str(sCardata['supportSkills'][i]['supportSkillEffect']['value'])
            s_skill_final = s_skill_description + str(s_skill_value)
        elif  sCardata['supportSkills'][i]['name'] == "体力サポート":
            s_skill_value = str(sCardata['supportSkills'][i]['supportSkillEffect']['value'])
            s_skill_final = s_skill_description + s_skill_value + "%"
        else:
            s_skill_final  = s_skill_description
        s_skill_levelData = []
        for j in range(len(sCardata['supportIdol']['supportSkills'])):
            if sCardata['supportIdol']['supportSkills'][j]['name'] == sCardata['supportSkills'][i]['name']:
                s_skill_level = sCardata['supportIdol']['supportSkills'][j]['supportSkillEffect']['supportSkillLevel']
                s_skill_card_level = sCardata['supportIdol']['supportSkills'][j]['level']
                s_skill_levelData.append({"cardLevel":s_skill_card_level,"skillLevel":s_skill_level})
                #s_skill_levelData["level" + str(s_skill_card_level)] = str(s_skill_level)
            else:
                continue
        a = {"name":s_skill_name,"description":s_skill_final,"value":s_skill_levelData}
        data['supportSkills'].append(a)
    data['supportIdolActiveSkill'] = []
    for i in range(len(sCardata['supportIdol']['supportIdolActiveSkill']['activeSkills'])):
        saSkill_name = word_translate(sCardata['supportIdol']['supportIdolActiveSkill']['activeSkills'][i]['name'],skillWordDic)
        saSkill_comment = word_translate(sCardata['supportIdol']['supportIdolActiveSkill']['activeSkills'][i]['comment'],skillWordDic)
        sakill = {"name":saSkill_name,"comment":saSkill_comment}
        data['supportIdolActiveSkill'].append(sakill)
    data['skillPanels'] = []
    for i in range(len(sCardata['supportIdol']['skillPanels'])):
        sequence = sCardata['supportIdol']['skillPanels'][i]['sequence']
        step = sCardata['supportIdol']['skillPanels'][i]['step']
        name = word_translate(sCardata['supportIdol']['skillPanels'][i]['skill']['name'],skillWordDic)
        comment = word_translate(sCardata['supportIdol']['skillPanels'][i]['skill']['comment'],skillWordDic)
        if sCardata['supportIdol']['skillPanels'][i]['skill']['skillEffects'][0]['attribute'] == "vocal":
            color = "#ff8c94"
        elif sCardata['supportIdol']['skillPanels'][i]['skill']['skillEffects'][0]['attribute'] == "dance":
            color = "#91eeff"
        elif sCardata['supportIdol']['skillPanels'][i]['skill']['skillEffects'][0]['attribute']== "visual":
            color = "#ffcf91"
        else:
            color = "#ffffff"
        a = {"sequence":sequence,"step":step,"name":name,"comment":comment,"color":color}
        data['skillPanels'].append(a)
    return data

def pCard_to_luaTable(card):
    lua_table = f'["{card['name']}"]'+' = {'
    #lua_table += f'name = "{card['name']}", '
    lua_table += f'uid = "{card['uid']}", '
    lua_table += f'unit = "{card['unit']}", '
    lua_table += f'rarity = "{card['rarity']}", '
    if len(card['date']) > 0:
        lua_table += f'date = "{card['date']}", '
    lua_table += f'get_med = "{card['get_med']}", '
    # Memory Appeals
    lua_table += "memoryAppeals = {"
    memory_appeals = []
    for appeal in card['memoryAppeals']:
        appeal_str = "level" + f'{appeal['level']} '+ " = {"
        #appeal_str += f"level = {appeal['level']}, "
        appeal_str += f'name = "{appeal['name']}", '
        appeal_str += f'comment = "{appeal['comment']}"'
        appeal_str += "}"
        memory_appeals.append(appeal_str)
    lua_table += ', '.join(memory_appeals) + "}, "
    
    # Skill Panels
    lua_table += "skillPanels = {"
    skill_panels = []
    for panel in card['skillPanels']:
        panel_str = f"['skill"+f"{panel['step']}"+"-"+f"{panel['sequence']}"+"']={"
        panel_str += f'name = "{panel['name']}", '
        panel_str += f'comment = "{panel['comment']}",'
        panel_str += f'color = "{panel['color']}"'
        panel_str += "}"
        skill_panels.append(panel_str)
    lua_table += ', '.join(skill_panels) + "}"
    lua_table += '}'
    return lua_table

def sCard_to_luaTable(card):
    lua_table = f'["{card['name']}"]'+' = {'
    lua_table += f'uid = "{card['uid']}",'
    lua_table += f'rarity = "{card['rarity']}",'
    lua_table += f'unit = "{card['unit']}",'
    lua_table += f'date = "{card['date']}",'
    lua_table += f'get_med = "{card['get_med']}",'
    lua_table += f'inspirationAttribute = "{card['inspirationAttribute']}",'
    lua_table += f'ideaMark = "{card['ideaMark']}",'
    lua_table += "musicSupportProficiencyBonuses = {"
    musicSupportProficiencyBonuses = []
    for bonuses in card['musicSupportProficiencyBonuses']:
        bonuses_str = "{"
        bonuses_str += f'proficiency = "{bonuses['proficiency']}",'
        bonuses_str += f'value = "{bonuses['value']}"'
        bonuses_str += "}"
        musicSupportProficiencyBonuses.append(bonuses_str)
    lua_table += ', '.join(musicSupportProficiencyBonuses) + "},"
    # bonus
    lua_table += "bonus = {"
    lua_table  += f'defaultVocalBonus = "{card['bonus']['defaultVocalBonus']}", '
    lua_table += f'defaultDanceBonus = "{card['bonus']['defaultDanceBonus']}", '
    lua_table  += f'defaultVisualBonus = "{card['bonus']['defaultVisualBonus']}", '
    lua_table  += f'defaultMentalBonus = "{card['bonus']['defaultMentalBonus']}", '
    lua_table  += f'middleVocalBonus = "{card['bonus']['middleVocalBonus']}", '
    lua_table  += f'middleDanceBonus = "{card['bonus']['middleDanceBonus']}", '
    lua_table  += f'middleVisualBonus = "{card['bonus']['middleVisualBonus']}", '
    lua_table  += f'middleMentalBonus = "{card['bonus']['middleMentalBonus']}", '
    lua_table  += f'maxVocalBonus = "{card['bonus']['maxVocalBonus']}", '
    lua_table  += f'maxDanceBonus = "{card['bonus']['maxDanceBonus']}", '
    lua_table  += f'maxVisualBonus = "{card['bonus']['maxVisualBonus']}", '
    lua_table  += f'maxMentalBonus = "{card['bonus']['maxMentalBonus']}" '
    lua_table += "},"
   # produceSupportIdolEvents
    lua_table += "produceSupportIdolEvents = {"
    produceSupportIdolEvents = []
    for event in card['produceSupportIdolEvents']:
        event_str = "{" 
        event_str += f'name = "{event['name']}",' 
        event_str += f'vocal = "{event['vocal']}",'
        event_str += f'dance = "{event['dance']}",'
        event_str += f'visual = "{event['visual']}",'
        event_str += f'mental = "{event['mental']}",'
        event_str += f'SP = "{event['SP']}"'
        event_str += "},"
        produceSupportIdolEvents.append(event_str)
    lua_table += ' '.join(produceSupportIdolEvents).rstrip(', ') + "},"  
    # fightSkill
    lua_table += "fightSkill = {"
    lua_table += f'name= "{card['fightSkill']['name']}",'  
    lua_table += f'comment= "{card['fightSkill']['comment']}"'  
    lua_table += "},"
    # supportSkills
    lua_table += "supportSkills = {"
    supportSkill = []
    supportSkill_num = 0
    for supSkill in card['supportSkills']:
        supSkill_str = "{"
        supSkill_str += f'name = "{supSkill['name']}",'
        supSkill_str += f'description = "{supSkill['description']}",'
        supSkill_str += "value = {"
        for index, supSkill_value in enumerate(card['supportSkills'][supportSkill_num]['value']):
            supSkill_value_str = "{"
            supSkill_value_str += f'cardLevel = "{supSkill_value['cardLevel']}",'
            supSkill_value_str += f'skillLevel = "{supSkill_value['skillLevel']}"'
            # 判断当前项是否为列表中的最后一项
            if index == len(card['supportSkills'][supportSkill_num]['value']) - 1:
                # 如果是最后一项，执行特定操作，例如添加特定的字符串
                supSkill_value_str += "}"
            else:
                supSkill_value_str += "},"
            supSkill_str += supSkill_value_str
        supSkill_str += "}}"
        supportSkill_num += 1
        supportSkill.append(supSkill_str)
    lua_table += ', '.join(supportSkill) + "},"
    # supportIdolActiveSkill
    lua_table += "supportIdolActiveSkill = {"
    supportIdolActiveSkill = []
    for saSkill in card['supportIdolActiveSkill']:
        saSkill_str = "{"
        saSkill_str += f'name = "{saSkill['name']}",'
        saSkill_str += f'comment = "{saSkill['comment']}"'
        saSkill_str += "}"
        supportIdolActiveSkill.append(saSkill_str)
    lua_table += ', '.join(supportIdolActiveSkill) + "},"
    # Skill Panels
    lua_table += "skillPanels = {"
    skill_panels = []
    for panel in card['skillPanels']:
        panel_str = "{"
        # panel_str += f"sequence = {panel['sequence']}, "
        # panel_str += f"step = {panel['step']}, "
        panel_str = f"['skill"+f"{panel['step']}"+"-"+f"{panel['sequence']}"+"']={"
        panel_str += f'name = "{panel['name']}",'
        panel_str += f'comment = "{panel['comment']}",'
        panel_str += f'color = "{panel['color']}"'
        panel_str += "}"
        skill_panels.append(panel_str)
    lua_table += ', '.join(skill_panels) + "}"
    lua_table += '},'
    return lua_table

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

def pcardJson_to_luaTable():
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
    return p_luaTable
    
def scardJson_to_luaTable():
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
    return s_luaTable