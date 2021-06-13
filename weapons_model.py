from  random import randint

class Weapon:
    def __str__(self):
        print(self.name, str(self.min_dmg),"-",str(self.max_dmg),"  ", str(self.accuracy), "% ", str(self.critical),"% ","w:", str(self.weight))    
    pass


class Sword(Weapon):
    def __init__(self, weapon_level):
        self.w_type = "W_CLASSIC" 
        self.w_subtype = "sword"
        self.weapon_level = weapon_level
        self.name =("Sword lvl." + str(weapon_level))
        self.min_dmg = 20
        self.max_dmg = 40
        self.accuracy = 50
        self.critical = 3
        self.weight = 10
        self.difficulty ="normal"
        self.parry = True
        self.range_min_dmg = 25
        self.range_max_dmg = 35
        self.range_accuracy = 35
        self.is_ranged = False
        self.is_close_impaired = False
        self.upgrade_level(self.weapon_level)

    def upgrade_level(self, number_of_levels):
        for level in range (0,number_of_levels):
            random_nr = randint(1,9)
            if random_nr in [1,2]:
                self.min_dmg += 1
            elif random_nr in [3,4]:
                self.max_dmg += 1              
            elif random_nr in [5]:           
                self.critical += 1
            elif random_nr in [6,7]:  
                self.accuracy +=1
            elif random_nr in [8]:
                self.weight  -= 1
            elif random_nr in [9]:
                self.weight += 1
                self.min_dmg += 1
                self.max_dmg += 2

class Axe(Weapon):
    def __init__(self, weapon_level):
        self.w_type = "W_CLASSIC" 
        self.w_subtype = "axe"
        self.weapon_level = weapon_level
        self.name =("Axe lvl." + str(weapon_level))
        self.min_dmg = 35
        self.max_dmg = 40
        self.accuracy = 40
        self.critical = 2
        self.weight = 11
        self.difficulty ="normal"
        self.parry = False
        self.range_min_dmg = 30
        self.range_max_dmg = 35
        self.range_accuracy = 50
        self.is_ranged = False
        self.is_close_impaired = False
        self.upgrade_level(self.weapon_level)

    def upgrade_level(self, number_of_levels):
        for level in range (0,number_of_levels):
            random_nr = randint(1,10)
            if random_nr in [1,2]:
                self.min_dmg += 1
            elif random_nr in [3,4]:
                self.max_dmg += 2              
            elif random_nr in [6,5]:  
                self.accuracy +=1
            elif random_nr in [7]:
                self.weight  -= 1
            elif random_nr in [9,8]:
                self.weight += 1
                self.min_dmg += 2
                self.max_dmg += 2
            elif random_nr in [10]:
                self.min_dmg -= 2
                self.max_dmg += 2            

class TwoHandedSword(Weapon):
    def __init__(self, weapon_level):
        self.w_type = "W_POLEARMS" 
        self.w_subtype = "sword"
        self.weapon_level = weapon_level
        self.name =("Two-handed sword lvl."+ str(weapon_level))
        self.min_dmg = 20
        self.max_dmg = 55
        self.accuracy = 50
        self.critical = 3
        self.weight = 17
        self.difficulty ="hard"
        self.parry = True
        self.range_min_dmg = 35
        self.range_max_dmg = 55
        self.range_accuracy = 10
        self.is_ranged = False
        self.is_close_impaired = False
        self.upgrade_level(self.weapon_level)

    def upgrade_level(self, number_of_levels):
        for level in range (0,number_of_levels):
            random_nr = randint(1,10)
            if random_nr in [1,2]:
                self.min_dmg += 2
            elif random_nr in [3]:
                self.max_dmg += 2              
            elif random_nr in [4]:  
                self.accuracy +=1
            elif random_nr in [5]:
                self.weight  -= 1
            elif random_nr in [6]:
                self.weight += 1
                self.min_dmg += 2
                self.max_dmg += 2
            elif random_nr in [7]:
                self.critical += 1

class Spear(Weapon):
    def __init__(self, weapon_level):
        self.w_type = "W_POLEARMS" 
        self.w_subtype = "spear"
        self.weapon_level = weapon_level
        self.name =("Spear lvl." + str(weapon_level))
        self.min_dmg = 15
        self.max_dmg = 25
        self.accuracy = 65
        self.critical = 4
        self.weight = 11
        self.difficulty ="normal"
        self.parry = False
        self.range_min_dmg = 30
        self.range_max_dmg = 50
        self.range_accuracy = 55
        self.is_ranged = False
        self.is_close_impaired = False
        self.upgrade_level(self.weapon_level)

    def upgrade_level(self, number_of_levels):
        for level in range (0,number_of_levels):
            random_nr = randint(1,10)
            if random_nr in [1]:
                self.min_dmg += 1
            elif random_nr in [2]:
                self.max_dmg += 2              
            elif random_nr in [3]:  
                self.accuracy -=1
                self.min_dmg += 1
                self.max_dmg += 2
            elif random_nr in [4]:
                self.min_dmg += 1
                self.max_dmg += 1
            elif random_nr in [5]:
                self.weight += 1
                self.min_dmg += 1
                self.max_dmg += 2
            elif random_nr in [6]:
                self.accuracy += 1 
            elif random_nr in [7]:
                self.critical += 1 
            elif random_nr in [8]:
                self.weight += 1             

