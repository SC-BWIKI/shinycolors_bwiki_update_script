import json
from card import *
from dic import *
def dic_sort(dic):
    dic = sorted(dic.items(),key=lambda item:len(item[0]),reverse=True)
    return dic

def word_translate (data,dic):
    dic = dic_sort(dic)
    for i,j in dic.items():
        data = data.replace(i,j)
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
    for i in range(0,len(pCardata.idol.memoryAppeals)-1):
        a = {"level":pCardata.idol.memoryAppeals[i].level,"name":word_translate(sentence_translate(pCardata.idol.memoryAppeals[i].name,skillSenDic),skillWordDic),
             "comment":word_translate(sentence_translate(pCardata.idol.memoryAppeals[i].comment,skillSenDic),skillWordDic)}
        data.memoryAppeals.append(a)
    #技能盘部分
    for i in range(0,len(pCardata.idol.skillPanels)-1):
        sequence = pCardata.idol.skillPanels[i].sequence
        step = pCardata.idol.skillPanels[i].step
        name = word_translate(sentence_translate(pCardata.idol.skillPanels[i].skill.name,skillSenDic),skillWordDic)
        comment = word_translate(sentence_translate(pCardata.idol.skillPanels[i].skill.comment,skillSenDic),skillWordDic)
        a = {"sequence":sequence,"step":step,"name":name,"comment":comment}
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
    for i in range(0,len(sCardata.musicSupportProficiencyBonuses)-1):
        a = {"proficiency":sCardata.musicSupportProficiencyBonuses[i].proficiency,"value":sCardata.musicSupportProficiencyBonuses[i].value}
    data.bonus = {}
    data.produceSupportIdolEvents = []
    data.fightSkill = {"name":sCardata.supportIdol.fightSkill.name,"comment":sCardata.supportIdol.fightSkill.comment}
    data.supportSkills = []
    data.supportIdolActiveSkill = []
    data.skillPanels = []

def setLuaTable(data):
    for i in data:
        pass