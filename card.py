class idolCard(object):
    def __init__(self,uid,name,get_med,rarity,bvId,unit):
        self.uid = uid
        self.name = name
        self.get_med = get_med #获得方式
        self.rarity = rarity #稀有度
        self.bvId = bvId #视频链接Bvid
        self.unit = unit #组合

class pCard (idolCard):
    def __init__(self, uid, name, get_med, rarity, bvId, unit,envApt,musicApt,pfmApt,memoryAppeals,skillPanels):
        super().__init__(uid, name, get_med, rarity, bvId, unit)
        self.envApt = envApt #dict
        self.musicApt = musicApt #dict
        self.pfmApt = pfmApt #dict
        self.memoryAppeals = memoryAppeals #list
        self.skillPanels = skillPanels #list
    
    def set_p_cardata(self):
        p_cardata = {"uid":self.uid,"name":self.name,"get_med":self.get_med,"rarity":self.rarity,"bvId":self.bvId,"unit":self.unit,
                     "envApt":self.envApt,"musicApt":self.musicApt,"pfmApt":self.pfmApt,"memoryAppeals":self.memoryAppeals,"skillPanels":self.skillPanels}
        return p_cardata

class sCard(idolCard):
    def __init__(self, uid, name, get_med, rarity, bvId, unit,inspirationAttribute,ideaMark,musicSupportProficiencyBonuses,
                 bonus,produceSupportIdolEvents,fightSkill,supportSkills,supportIdolActiveSkill,skillPanels):
        super().__init__(uid, name, get_med, rarity, bvId, unit)
        self.inspirationAttribute = inspirationAttribute #str
        self.ideaMark = ideaMark #str
        self.musicSupportProficiencyBonuses = musicSupportProficiencyBonuses #list
        self.bonus = bonus #dict
        self.produceSupportIdolEvents = produceSupportIdolEvents #list
        self.fightSkill = fightSkill #dict
        self.supportSkills = supportSkills #list
        self.supportIdolActiveSkill = supportIdolActiveSkill #list
        self.skillPanels = skillPanels #list