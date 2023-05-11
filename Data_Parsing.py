# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sqlite3




RunInformation = []
ItemHeld = []
ItemName = []
RunCategories = ['gameModeName', 'gameEnding', 'runStopwatchValue', 'bodyName', 'totalKills', 'totalDamageDealt',
                 'totalDamageTaken', 'highestDamageDealt', 'totalGoldCollected', 'totalItemsCollected', 'totalPurchases', 'equipment']

temp_arrs = []

RunDifficulty = ['Hard', 'Normal', 'Easy', 'Eclipse']

ItemStack = ['AlienHead', 'ArmorPlate', 'ArmorReductionOnHit', 'ArtifactKey',
             'AttackSpeedAndMoveSpeed', 'AttackSpeedOnCrit','AutoCastEquipment', 'Bandolier',
             'BarrierOnKill', 'BarrierOnOverHeal', 'Bear', 'BearVoid', 'BeetleGland',
             'Behemoth', 'BleedOnHit', 'BleedOnHitAndExplode', 'BleedOnHitVoid',
             'BonusGoldPackOnKill', 'BossDamageBonus', 'BounceNearby', 'CaptainDefenseMatrix',
             'ChainLightning', 'ChainLightingVoid', 'Clover', 'CloverVoid', 'CritDamage',
             'CritGlasses', 'CritGlassesVoid', 'Crowbar', 'Dagger', 'DeathMark', 'DroneWeapons',
             'ElementalRingVoid', 'EnergizedOnEquipmentUse', 'EquipmentMagazine', 'EquipmentMagazineVoid',
             'ExecuteLowHealthElite', 'ExplodeOnDeath', 'ExplodeOnDeathVoid', 'ExtraLife','ExtraLifeVoid',
             'FallBoots', 'Feather', 'FireRing', 'FireballsOnHit', 'Firework', 'FlatHealth',
             'FocusConvergence', 'FragileDamageBonus', 'FreeChest', 'GhostOnKill', 'GoldOnHit',
             'GoldOnHurt', 'HalfAttackSpeedHalfCooldowns', 'HalfSpeedDoubleHealth',
             'HeadHunter', 'HealOnCrit', 'HealWhileSafe', 'HealingPotion', 'Hoof', 'IceRing',
             'Icicle', 'IgniteOnKill', 'ImmuneToDebuff', 'IncreaseHealing', 'Infusion',
             'JumpBoost', 'KillEliteFrenzy', 'Knurl', 'LaserTurbine', 'LightningStrikeOnHit',
             'LunarBadLuck','LunarDagger', 'LunarPrimaryReplacement', 'LunarSecondaryReplacement',
             'LunarSpecialReplacement', 'LunarSun', 'LunarTrinket', 'LunarUtilityReplacement',
             'Medkit', 'MinorConstructOnKill', 'Missile', 'MissileVoid', 'MonstersOnShrineUse',
             'MoreMissle', 'MoveSpeedOnKill', 'Mushroom', 'MushroomVoid', 'NearbyDamageBonus',
             'NovaOnHeal', 'NovaOnLowHealth', 'OutOfCombatArmor', 'ParentEgg', 'Pearl',
             'PermanentDebuffOnHit', 'PersonalShield', 'Phasing', 'Plant', 'PrimarySkillShuriken',
             'RandomDamageZone', 'RandomEquipmentTrigger', 'RandomlyLunar', 'RegeneratingScrap',
             'RepeatHeal', 'RoboBallBuddy', 'ScrapGreen', 'ScrapRed', 'ScrapWhite', 'ScrapYellow',
             'SecondarySkillMagazine', 'Seed', 'ShieldOnly', 'ShinyPearl', 'ShockNearby',
             'SiphonOnLowHealth', 'SlowOnHit', 'SlowOnHitVoid', 'SprintArmor',
             'SprintBonus', 'SprintOutOfCombat','SprintWisp', 'Squid', 'StickyBomb',
             'StrengthenBurn', 'StunChanceOnHit', 'Syringe', 'TPHealingNova', 'Talisman',
             'Thorns', 'TitanGoldDuringTP', 'Tooth', 'TreasureCache', 'TreasureCacheVoid',
             'UtilitySkillMagazine', 'VoidMegaCrabItem', 'WarCryOnMultiKill', 'WardOnLevel']


