import json
from card import *
from dic import *
def dic_sort(dic):
    dic = sorted(dic.items(),key=lambda item:len(item[0]),reverse=True)
    return dic

def word_translate (data,dic):
    sorted_items = dic_sort(dic)
    for key, value in sorted_items:
        data = data.replace(key, value)
    return data

def sentence_translate(data,dic):
    dic = dic_sort(dic)
    pass

def pCardDecode(cardata):
    #除Bvid、获得方式外的其他属性转换字典传递
    pCardata = json.load(cardata)
    data = pCard()
    data.name = word_translate (pCardata.idol.name,nameDic)
    data.uid = pCardata.idol.id
    data.unit = word_translate(pCardata.idol.character.unit.name,unitDic)
    data.rarity = pCardata.idol.rarity 
    data.memoryAppeals = []
    data.skillPanels = []
    #三种适性
    envApt = ["fine","sunny","cloudy","rain"]
    j = 0
    for i in envApt:
        if j < len(pCardata.environmentAptitudes):
            data.envApt = {i:pCardata.environmentAptitudes[j].stepName}
            j += 1
    musicApt = ["cute","cool","positive","relax","emotional"]
    j = 0
    for i in musicApt :
        if j < len(pCardata.musicStyleAptitudes):
            data.musicApt = {i:pCardata.musicStyleAptitudes[j].stepName}
            j += 1
    pfmApt = ["high","medium","slow"]
    j = 0
    for i in pfmApt :
        if j < len(pCardata.performanceAptitudes):
            data.pfmApt = {i:pCardata.performanceAptitudes[j].stepName}
            j += 1
    #回忆炸弹部分
    for i in range(len(pCardata.idol.memoryAppeals)):
        a = {"level":pCardata.idol.memoryAppeals[i].level,"name":word_translate(sentence_translate(pCardata.idol.memoryAppeals[i].name,skillSenDic),skillWordDic),
             "comment":word_translate(sentence_translate(pCardata.idol.memoryAppeals[i].comment,skillSenDic),skillWordDic)}
        data.memoryAppeals.append(a)
    #技能盘部分
    for i in range(len(pCardata.idol.skillPanels)):
        sequence = pCardata.idol.skillPanels[i].sequence
        step = pCardata.idol.skillPanels[i].step
        name = word_translate(sentence_translate(pCardata.idol.skillPanels[i].skill.name,skillSenDic),skillWordDic)
        comment = word_translate(sentence_translate(pCardata.idol.skillPanels[i].skill.comment,skillSenDic),skillWordDic)
        if pCardata.idol.skillPanels[i].skill.skillEffects.attribute == "vocal":
            color = "#ff8c94"
        elif pCardata.idol.skillPanels[i].skill.skillEffects.attribute == "dance":
            color = "#91eeff"
        elif pCardata.idol.skillPanels[i].skill.skillEffects.attribute == "visual":
            color = "#ffcf91"
        else:
            color = "#ffffff"
        a = {"sequence":sequence,"step":step,"name":name,"comment":comment,"color":color}
        data.skillPanels.append(a)
    return data
        