class Dagger(Weapon):
    def __init__(self, weapon_level):
        self.w_type = "W_SMALL" 
        self.w_subtype = "dagger"
        self.weapon_level = weapon_level
        self.name =("Dagger lvl." + str(weapon_level))
        self.min_dmg = 10
        self.max_dmg = 25
        self.accuracy = 45
        self.critical = 10
        self.weight = 8
        self.difficulty ="normal"
        self.parry = False
        self.range_min_dmg = 20
        self.range_max_dmg = 30
        self.range_accuracy = 60
        self.is_ranged = False
        self.is_close_impaired = False
        self.upgrade_level(self.weapon_level)

    def upgrade_level(self, number_of_levels):
        for level in range (0,number_of_levels):
            random_nr = randint(1,7)
            if random_nr in [1,2]:
                self.max_dmg += 1
            elif random_nr in [4,3]:           
                self.critical += 1    
            elif random_nr in [5]:  
                self.accuracy +=1
            elif random_nr in [6]:
                self.weight  -= 1
            elif random_nr in [7]:
                self.weight += 1
                self.min_dmg += 1
                self.max_dmg += 3

class Bow(Weapon):
    def __init__(self, weapon_level):
        self.w_type = "W_BOW" 
        self.w_subtype = "bow"
        self.weapon_level = weapon_level
        self.name =("Bow lvl." + str(weapon_level))
        self.min_dmg = 10
        self.max_dmg = 25
        self.accuracy = 40
        self.critical = 3
        self.weight = 10
        self.difficulty ="normal"
        self.parry = False
        self.range_min_dmg = 20
        self.range_max_dmg = 30
        self.range_accuracy = 50
        self.is_ranged = True
        self.is_close_impaired = True
        self.upgrade_level(self.weapon_level)

    def upgrade_level(self, number_of_levels):
        for level in range (0,number_of_levels):
            random_nr = randint(1,7)
            if random_nr in [1]:
                self.range_min_dmg += 1
            if random_nr in [2]:
                self.range_max_dmg += 1           
            elif random_nr in [3]:           
                self.critical += 1    
            elif random_nr in [4]:  
                self.range_accuracy +=1
            elif random_nr in [5]:
                self.weight  -= 1
            elif random_nr in [6]:
                self.weight += 1
                self.range_min_dmg += 1
                self.range_max_dmg += 2

    def __str__(self):
        print(self.name, str(self.range_min_dmg),"-",str(self.range_max_dmg),"  ", str(self.range_accuracy), "% ", str(self.critical),"% ","w:", str(self.weight))    
                   
class Sling(Weapon):
    def __init__(self, weapon_level):
        self.w_type = "W_SPECIAL"
        self.w_subtype = "sling"
        self.weapon_level = weapon_level
        self.name =("Sling lvl." + str(weapon_level))
        self.min_dmg = 5
        self.max_dmg = 15
        self.accuracy = 55
        self.critical = 3
        self.weight = 6
        self.difficulty ="normal"
        self.parry = False
        self.range_min_dmg = 25
        self.range_max_dmg = 35
        self.range_accuracy = 45
        self.is_ranged = True
        self.is_close_impaired = True
        self.upgrade_level(self.weapon_level)

    def upgrade_level(self, number_of_levels):
        for level in range (0,number_of_levels):
            random_nr = randint(1,7)
            if random_nr in [1]:
                self.range_min_dmg += 1
            if random_nr in [2]:
                self.range_max_dmg += 1           
            elif random_nr in [3]:           
                self.critical += 1    
            elif random_nr in [4]:  
                self.range_accuracy +=1
                self.range_max_dmg -= 1 
            elif random_nr in [5]:
                pass
            elif random_nr in [6]:
                self.range_max_dmg += 2 
            elif random_nr in [7]:  
                self.range_accuracy -=1
                self.range_max_dmg += 2              
               
    def __str__(self):
        print(self.name, str(self.range_min_dmg),"-",str(self.range_max_dmg),"  ", str(self.range_accuracy), "% ", str(self.critical),"% ","w:", str(self.weight))   


class Wand(Weapon):
    def __init__(self, weapon_level):
        self.w_type = "M_MAGIC"
        self.w_subtype = "wand"
        self.weapon_level = weapon_level
        self.name =("Wand lvl." + str(weapon_level))
        self.min_dmg = 10
        self.max_dmg = 15
        self.accuracy = 40
        self.critical = 1
        self.weight = 6
        self.difficulty ="normal"
        self.parry = False
        self.range_min_dmg = 5
        self.range_max_dmg = 10
        self.range_accuracy = 45
        self.is_ranged = False
        self.is_close_impaired = True
        self.upgrade_level(self.weapon_level)

    def upgrade_level(self, number_of_levels):
        pass
               
    def __str__(self):
        print(self.name, str(self.min_dmg),"-",str(self.max_dmg),"do magic")   
        
        
x3 = Sword(5)
x4 = Sword(15)
x3.__str__()
x4.__str__()

x1 = Axe(5)
x2 = Axe(15)
x1.__str__()
x2.__str__()

x5 = Dagger(5)
x6 = Dagger(15)
x5.__str__()
x6.__str__()

x7 = Bow(5)
x8 = Bow(15)
x7.__str__()
x8.__str__()

x9 = Spear(5)
x10 = Spear(15)
x9.__str__()
x10.__str__()

x11 = TwoHandedSword(5)
x12 = TwoHandedSword(15)
x11.__str__()
x12.__str__()

x13 = Sling(5)
x14 = Sling(15)
x13.__str__()
x14.__str__()

x15 = Wand(5)
x15.__str__()