def Grab_Items(file):
    lineNum = 0
    temp = 0
    temp_index = 0
    temp_str = ''
    for line in file:
        for item in ItemStack:
            if line.find('Consumed')  != -1:
                #Do Nothing :)
                pog = '57 leaf Clover'
            elif line.find(item) != -1:
                line = line.strip()
                temp_index = line.find('>')
                temp_str = line[1:temp_index]
                #print(f' {temp_str} and {item}')
                if temp_str == item:
                    ItemName.append(item)
                    line = line.replace("<" + item + '>', '')
                    line = line.replace("</" + item + '>', '')
                    ItemHeld.append(int(line.strip()))
        if line.find('</itemStacks>') != -1:
            return


def read_file(fname):
    file = open(fname, encoding="utf8")
    num = 0
    for line in file:
        for cat in RunCategories:
            if line.find(cat) != -1:
                line = line.replace("<" + cat + '>', "")
                line = line.replace("</" + cat + '>', '')
                temp = line.strip()
                temp_arrs.append(cat)
                RunInformation.append(temp)
        if line.find('<ruleBook>') != -1:
            line = line.strip()
            ind = line.find('.')
            ind2 = line.find(' ')
            line = line[ind +1 : ind2]
            if line.find(RunDifficulty[0]) != -1:
                RunInformation.append(RunDifficulty[0])
            elif line.find(RunDifficulty[1]) != -1:
                RunInformation.append(RunDifficulty[1])
            elif line.find(RunDifficulty[2]) != -1:
                RunInformation.append(RunDifficulty[2])
            else:
                RunInformation.append(RunDifficulty[3])
        if line.find('<itemStacks>')  != -1:
            Grab_Items(file)
        if line.find('</PlayerInfo>') != -1:
            file.close()
            return
    file.close()

#If error its bc it was already ran on the DB
def add_Items_Data(cur):
    for Name in ItemStack:
        cur.execute(f'ALTER TABLE ItemData ADD {Name} INT DEFAULT 0;')

def insert_Data(cur):
    File = open("index.txt", "r+")
    ind = int(File.read())
    File.close()
    File = open('index.txt', 'w+')
    cur.execute("INSERT INTO RunData(GameMode, GameEnding, TimeAlive, Difficulty, Survivor, TotalKills, TotalDamageDealt, TotalDamageTaken, HighestDamageDealt, TotalGoldCollected, TotalItemsCollected, TotalPurchases, Equipment)  VALUES (:id, :end, :time, :diff, :surv, :kill, :dealt, :taken, :highest, :gold, :items, :purchase, :equip)",
                {
                    'id':RunInformation[0],
                    'end':RunInformation[1],
                    'time':RunInformation[2],
                    'diff':RunInformation[3],
                    'surv':RunInformation[4],
                    'kill':RunInformation[5],
                    'dealt':RunInformation[6],
                    'taken':RunInformation[7],
                    'highest':RunInformation[8],
                    'gold':RunInformation[9],
                    'items':RunInformation[10],
                    'purchase':RunInformation[11],
                    'equip':RunInformation[12],
                })
    if len(ItemName) > 0:
        temp = ",".join(ItemName)
        temp2 = ''
        for num in ItemHeld:
            temp2 += str(num) +', '
        temp2 = temp2[:len(temp2) - 2]
        cur.execute('INSERT INTO ItemData (runID, %s) VALUES ( %d , %s)' % (temp, ind , temp2))
        ind += 1
    else:
        cur.execute('INSERT INTO ItemData (runID) VALUES ( %d )' % (ind))
        ind += 1

    File.write(str(ind))
    File.close()

def defaults(arr):
    temp_arr = temp_arrs
    Cat_Arr = RunCategories
    temp_str = []
    print(Cat_Arr)
    print(temp_arr)
    for string in Cat_Arr:
        if string not in temp_arr:
            temp_str.append(string)
    print(temp_str)
    for val in temp_str:
        index = RunCategories.index(val)
        print(index)
        RunInformation.insert(index + 1, '0')
    print(RunInformation)

if __name__ == '__main__':
    db = sqlite3.connect('RoR_Data.db')
    cur = db.cursor()
    add_Items_Data(cur)
    link = os.listdir()
    for fname in link:
        if fname.find("xml") != -1:
            print(fname)
            read_file(fname)
            print(RunInformation)
            if len(RunInformation) < 13:
                defaults(RunInformation)
            insert_Data(cur)
            temp_arrs.clear()
            ItemName.clear()
            ItemHeld.clear()
            RunInformation.clear()
            print('\n\n')
    db.commit()
    cur.close()