def sCardDecode(cardata):
    sCardata = json.load(cardata)
    data = sCard()
    data.name = word_translate(sCardata.supportIdol.name,nameDic)
    data.uid = sCardata.supportIdolId
    data.rarity = sCardata.supportIdol.rarity
    data.unit = word_translate(sCardata.supportIdol.character.unit.name,unitDic)
    data.inspirationAttribute = sCardata.inspirationAttribute
    data.ideaMark = sCardata.supportIdol.ideaMark
    data.musicSupportProficiencyBonuses = []
    for i in range(len(sCardata.musicSupportProficiencyBonuses)):
        a = {"proficiency":sCardata.musicSupportProficiencyBonuses[i].proficiency,"value":sCardata.musicSupportProficiencyBonuses[i].value}
        data.musicSupportProficiencyBonuses.append(a)
    defaultVocalBonus = sCardata.supportIdol.defaultVocalBonus
    defaultDanceBonus = sCardata.supportIdol.defaultDanceBonus
    defaultVisualBonus = sCardata.supportIdol.defaultVisualBonus
    defaultMentalBonus = sCardata.supportIdol.defaultMentalBonus
    middleVocalBonus = sCardata.supportIdol.middleVocalBonus 
    middleDanceBonus = sCardata.supportIdol.middleDanceBonus
    middleVisualBonus = sCardata.supportIdol.middleVisualBonus
    middleMentalBonus = sCardata.supportIdol.middleMentalBonus
    maxVocalBonus = sCardata.supportIdol.maxVocalBonus
    maxDanceBonus = sCardata.supportIdol.maxDanceBonus
    maxVisualBonus = sCardata.supportIdol.maxVisualBonus
    maxMentalBonus = sCardata.supportIdol.maxMentalBonus
    data.bonus = {"defaultVocalBonus":defaultVocalBonus,"defaultDanceBonus":defaultDanceBonus,"defaultVisualBonus":defaultVisualBonus,"defaultMentalBonus":defaultMentalBonus,
                  "middleVocalBonus":middleVocalBonus,"middleDanceBonus":middleDanceBonus,"middleVisualBonus":middleVisualBonus,"middleMentalBonus":middleMentalBonus,
                  "maxVocalBonus":maxVocalBonus,"maxDanceBonus":maxDanceBonus,"maxVisualBonus":maxVisualBonus,"maxMentalBonus ":maxMentalBonus}
    data.produceSupportIdolEvents = []
    for i in range(len(sCardata.supportIdol.produceSupportIdolEvents)):
        envet_name = sCardata.supportIdol.produceSupportIdolEvents[i].eventCategoryName
        envet_vocal = sCardata.supportIdol.produceSupportIdolEvents[i].eventParam.vocal
        envet_dance = sCardata.supportIdol.produceSupportIdolEvents[i].eventParam.dance
        envet_visual = sCardata.supportIdol.produceSupportIdolEvents[i].eventParam.visual
        envet_mental = sCardata.supportIdol.produceSupportIdolEvents[i].eventParam.mental
        envet_skillPoint= sCardata.supportIdol.produceSupportIdolEvents[i].eventParam.skillPoint
        a = {"name":envet_name,"vocal":envet_vocal,"dance":envet_dance,"visual":envet_visual,"mental":envet_mental,"SP":envet_skillPoint}
        data.produceSupportIdolEvents.append(a)
    data.fightSkill = {"name":sCardata.supportIdol.fightSkill.name,"comment":sCardata.supportIdol.fightSkill.comment}
    data.supportSkills = []
    for i in range(len(sCardata.supportSkills)):
        s_skill_name = word_translate(sCardata.supportSkills[i].name,supSkillDic)
        s_skill_description = word_translate(sCardata.supportSkills[i].name,supSkillValueDic)
        if sCardata.supportSkills[i].name == "おやすみブースト" or sCardata.supportSkills[i].name == "トラブルガード":
            s_skill_value = sCardata.supportSkills[i].supportSkillEffect.value
            s_skill_final = s_skill_description + s_skill_value
            data.supportSkills.append(s_skill_final)
        elif  sCardata.supportSkills[i].name == "体力サポート":
            s_skill_value = sCardata.supportSkills[i].supportSkillEffect.value
            s_skill_final = s_skill_description + s_skill_value + "%"
        else:
            s_skill_final  = s_skill_description
        s_skill_levelData = {}
        for j in range(len(sCardata.supportIdol.supportSkills)):
            if sCardata.supportIdol.supportSkills.name == sCardata.supportSkills.name:
                s_skill_level = sCardata.supportIdol.supportSkills.supportSkillLevel
                s_skill_levelData = {"level" + s_skill_level:s_skill_level}
            else:
                continue
        a = {"name":s_skill_name,"description":s_skill_final,"value":s_skill_levelData}
        data.supportSkills.append(a)
    data.supportIdolActiveSkill = []
    for i in range(len(sCardata.supportIdol.supportIdolActiveSkill.activeSkills)):
        saSkill_name = word_translate(sentence_translate(sCardata.supportIdol.supportIdolActiveSkill.activeSkills[i].name,skillSenDic),skillWordDic)
        saSkill_comment = word_translate(sentence_translate(sCardata.supportIdol.supportIdolActiveSkill.activeSkills[i].comment,skillSenDic),skillWordDic)
        sakill = {"name":saSkill_name,"comment":saSkill_comment}
        data.supportIdolActiveSkill.append(sakill)
    data.skillPanels = []
    for i in range(len(sCardata.supportIdol.skillPanels)):
        sequence = sCardata.supportIdol.skillPanels[i].sequence
        step = sCardata.supportIdol.skillPanels[i].step
        name = word_translate(sentence_translate(sCardata.supportIdol.skillPanels[i].skill.name,skillSenDic),skillWordDic)
        comment = word_translate(sentence_translate(sCardata.supportIdol.skillPanels[i].skill.comment,skillSenDic),skillWordDic)
        if sCardata.supportIdol.skillPanels[i].skill.skillEffects.attribute == "vocal":
            color = "#ff8c94"
        elif sCardata.supportIdol.skillPanels[i].skill.skillEffects.attribute == "dance":
            color = "#91eeff"
        elif sCardata.supportIdol.skillPanels[i].skill.skillEffects.attribute == "visual":
            color = "#ffcf91"
        else:
            color = "#ffffff"
        a = {"sequence":sequence,"step":step,"name":name,"comment":comment,"color":color}
        data.skillPanels.append(a)
    return data

def pCard_to_luaTable(card):
    lua_table = '{'
    lua_table += f"name = '{card.name}', "
    lua_table += f"uid = {card.uid}, "
    lua_table += f"unit = '{card.unit}', "
    lua_table += f"rarity = '{card.rarity}', "
    lua_table += f"date = '{card.date}', "
    lua_table += f"get_med = '{card.get_med}', "
    # Memory Appeals
    lua_table += "memoryAppeals = {"
    memory_appeals = []
    for appeal in card.memoryAppeals:
        appeal_str = "{"
        appeal_str += f"level = {appeal['level']}, "
        appeal_str += f"name = '{appeal['name']}', "
        appeal_str += f"comment = '{appeal['comment']}'"
        appeal_str += "}"
        memory_appeals.append(appeal_str)
    lua_table += ', '.join(memory_appeals) + "}, "
    
    # Skill Panels
    lua_table += "skillPanels = {"
    skill_panels = []
    for panel in card.skillPanels:
        panel_str = "{"
        panel_str += f"sequence = {panel['sequence']}, "
        panel_str += f"step = {panel['step']}, "
        panel_str += f"name = '{panel['name']}', "
        panel_str += f"comment = '{panel['comment']}'"
        panel_str += f"color = '{panel['color']}'"
        panel_str += "}"
        skill_panels.append(panel_str)
    lua_table += ', '.join(skill_panels) + "}"
    lua_table += '}'
    return lua_table

def sCard_to_luaTable(card):
    lua_table = '{'
    lua_table += f"name = '{card.name}',"
    lua_table += f"uid = {card.uid},"
    lua_table += f"rarity = '{card.rarity}',"
    lua_table += f"unit = '{card.unit}',"
    lua_table += f"date = '{card.date}', "
    lua_table += f"get_med = '{card.get_med}', "
    lua_table += f"inspirationAttribute = '{card.inspirationAttribute}',"
    lua_table += f"ideaMark = '{card.ideaMark}',"
    # musicSupportProficiencyBonuses
    lua_table += "musicSupportProficiencyBonuses = {"
    musicSupportProficiencyBonuses = []
    for bonuses in card.musicSupportProficiencyBonuses:
        bonuses_str = "{"
        bonuses_str += f"proficiency = {bonuses['proficiency']}, "
        bonuses_str += f"value = {bonuses['value']}, "
        bonuses_str += "}"
        musicSupportProficiencyBonuses.append(bonuses_str)
    lua_table += ', '.join(musicSupportProficiencyBonuses) + "},"
    # bonus
    lua_table += "bonus = {"
    lua_table  += f"defaultVocalBonus = {card.bonus['defaultVocalBonus']}, "
    lua_table += f"defaultDanceBonus = {card.bonus['defaultDanceBonus']}, "
    lua_table  += f"defaultVisualBonus = {card.bonus['defaultVisualBonus']}, "
    lua_table  += f"defaultMentalBonus = {card.bonus['defaultMentalBonus']}, "
    lua_table  += f"middleVocalBonus = {card.bonus['middleVocalBonus']}, "
    lua_table  += f"middleDanceBonus = {card.bonus['middleDanceBonus']}, "
    lua_table  += f"middleVisualBonus = {card.bonus['middleVisualBonus']}, "
    lua_table  += f"middleMentalBonus = {card.bonus['middleMentalBonus']}, "
    lua_table  += f"maxVocalBonus = {card.bonus['maxVocalBonus']}, "
    lua_table  += f"maxDanceBonus = {card.bonus['maxDanceBonus']}, "
    lua_table  += f"maxVisualBonus = {card.bonus['maxVisualBonus']}, "
    lua_table  += f"maxMentalBonus = {card.bonus['maxMentalBonus']}, "
    lua_table += "}"
   # produceSupportIdolEvents
    lua_table += "produceSupportIdolEvents = {"
    produceSupportIdolEvents = []
    for event in card.produceSupportIdolEvents:
        event_str = "{" 
        event_str += f"name = '{event['name']}', " 
        event_str += f"vocal = {event['vocal']}, "
        event_str += f"dance = {event['dance']}, "
        event_str += f"visual = {event['visual']}, "
        event_str += f"mental = {event['mental']}, "
        event_str += f"SP = {event['SP']} "
        event_str += "},"
        produceSupportIdolEvents.append(event_str)
    lua_table += ' '.join(produceSupportIdolEvents).rstrip(', ') + "},"  
    # fightSkill
    lua_table += "fightSkill = {"
    lua_table += f"name= '{card.fightSkill['name']}',"  
    lua_table += f"comment= '{card.fightSkill['comment']}'"  
    lua_table += "},"
    # supportSkills
    lua_table += "supportSkills = {"
    supportSkill = []
    for supSkill in card.supportSkills:
        supSkill_str += "{"
        supSkill_str += f"name = {supSkill['name']}, "
        supSkill_str += f"description = {supSkill['description']}, "
        supSkill_str += f"value = {supSkill['value']} "
        supSkill_str += "}"
        supportSkill.append(supSkill_str)
    lua_table += ', '.join(supportSkill) + "},"
    # supportIdolActiveSkill
    lua_table += "supportIdolActiveSkill = {"
    supportIdolActiveSkill = []
    for saSkill in card.supportIdolActiveSkill:
        saSkill_str += "{"
        saSkill_str += f"name = {saSkill['name']}, "
        saSkill_str += f"comment = {saSkill['comment']}"
        saSkill_str += "}"
        supportIdolActiveSkill.append(saSkill_str)
    lua_table += ', '.join(supportIdolActiveSkill) + "},"
    # Skill Panels
    lua_table += "skillPanels = {"
    skill_panels = []
    for panel in card.skillPanels:
        panel_str = "{"
        panel_str += f"sequence = {panel['sequence']}, "
        panel_str += f"step = {panel['step']}, "
        panel_str += f"name = '{panel['name']}', "
        panel_str += f"comment = '{panel['comment']}',"
        panel_str += f"color = '{panel['color']}'"
        panel_str += "}"
        skill_panels.append(panel_str)
    lua_table += ', '.join(skill_panels) + "}"
    lua_table += '}'
    return lua_table